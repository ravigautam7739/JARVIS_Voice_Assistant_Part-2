# 🤖 Advanced Jarvis Voice Assistant (Wake Word Enabled AI)

A Python-based **AI Voice Assistant** that activates only when you say a **wake word ("Hey Jarvis")**, making it more realistic and efficient.

This project simulates a **real-world virtual assistant** with voice commands, smart responses, and controlled activation.

---

# 🚀 Features

✔ Wake word activation ("Hey Jarvis") 🎙️
✔ Smart listening mode (sleep → active → sleep)
✔ Voice command recognition
✔ Text-to-speech responses 🔊
✔ Opens websites (Google, Facebook)
✔ Performs web searches
✔ Tells current time
✔ Natural conversational responses

---

# 🛠 Technologies Used

* Python
* SpeechRecognition
* Pyttsx3 (Text-to-Speech)
* Webbrowser
* Datetime

---

# 📂 Project Structure

```id="w8m2zx"
advanced-jarvis-assistant
│
├── main.py
└── README.md
```

👉 Rename your file to **main.py** for a clean and professional structure.

---

# ⚙️ Installation

1️⃣ Install Python 3.x

2️⃣ Install required libraries:

```bash id="p9n3kl"
pip install SpeechRecognition pyttsx3 pyaudio
```

⚠️ If `pyaudio` fails:

```bash id="x2k9pl"
pip install pipwin
pipwin install pyaudio
```

---

# ▶️ How to Run

```bash id="k7p2zl"
git clone https://github.com/ravigautam7739/advanced-jarvis-assistant.git
cd advanced-jarvis-assistant
python main.py
```

---

# 🧠 How It Works

1. System starts with a welcome message
2. Assistant stays in **sleep mode**
3. Waits for wake word → **"Hey Jarvis"**

### 📌 Activation Flow:

* "Hey Jarvis" → Assistant wakes up
* Executes one command
* Returns to sleep mode

4. Commands include:

   * Open websites
   * Search Google
   * Tell time
   * Respond conversationally

---

# 💻 Example Commands

```id="z8p2wl"
"Hey Jarvis"
"Open Google"
"Search AI tools"
"What is the time"
"Thank you"
"Stop"
```

---

# 💻 Example Output

```id="m9n4pt"
Welcome back sir. Systems are online and ready.

Listening...

You said: hey jarvis

Jarvis: Yes sir, I'm listening.

You said: open google

Jarvis: Opening Google
Jarvis: Google is on your screen
```

---

# 🎯 Use Cases

* Personal voice assistant
* Smart home automation (base system)
* Voice-controlled computing
* AI learning projects
* Automation demos

---

# ⚠️ Notes

* Requires microphone
* Internet needed for speech recognition
* Works best in low-noise environment
* Wake word detection is keyword-based (not AI-trained)

---

# 🔮 Future Improvements

* AI-based wake word detection
* ChatGPT integration 🤖
* Control system apps (volume, files, etc.)
* GUI interface
* Continuous conversation mode
* Multi-language support

---

# ⭐ Support

If you found this project useful, give it a **star ⭐**.

---

# 📱 Follow for More Projects

I regularly share **Python, AI, and automation projects**.

Stay tuned 🚀
