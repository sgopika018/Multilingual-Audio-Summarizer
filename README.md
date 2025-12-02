Iam Gopika from computer science of artificial intelligence and machine learning department.Completing this project for the first time has been a truly meaningful learning experience. When I started, many concepts were new to me—such as text processing, speech recognition, translation, and building an interactive interface with Gradio. Working through each part step by step helped me understand how different technologies connect to form a complete application. I learned how to debug, structure code, handle errors, and think from a user’s perspective. This project not only improved my technical skills but also boosted my confidence to create more advanced projects in the future. It marks an important milestone in my journey as a CSE (AI & ML) student, and I am proud of the progress I made while building it.
# Multilingual-Audio-Summarizer
A multilingual text and audio summarizer built using Python and Gradio.   It can summarize text or speech in any language, convert audio to text, translate content, and generate voice output for summaries.
A multilingual text + audio summarization tool built using Python, Gradio, and speech/translation APIs.
This project can:
Summarize text in any language
  🎙Summarize audio/speech
  🔊Convert audio → text (Speech-to-Text)
  🌐Translate summaries into multiple languages
  🗣Generate voice output (Text-to-Speech)
  
Features
✔ Supports multiple languages (English, Hindi, Tamil, Spanish, German, French)
✔ Upload audio and automatically convert to text
✔ Auto-language detection
✔ Adjustable summary length
✔ Voice output using gTTS
✔ Runs on Google Colab or local machine
✔ Clean Gradio UI

 Installation

1. Install dependencies
pip install gradio deep-translator langdetect gTTS SpeechRecognition pydub
sudo apt-get update && sudo apt-get install -y ffmpeg

▶ Run the App
Save your Python script and run:
python app.py
Or launch inside Google Colab (fully supported).

  How It Works

Text Summarization
Uses a TF–IDF scoring algorithm with:
sentence tokenization
stopword removal
term-frequency weight
ranking of sentences
Speech to Text
Uses SpeechRecognition + Google Speech API
(.wav, .mp3, .m4a etc. supported)

Translation
Uses GoogleTranslator (deep-translator library).
Text to Speech (TTS)
Uses gTTS to generate voice output in selected language.

Gradio Interface

Your app provides:
Text input
Audio upload
Sliders to control summary length
Dropdown for language
Checkbox for voice output
iface = gr.Interface(
    fn=summarize_colab,
    inputs=[ ... ],
    outputs=[ ... ]
)
iface.launch(share=True)

Project Structure
Multilingual-Audio-Summarizer/
│── app.py
│── requirements.txt
│── README.md
│── samples/
│── output/

Contributing
Pull requests and feature suggestions are welcome!

📄License
MIT License

Output:
<img width="1269" height="512" alt="image" src="https://github.com/user-attachments/assets/2798007b-b0ff-4434-b4d2-ac3bba4256ce" />
<img width="1144" height="478" alt="image" src="https://github.com/user-attachments/assets/73442880-b055-4906-a657-421d18dfb019" />

 # Problem Statement
 In today’s world, large amounts of information are shared through long text documents, audio recordings, lectures, and spoken content. Manually reading or listening to all this information takes a lot of time and effort, especially for multilingual users. There is a need for a system that can automatically summarize long text or audio, convert speech to text, and translate content into different languages so that users can quickly understand the main ideas.
This project aims to develop a Multilingual Audio and Text Summarizer that can take text or audio input, generate a concise summary, and optionally provide translated or voice-based output. The system helps users save time, overcome language barriers, and easily access key information from lengthy content.

 # Abstract
 The increasing volume of text and audio information in digital platforms has created a need for efficient tools that can help users quickly extract meaningful insights. This project presents a Multilingual Audio and Text Summarizer capable of processing both written text and spoken audio to generate concise, accurate summaries. The system integrates speech-to-text conversion, language detection, machine translation, and text-to-speech technologies to support users across multiple languages. Using a TF–IDF–based approach, the model identifies key sentences and produces a simplified representation of the original content. The Gradio interface ensures ease of use by allowing users to input text or upload audio files, adjust summary length, choose the output language, and enable voice output. This project aims to reduce information overload, overcome language barriers, and provide an accessible tool for students, researchers, and general users needing quick, multilingual summarization.

 # Some example link
 Extractive Text and Video Summarization using TF‑IDF Algorithm — describes extractive summarization for text (and video) using TF-IDF, similar to the method you use. 

Single Document Automatic Text Summarization using TF‑IDF — a basic text-summarization paper using TF-IDF for a single document. 

Summarizing Speech: A Comprehensive Survey — a survey paper on speech summarization (speech/audio → summary), covering techniques relevant to summarizing spoken content.

# Papers Related
Single Document Automatic Text Summarization using Term Frequency-Inverse Document Frequency (TF-IDF) — Describe extractive summarization using TF-IDF. 

From Speech to Summary: A Comprehensive Survey of Speech Summarization — A recent survey covering speech-to-summary methods. 

A survey of text summarization: Techniques, evaluation and challenges — Provides a broader overview of text summarization techniques, evaluation methods and challenges.
 


