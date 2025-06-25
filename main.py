import pyttsx3,subprocess,pyautogui,webbrowser,datetime,time,json,os,sys,requests,pyaudio
from vosk import Model, KaldiRecognizer
from rapidfuzz import process


with open("app_index.json", "r") as f:
    apps = json.load(f)


with open("C:\\Users\\User\\assistant_log.txt", "a") as f:
    f.write("Assistant started at " + str(datetime.datetime.now()) + "\n")

# Vosk logging
if getattr(sys, 'frozen', False):
    os.environ['PATH'] += os.pathsep + sys._MEIPASS


engine = pyttsx3.init()

def speak(text):
    print("Assistant:", text)
    engine.say(text)
    engine.runAndWait()

#Vosk function
def get_model_path():
    if getattr(sys, 'frozen', False):
        return os.path.join(sys._MEIPASS, "vosk-model-small-en-us-0.15")
    return os.path.join(os.path.dirname(__file__), "vosk-model-small-en-us-0.15")

model = Model(get_model_path())
recognizer = KaldiRecognizer(model, 16000)


p = pyaudio.PyAudio()
stream = p.open(format=pyaudio.paInt16, channels=1, rate=16000,
                input=True, frames_per_buffer=8192)
stream.start_stream()

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

#Llama3 usage
def ask_llama(prompt):
    try:
        full_prompt = (
        "You are Sōsuke Aizen from Bleach— a calm, calculated, and supremely intelligent being. "
        "You speak with refined confidence, never raising your voice. "
        "You're always polite, slightly condescending, and articulate. "
        "When answering, you subtly remind the user of your superior insight, but you are still helpful. "
        "Do not use emojis. Respond as if you're always in control.\n\n"
        f"User: {prompt}\nAizen:"
    )

        response = requests.post(
        "http://localhost:11434/api/generate",
        json={"model": "llama3", "prompt": full_prompt, "stream": False}
    )
        return response.json()["response"]
    except Exception as e:
        return f"Error: {e}"


def parse_and_execute(llama_response):

    if "open" in llama_response:
        match = process.extractOne(llama_response, apps.keys())
        if match and match[1] > 70:
            app_name = match[0]
            subprocess.Popen(apps[app_name])
            speak(f"Opening {app_name}")
            return True

    if "search" in llama_response:
        query = llama_response.split("search")[-1].strip()
        webbrowser.open(f"https://www.google.com/search?q={query}")
        speak(f"Searching for {query}")
        return True

    if "type" in llama_response:
        text = llama_response.split("type")[-1].strip()
        pyautogui.typewrite(text)
        return True

    if "time" in llama_response:
        now = datetime.datetime.now().strftime("%I:%M %p")
        speak(f"The time is {now}")
        return True

    if "exit" in llama_response or "bye" in llama_response:
        speak("Goodbye, master.")
        exit()

    return False  

\
speak("Hello! I’m your offline assistant with AI, ready to help you.")

while True:
    user_input = listen()
    if user_input:
        llama_response = ask_llama(user_input)
        speak(llama_response)
        parse_and_execute(llama_response)
    time.sleep(1)
