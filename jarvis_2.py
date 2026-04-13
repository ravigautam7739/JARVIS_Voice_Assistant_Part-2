import speech_recognition as sr
import pyttsx3
import webbrowser
import datetime

engine = pyttsx3.init()
engine.setProperty('rate', 170)

def speak(text):
    print("Jarvis:", text)
    engine.say(text)
    engine.runAndWait()

def take_command():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source)

    try:
        command = r.recognize_google(audio)
        print("You said:", command)
        return command.lower()
    except:
        return ""

# 🔥 Startup Message (IMPORTANT)
speak("Welcome back sir. Systems are online and ready.")

active = False  # Jarvis sleeps until wake word

while True:
    command = take_command()

    # Wake word
    if "hey jarvis" in command:
        active = True
        speak("Yes sir, I'm listening.")
        continue

    if not active:
        continue

    # Commands
    if "open facebook" in command:
        speak("Opening YouTube")
        webbrowser.open("https://facebook.com")
        speak("YouTube is now ready")

    elif "open google" in command:
        speak("Opening Google")
        webbrowser.open("https://google.com")
        speak("Google is on your screen")

    elif "time" in command:
        time_now = datetime.datetime.now().strftime("%H:%M")
        speak(f"The time is {time_now}")

    elif "search" in command:
        query = command.replace("search", "")
        speak(f"Searching for {query}")
        webbrowser.open(f"https://www.google.com/search?q={query}")
        speak("Here are the results")

    elif "thank you" in command:
        speak("Always here to help, sir")

    elif "stop" in command or "exit" in command:
        speak("Shutting down. Have a great day sir.")
        break

    # Reset to sleep after command (optional realistic behavior)
    active = False