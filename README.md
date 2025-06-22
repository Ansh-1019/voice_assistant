# 🗣️ Voice Assistant – Friday

A beginner-friendly Python voice assistant that listens, understands, and responds to your voice commands.  
This project was built to explore **speech recognition**, **text-to-speech**, and **smart command execution** in Python.

---

## 🚀 Getting Started

To run the assistant:

```bash
python friday.py

## 🚀 Features

- 🎤 **Voice Input** — Recognizes your voice using the microphone  
- 🕓 **Tells the Time and Date** — Fetches current time and date on command  
- 🎵 **Plays Songs** — Plays songs on YouTube using `pywhatkit`  
- 😂 **Tells Jokes** — Lightens the mood with a random joke  
- 📖 **Wikipedia Summaries** — Provides brief summaries from Wikipedia  
- 🌐 **Google Search** — Searches the web for any topic  
- 🧠 **Wake Word Detection** — Activates when you say **"Friday"**

## 🛠️ Tech Stack

- Python 3.13  
- `speech_recognition` – Speech-to-text  
- `pyttsx3` – Text-to-speech  
- `pywhatkit` – YouTube/Google automation  
- `wikipedia` – Search summaries  
- `pyjokes` – Random jokes for fun  

## 🗂️ Project Structure
 voice_assistant/
├── friday.py # Main assistant logic
├── stt.py # (Optional) Speech-to-text module
├── tts.py # (Optional) Text-to-speech module
├── combine.py # (Optional) Testing combined features
└── README.md # Project overview and setup instructions

