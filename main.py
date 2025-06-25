import pyttsx3
import subprocess
import pyautogui
import webbrowser
import datetime
import time
import json
import os
import sys
import pyaudio
from vosk import Model, KaldiRecognizer

# Ensure libvosk.dll loads correctly when frozen
if getattr(sys, 'frozen', False):
    os.environ['PATH'] += os.pathsep + sys._MEIPASS

# Logging assistant start
with open("C:\\Users\\User\\assistant_log.txt", "a") as f:
    f.write("Assistant started at " + str(datetime.datetime.now()) + "\n")

# Initialize voice engine
engine = pyttsx3.init()

# Get correct model path for bundled .exe or source script
def get_model_path():
    if getattr(sys, 'frozen', False):
        base_path = sys._MEIPASS
    else:
        base_path = os.path.dirname(__file__)
    return os.path.join(base_path, "vosk-model-small-en-us-0.15")

model_path = get_model_path()

# Debug file to confirm path
with open("C:\\Users\\User\\model_debug.txt", "w") as f:
    f.write("Model path used: " + model_path + "\n")

# Load Vosk model
model = Model(model_path)
recognizer = KaldiRecognizer(model, 16000)

# PyAudio setup
p = pyaudio.PyAudio()
stream = p.open(format=pyaudio.paInt16, channels=1, rate=16000,
                input=True, frames_per_buffer=8192)
stream.start_stream()

# Text-to-speech
def speak(text):
    print("Assistant:", text)
    engine.say(text)
    engine.runAndWait()

# Voice input
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

# Command handler
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

# Start
speak("Hello! I’m your offline assistant, ready to help you.")

# Loop
while True:
    command = listen()
    if command:
        handle_command(command)
    time.sleep(1)
