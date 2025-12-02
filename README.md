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
<img width="1144" height="478" alt="image" src="https://github.com/user-attachments/assets/73442880-b055-4906-a657-421d18dfb019" />
![Uploading image.png…]()

