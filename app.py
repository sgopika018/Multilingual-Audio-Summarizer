import math
import os
import re
import tempfile
from collections import Counter

import gradio as gr
import speech_recognition as sr
from deep_translator import GoogleTranslator
from gtts import gTTS
from langdetect import detect, LangDetectException
from pydub import AudioSegment

# Keeps the app working even if the Space hardware is set to ZeroGPU.
# (Harmless on CPU hardware.)
try:
    import spaces

    @spaces.GPU
    def _gpu_placeholder():
        return None
except Exception:
    pass


# -------------------- Stopwords and tokenization --------------------

STOPWORDS = {
    "a", "an", "the", "and", "or", "but", "if", "while", "with", "to",
    "from", "in", "on", "at", "for", "of", "by", "as", "is", "am",
    "are", "was", "were", "be", "been", "being", "it", "its", "this",
    "that", "these", "those", "he", "she", "they", "them", "his", "her",
    "their", "you", "your", "i", "me", "my", "we", "our", "us", "do",
    "does", "did", "doing", "done", "not", "no", "nor"
}

SENTENCE_SPLITTER = re.compile(r'(?<=[.!?])\s+')
WORD_PATTERN = re.compile(r"[A-Za-z0-9']+")


# -------------------- Text summarization --------------------

def split_sentences(text):
    text = str(text).strip()
    if not text:
        return []
    text = re.sub(r"\s+", " ", text)
    return SENTENCE_SPLITTER.split(text)


def tokenize(text):
    return [word.lower() for word in WORD_PATTERN.findall(text)]


def build_vocab(sentences):
    term_frequency = Counter()
    for sentence in sentences:
        for word in tokenize(sentence):
            if word not in STOPWORDS and len(word) > 1:
                term_frequency[word] += 1
    return term_frequency


def compute_idf(sentences, vocabulary):
    total_sentences = len(sentences)
    document_frequency = Counter()

    for sentence in sentences:
        seen_words = {
            word for word in tokenize(sentence)
            if word in vocabulary
        }
        document_frequency.update(seen_words)

    return {
        word: math.log((1 + total_sentences) / (1 + document_frequency[word])) + 1
        for word in vocabulary
    }


def sentence_scores(sentences, term_frequency, inverse_document_frequency):
    scores = []

    for index, sentence in enumerate(sentences):
        words = [word for word in tokenize(sentence) if word in term_frequency]

        if not words:
            scores.append((0.0, index))
            continue

        score = sum(
            term_frequency[word] * inverse_document_frequency[word]
            for word in words
        ) / (len(words) ** 0.8)

        scores.append((score, index))

    return scores


def summarize(text, ratio=0.4, min_sentences=2, max_sentences=5):
    sentences = split_sentences(text)
    if not sentences:
        return ""

    term_frequency = build_vocab(sentences)
    if not term_frequency:
        count = min(len(sentences), int(min_sentences))
        return " ".join(sentences[:count])

    inverse_document_frequency = compute_idf(sentences, term_frequency)
    scores = sentence_scores(
        sentences, term_frequency, inverse_document_frequency
    )

    selected_count = int(round(len(sentences) * float(ratio)))
    selected_count = max(int(min_sentences), selected_count)
    selected_count = min(int(max_sentences), selected_count, len(sentences))
    selected_count = max(1, selected_count)

    top_indices = [
        index
        for _, index in sorted(scores, key=lambda item: item[0], reverse=True)[:selected_count]
    ]
    top_indices.sort()

    return " ".join(sentences[index] for index in top_indices)


# -------------------- Speech-to-text --------------------

SPEECH_LOCALES = {
    "en": "en-IN",
    "ta": "ta-IN",
    "hi": "hi-IN",
    "fr": "fr-FR",
    "de": "de-DE",
    "es": "es-ES",
}


def recognize_with_locale(recognizer, audio_data, locale):
    """Returns (transcript, confidence). Empty transcript if nothing understood."""
    try:
        result = recognizer.recognize_google(
            audio_data, language=locale, show_all=True
        )
    except sr.UnknownValueError:
        return "", 0.0

    if not result or "alternative" not in result:
        return "", 0.0

    best = result["alternative"][0]
    return best.get("transcript", ""), best.get("confidence", 0.5)


