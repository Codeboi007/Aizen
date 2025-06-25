Absolutely. Here's a clean, professional `README.md` based solely on what you've implemented **up to this point**, leaving Coqui TTS and advanced features in the "Future Improvements" section:

---

````markdown
# Aizen: Offline Voice Assistant for Windows

Aizen is a local desktop voice assistant that runs entirely offline. It listens for commands, speaks responses, and helps navigate the system with minimal reliance on keyboard or mouse. Inspired by Sosuke Aizen (*Bleach*), it uses Vosk for offline speech recognition and pyttsx3 for voice output.

---

## Features

- Offline speech recognition using Vosk
- Text-to-speech responses via pyttsx3
- Open installed applications using fuzzy matching
- Web search via voice commands
- Text input simulation
- Time reporting
- Startup logging and persistent model paths
- Configurable to run at system startup

---

## Requirements

- Windows 10/11
- Python 3.10+
- A functional microphone
- Basic text-to-speech voices installed (e.g., Microsoft Zira, David, Hazel)

---

## Installation

### 1. Clone the repository

```bash
git clone https://github.com/Codeboi007/Aizen.git
cd Aizen
````

### 2. Create a virtual environment and activate it

```bash
python -m venv Aizen
Aizen\Scripts\activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

---

## Vosk Model Setup

1. Download the model: [vosk-model-small-en-us-0.15](https://alphacephei.com/vosk/models)
2. Extract the folder `vosk-model-small-en-us-0.15` into the project directory

Example directory layout:

```
Aizen/
├── main.py
├── vosk-model-small-en-us-0.15/
├── app_index.json
```

---

## Usage

Run the assistant:

```bash
python main.py
```

You can use voice commands like:

* `open chrome`
* `search python tutorial`
* `type hello world`
* `what time is it`
* `exit`

---

## Building as Executable

To package the assistant as a standalone Windows `.exe`:

```bash
pyinstaller main.spec
```

Move the resulting `.exe` from `dist/` into your system's startup folder to launch Aizen automatically on boot:

```
C:\Users\<YourUsername>\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup
```

---

## App Indexing

Aizen builds a searchable `app_index.json` by scanning installed applications. It uses fuzzy matching to recognize voice commands and open the correct executable.

---

## Logs and Debugging

* `assistant_log.txt` stores startup logs and execution notes
* `model_debug.txt` confirms the Vosk model path used during runtime

---

## Future Improvements

* Integrate Coqui TTS for more natural voice synthesis
* Add LLaMA 3 for conversational capabilities
* Support context-aware multi-turn conversation
* Custom voice styles (e.g., Sosuke Aizen's tone)
* Dynamic configuration panel

---

