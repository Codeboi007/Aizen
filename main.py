from Functions.speech import speak
from Functions.listener import listen
from Functions.llama import ask_llama,parse_and_execute

def main():
    speak("Hello! I’m your offline assistant with AI, ready to help you.")

    while True:
        user_input = listen()
        if user_input:
            llama_response = ask_llama(user_input)
            speak(llama_response)
            parse_and_execute(llama_response)

if __name__ == "__main__":
    main()
