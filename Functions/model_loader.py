import os,json,sys
from vosk import Model, KaldiRecognizer

def get_resource_path(filename):
    if getattr(sys, 'frozen', False):
        return os.path.join(sys._MEIPASS, filename)
    return os.path.join(os.path.abspath("."), filename)

try:
    with open(get_resource_path("app_index.json"), "r") as f:
        apps = json.load(f)
except FileNotFoundError:
    print("❌ app_index.json not found.")
    apps = {}


def get_model_path():
    if getattr(sys, 'frozen', False):
        return os.path.join(sys._MEIPASS, "D:/Programming/Aizen/vosk-model-small-en-us-0.15")
    return os.path.join(os.path.dirname(__file__), "D:/Programming/Aizen/vosk-model-small-en-us-0.15")

model = Model(get_model_path())
recognizer = KaldiRecognizer(model, 16000)