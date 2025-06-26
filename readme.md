# Aizen - Offline AI Desktop Assistant

**Aizen** is a voice-activated AI assistant that runs locally on your Windows system. It can open any installed application, search the web, type dictated text, and respond with conversational intelligence powered by a local LLaMA 3 model. It features offline voice recognition (Vosk), TTS, intent parsing, and app control.

---

## 🔧 Features

-  **Offline Voice Recognition** using [Vosk](https://alphacephei.com/vosk/)
-  **Conversational AI** using [LLaMA 3 via Ollama](https://ollama.com/)
-  **Intelligent App Launcher** with fuzzy matching (RapidFuzz)
-  **Custom Voice Personality**: Speaks like Sosuke Aizen from *Bleach*
-  **Modular Design**: Easily extendable and readable architecture
-  **Natural Command Parsing**: Opens apps, types text, or searches based on free-form prompts
-  **No API Keys Required**: Fully local and offline

---

## 📁 Project Structure

```

Aizen/
├── main.py                    # Main orchestrator loop
├── app\_index.json             # App name to path mappings
├── vosk-model-small-en-us-0.15/  # Vosk model directory
├── Functions/
│   ├── **init**.py
│   ├── speech\_engine.py       # Handles text-to-speech
│   ├── listener.py            # Voice recognition using Vosk
│   ├── llama\_interface.py     # Sends prompts to local LLaMA
│   ├── commands.py            # Parses and executes commands
│   ├── model\_loader.py        # Loads the Vosk model and recognizer
├── script.py                   #run this to create app indexes on your local machine
├── training.py                 #run this to train a Classifier with a custom json dataset

````

---

## 🛠️ Requirements

- Python 3.10+
- [Ollama](https://ollama.com/) (running `llama3` model locally)
- [Vosk Model](https://alphacephei.com/vosk/models) (e.g. `vosk-model-small-en-us-0.15`)

Install dependencies:

```bash
pip install -r requirements.txt
````


---

##  Usage

1. Create your `app_index.json` in the root folder:


2. Start the Ollama LLaMA 3 server:

```bash
ollama run llama3
```

3. Run the assistant:

```bash
python main.py
```

---

##  Examples

* “Open Chrome”
* “Type Hello world”
* “Search machine learning courses”
* “What’s the time?”
* “Goodbye”

---

##  Future Improvements

* Replace pyttsx3 with **Coqui TTS** for a high-quality, expressive Japanese male voice
* Memory + context using a lightweight vector DB
* Training an **intent classifier** for better accuracy
* Auto-index new apps on system

---

##  Notes

* The assistant runs entirely **offline**
* Ollama must be running in the background for conversation to work
* `vosk-model-small-en-us-0.15` must be extracted into the root or included in the `dist` build


