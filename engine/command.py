import pyttsx3
import speech_recognition as sr
import eel
import time

def speak(text):
    engine = pyttsx3.init('sapi5')
    voices = engine.getProperty('voices')
    engine.setProperty('voice',voices[1].id)
    engine.setProperty('rate',174)
    eel.DisplayMessage(text)
    engine.say(text)
    engine.runAndWait()


def takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:  # Add parentheses to correctly instantiate the Microphone
        print("Listening...")
        eel.DisplayMessage('Listening....')
        r.pause_threshold = 1
        r.adjust_for_ambient_noise(source)
        
        audio = r.listen(source, 10, 6)
        
    try:
        print("Recognizing...")
        eel.DisplayMessage('Recognizing...')
        query = r.recognize_google(audio, language='en-in')
        print(f"user said: {query}")  # Corrected the f-string formatting
        eel.DisplayMessage(query);
        time.sleep(2)
    except Exception as e:
        print(f"Error: {e}")  # Optional: prints the error if there's an exception
        return ""
    
    return query.lower()

@eel.expose
def allCommands():
    
    try:
        query = takecommand()
        print(query)   
        if "open" in query:
            from engine.features import openCommand
            openCommand(query)
        elif "on youtube":
            from engine.features import PlayYoutube
            PlayYoutube(query)
        else:
            print("not run")
    except:
        print("error")
    eel.ShowHood()
       
   
    