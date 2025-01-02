import pyttsx3
import speech_recognition as sr
import eel

def speak(text):
    engine = pyttsx3.init('sapi5')
    voices = engine.getProperty('voices')
    engine.setProperty('voice',voices[1].id)
    engine.setProperty('rate',174)
    engine.say(text)
    engine.runAndWait()


@eel.expose
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
        speak(query)
        eel.ShowHood()
    except Exception as e:
        print(f"Error: {e}")  # Optional: prints the error if there's an exception
        return ""
    
    return query.lower()
   
   
   
    