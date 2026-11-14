# 🌐 Multilingual Audio & Text Summarizer

A multilingual text and audio summarization tool built with **Python** and **Gradio**. It summarizes text or speech, converts audio to text, translates the summary, and can read it aloud.

🔗 **Live Demo:** [Hugging Face Space](https://huggingface.co/spaces/kit28aiml021/multilingual-audio-text-summarizer)

---

## 📌 Table of Contents

1. [Overview](#-overview)
2. [Features](#-features)
3. [Problem Statement](#-problem-statement)
4. [Abstract](#-abstract)
5. [How It Works](#-how-it-works)
6. [Installation](#-installation)
7. [Running the App](#-running-the-app)
8. [Gradio Interface](#-gradio-interface)
9. [Project Structure](#-project-structure)
10. [Output Screenshots](#-output-screenshots)
11. [Related Papers](#-related-papers)
12. [Project Reflection](#-project-reflection)
13. [Contributing](#-contributing)
14. [License](#-license)

---

## 🔎 Overview

This project can:

- 📝 Summarize text in any language
- 🎙 Summarize audio / speech
- 🔊 Convert audio → text (Speech-to-Text)
- 🌍 Translate summaries into multiple languages
- 🗣 Generate voice output (Text-to-Speech)

---

## ✨ Features

- ✔ Supports multiple languages: English, Hindi, Tamil, Spanish, German, French
- ✔ Upload audio and automatically convert it to text
- ✔ Automatic language detection
- ✔ Adjustable summary length
- ✔ Voice output using gTTS
- ✔ Runs on Google Colab or a local machine
- ✔ Clean Gradio UI

---

## ❓ Problem Statement

Large amounts of information are shared today through long text documents, audio recordings, lectures, and spoken content. Reading or listening to all of it takes a lot of time and effort, especially for multilingual users.

There is a need for a system that can automatically summarize long text or audio, convert speech to text, and translate content into different languages so users can quickly grasp the main ideas.

This project develops a **Multilingual Audio and Text Summarizer** that takes text or audio input, generates a concise summary, and optionally provides translated or voice-based output. It helps users save time, overcome language barriers, and access key information from lengthy content.

---

## 📄 Abstract

The growing volume of text and audio information on digital platforms calls for efficient tools that help users extract meaningful insights quickly. This project presents a Multilingual Audio and Text Summarizer that processes both written text and spoken audio to generate concise summaries.

The system integrates speech-to-text conversion, language detection, machine translation, and text-to-speech technologies to support users across multiple languages. Using a **TF-IDF-based approach**, it identifies key sentences and produces a simplified representation of the original content.

The Gradio interface makes the tool easy to use: users can enter text or upload audio, adjust summary length, choose the output language, and enable voice output. The project aims to reduce information overload, overcome language barriers, and provide an accessible tool for students, researchers, and general users.

---

## ⚙️ How It Works

| Stage | Technology | Details |
|---|---|---|
| **Text Summarization** | TF-IDF scoring | Sentence tokenization, stopword removal, term-frequency weighting, sentence ranking |
| **Speech-to-Text** | SpeechRecognition + Google Speech API | Supports `.wav`, `.mp3`, `.m4a`, etc. |
| **Translation** | `deep-translator` (GoogleTranslator) | Translates summaries into the chosen language |
| **Text-to-Speech** | `gTTS` | Generates voice output in the selected language |

---

## 🛠 Installation

Install the Python dependencies:

```bash
pip install gradio deep-translator langdetect gTTS SpeechRecognition pydub
```

Install FFmpeg (needed for audio processing):

```bash
sudo apt-get update && sudo apt-get install -y ffmpeg
```

---

## ▶️ Running the App

Save your Python script and run:

```bash
python app.py
```

Or launch it inside **Google Colab** (fully supported).

---

## 🖥 Gradio Interface

The app provides:

- Text input box
- Audio upload
- Slider to control summary length
- Dropdown to select language
- Checkbox to enable voice output

```python
iface = gr.Interface(
    fn=summarize_colab,
    inputs=[ ... ],
    outputs=[ ... ]
)
iface.launch(share=True)
```

---

## 📁 Project Structure

```
Multilingual-Audio-Summarizer/
├── app.py
├── requirements.txt
├── README.md
├── samples/
└── output/
```

---

## 🖼 Output Screenshots

<img width="1269" height="512" alt="Output screenshot 1" src="https://github.com/user-attachments/assets/2798007b-b0ff-4434-b4d2-ac3bba4256ce" />

<img width="1144" height="478" alt="Output screenshot 2" src="https://github.com/user-attachments/assets/73442880-b055-4906-a657-421d18dfb019" />

---

## 📚 Related Papers

- **Single Document Automatic Text Summarization using Term Frequency-Inverse Document Frequency (TF-IDF)**: extractive summarization using TF-IDF, similar to the method used here.
- **Extractive Text and Video Summarization using TF-IDF Algorithm**: extractive summarization for text (and video) using TF-IDF.
- **From Speech to Summary: A Comprehensive Survey of Speech Summarization**: a recent survey of speech-to-summary methods.
- **A Survey of Text Summarization: Techniques, Evaluation and Challenges**: a broader overview of techniques, evaluation methods, and challenges.

---

## 💭 Project Reflection

I am **Gopika**, a student of Computer Science (Artificial Intelligence and Machine Learning).

Completing this project for the first time has been a truly meaningful learning experience. Many concepts were new to me, such as text processing, speech recognition, translation, and building an interactive interface with Gradio. Working through each part step by step helped me understand how different technologies connect to form a complete application.

I learned how to debug, structure code, handle errors, and think from a user's perspective. This project improved my technical skills and boosted my confidence to build more advanced projects in the future. It marks an important milestone in my journey as a CSE (AI & ML) student, and I am proud of the progress I made.

---

## 🤝 Contributing

Pull requests and feature suggestions are welcome!

---

## 📜 License

This project is licensed under the **MIT License**.