def speech_to_text(audio_path, audio_lang="auto"):
    if not audio_path:
        return None

    recognizer = sr.Recognizer()
    wav_path = audio_path
    temporary_wav = None

    try:
        extension = os.path.splitext(audio_path)[1].lower()

        if extension != ".wav":
            temporary_wav = tempfile.NamedTemporaryFile(
                suffix=".wav", delete=False
            )
            temporary_wav.close()
            AudioSegment.from_file(audio_path).export(
                temporary_wav.name, format="wav"
            )
            wav_path = temporary_wav.name

        with sr.AudioFile(wav_path) as source:
            audio_data = recognizer.record(source)

        if audio_lang in SPEECH_LOCALES:
            text, _ = recognize_with_locale(
                recognizer, audio_data, SPEECH_LOCALES[audio_lang]
            )
        else:
            # Auto: try every supported language, keep the most confident result
            text, best_confidence = "", -1.0
            for locale in SPEECH_LOCALES.values():
                candidate, confidence = recognize_with_locale(
                    recognizer, audio_data, locale
                )
                if candidate and confidence > best_confidence:
                    text, best_confidence = candidate, confidence

        if not text:
            return "⚠ Could not understand the audio."
        return text

    except Exception as error:
        return f"⚠ Speech recognition error: {error}"
    finally:
        if temporary_wav and os.path.exists(temporary_wav.name):
            os.remove(temporary_wav.name)


def translate_text(text, source, target):
    """Translate in chunks (the translator limits each request to ~5000 characters)."""
    pieces = [text[i:i + 4000] for i in range(0, len(text), 4000)]
    translator = GoogleTranslator(source=source, target=target)
    return " ".join(translator.translate(piece) for piece in pieces if piece.strip())


# -------------------- Main application function --------------------

def summarize_audio_text(
    input_text,
    ratio,
    min_sentences,
    max_sentences,
    output_lang,
    voice_output,
    audio_file,
    audio_lang
):
    if audio_file:
        transcribed_text = speech_to_text(audio_file, audio_lang)
        if not transcribed_text or transcribed_text.startswith("⚠"):
            return transcribed_text or "⚠ Audio could not be processed.", None
        input_text = transcribed_text

    if not input_text or not str(input_text).strip():
        return "⚠ Please enter text or upload an audio file.", None

    try:
        try:
            input_language = detect(input_text)
        except LangDetectException:
            input_language = "en"

        # The original project translates non-English input to English
        # before applying its extractive summarization algorithm.
        english_text = input_text
        if input_language != "en":
            english_text = translate_text(input_text, "auto", "en")

        summary = summarize(
            english_text,
            ratio=ratio,
            min_sentences=int(min_sentences),
            max_sentences=int(max_sentences)
        )

        if output_lang != "en" and summary:
            summary = translate_text(summary, "en", output_lang)

        audio_output_path = None
        if voice_output and summary:
            tts = gTTS(text=summary, lang=output_lang)
            temporary_mp3 = tempfile.NamedTemporaryFile(
                delete=False, suffix=".mp3"
            )
            temporary_mp3.close()
            tts.save(temporary_mp3.name)
            audio_output_path = temporary_mp3.name

        return summary, audio_output_path

    except Exception as error:
        return f"⚠ Error: {error}", None


# -------------------- Gradio interface --------------------

demo = gr.Interface(
    fn=summarize_audio_text,
    inputs=[
        gr.Textbox(
            lines=10,
            placeholder="Type or paste your text here...",
            label="Input Text"
        ),
        gr.Slider(
            minimum=0.1, maximum=0.9, value=0.4,
            label="Summary Ratio"
        ),
        gr.Slider(
            minimum=1, maximum=5, value=2, step=1,
            label="Minimum Sentences"
        ),
        gr.Slider(
            minimum=1, maximum=10, value=5, step=1,
            label="Maximum Sentences"
        ),
        gr.Dropdown(
            choices=[
                ("English", "en"),
                ("Hindi", "hi"),
                ("French", "fr"),
                ("German", "de"),
                ("Spanish", "es"),
                ("Tamil", "ta")
            ],
            label="Output Language",
            value="en"
        ),
        gr.Checkbox(
            label="Enable Voice Output",
            value=False
        ),
        gr.Audio(
            sources=["upload", "microphone"],
            type="filepath",
            label="Upload Audio (optional)"
        ),
        gr.Dropdown(
            choices=[
                ("Auto-detect", "auto"),
                ("English", "en"),
                ("Tamil", "ta"),
                ("Hindi", "hi"),
                ("French", "fr"),
                ("German", "de"),
                ("Spanish", "es")
            ],
            label="Spoken language in audio",
            value="auto"
        )
    ],
    outputs=[
        gr.Textbox(label="Summary Output"),
        gr.Audio(label="Voice Output", type="filepath")
    ],
    title="Multilingual Audio Text Summarizer",
    description=(
        "Enter text or upload an audio file. The application transcribes "
        "audio, detects the input language, translates text for summarization, "
        "generates a concise summary, and can produce voice output."
    )
)

if __name__ == "__main__":
    demo.launch()
