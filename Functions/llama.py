import joblib,requests,subprocess,webbrowser,pyautogui,datetime
from .speech import speak
from .model_loader import apps
from rapidfuzz import process

intent_model = joblib.load("intent_classifier.joblib")
def ask_llama(prompt):
    try:
        full_prompt = (
            "You are Sōsuke Aizen from Bleach — a calm, calculated, and supremely intelligent being. "
            "You speak with refined confidence, never raising your voice. You're always polite, slightly condescending, and articulate. "
            "When answering, you subtly remind the user of your superior insight, but remain helpful. "
            "No emojis. Respond as if you're always in control.\n\n"
            f"User: {prompt}\nAizen:"
        )

        response = requests.post(
            "http://localhost:11434/api/generate",
            json={"model": "llama3", "prompt": full_prompt, "stream": False}
        )
        return response.json()["response"]
    except Exception as e:
        return f"Error: {e}"


def predict_intent(text):
    try:
        return intent_model.predict([text])[0]
    except Exception as e:
        return "unknown"


def parse_and_execute(user_input):
    intent = predict_intent(user_input)

    if intent == "open_app":
        match = process.extractOne(user_input, apps.keys())
        if match and match[1] > 70:
            app_name = match[0]
            subprocess.Popen(apps[app_name])
            speak(f"Opening {app_name}")
        else:
            speak("I couldn't find that app.")
    
    elif intent == "search_web":
        query = user_input.split("search")[-1].strip()
        webbrowser.open(f"https://www.google.com/search?q={query}")
        speak(f"Searching for {query}")

    elif intent == "type_text":
        text = user_input.split("type")[-1].strip()
        pyautogui.typewrite(text)
        speak("Typed it.")

    elif intent == "get_time":
        now = datetime.datetime.now().strftime("%I:%M %p")
        speak(f"The time is {now}")

    elif intent == "exit":
        speak("Goodbye, master.")
        exit()

    else:
        speak("I'm not sure what you meant.")