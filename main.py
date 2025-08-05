from voice.listen import listen
from voice.speak import speak
from query_engine import smart_answer

def main():
    speak("Hi! Ask me anything about your college.")
    while True:
        query =listen().lower()
        print("You said:", query)
        if "exit" in query:
            speak("Goodbye!")
            break
        answer=smart_answer(query)
        speak(answer)
if __name__=="__main__":
    main()
