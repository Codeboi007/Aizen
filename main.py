import pyttsx3
import subprocess
import pyautogui
import webbrowser
import datetime
import time
import json
from vosk import Model, KaldiRecognizer
import pyaudio

# Initialize voice engine
engine = pyttsx3.init()

# Load Vosk model
model = Model("vosk-model-small-en-us-0.15")
recognizer = KaldiRecognizer(model, 16000)

# PyAudio setup
p = pyaudio.PyAudio()
stream = p.open(format=pyaudio.paInt16, channels=1, rate=16000,
                input=True, frames_per_buffer=8192)
stream.start_stream()

def speak(text):
    print("Assistant:", text)
    engine.say(text)
    engine.runAndWait()

def listen():
    print("🎤 Listening with Vosk...")
    while True:
        data = stream.read(4096, exception_on_overflow=False)
        if recognizer.AcceptWaveform(data):
            result = json.loads(recognizer.Result())
            command = result.get("text", "")
            if command:
                print("You said:", command)
                return command.lower()

# Handle voice commands
def handle_command(command):
    if "chrome" in command:
        speak("Opening Chrome.")
        subprocess.Popen("C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe")
    elif "code" in command:
        speak("Opening Visual Studio Code.")
        subprocess.Popen("C:\\Users\\YourUsername\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe")
    elif "search" in command:
        speak("What should I search for?")
        query = listen()
        webbrowser.open(f"https://www.google.com/search?q={query}")
        speak(f"Searching for {query}")
    elif "type" in command:
        speak("What should I type?")
        text = listen()
        pyautogui.typewrite(text)
    elif "time" in command:
        now = datetime.datetime.now().strftime("%I:%M %p")
        speak(f"The time is {now}")
    elif "exit" in command or "bye" in command:
        speak("Goodbye, master.")
        exit()
    else:
        speak("Sorry, I don't know that command.")

# Startup greeting
speak("Hello! I’m your offline assistant, ready to help you.")

# Main loop
while True:
    command = listen()
    if command:
        handle_command(command)
    time.sleep(1)
