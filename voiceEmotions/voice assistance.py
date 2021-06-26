import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
def speak (audio):
    engine.say(audio)
    engine.runAndWait()

engine = pyttsx3.init('espeak')
voices = engine.getProperty('voices')

if __name__=="__main__":
    speak("Hello world!")


def wishme ():
    hour = int(datetime.datetime.now().hour)
    if hour >=0 and hour<12:
        speak("Good Morning!")
    elif hour >=12 and hour <18:
        speak("Good Afternoon")
    else:
        speak("Good evening")

    speak("Welcome!")

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening....")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognising....")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        print("say that again please")
        return None
    return query

if __name__ == "__main__":
    wishme()
    while True:
        query = takeCommand().lower()

        if 'wikipedia' in query:
            speak("Searching wikipedia!")
            query = query.replace("wikipedia","")
            results = wikipedia.summary(query, sentences = 2)
            speak(results)
            print(results)
        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Ma ' am, time is {strTime}")




