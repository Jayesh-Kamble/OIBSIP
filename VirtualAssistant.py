import speech_recognition as sr
import pyttsx3
import datetime
import wikipedia
import webbrowser


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
print(voices[1].id)
engine.setProperty('voice',voices[1])



def speak(audio):
    engine.say(audio)
    engine.runAndWait()
def wishme():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")
    elif hour>=12 and hour<18:
        speak("Good afternoon!")
    else:
        speak("Good Evening!")        
    speak("I am VA sir, Please tell me how may i help you")

def takeCommand():
    '''
    It takes microphone input from the user and returns string output
    '''
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("Recognizing...")
        query = r.recognize_google(audio,language='en-in')   
        print(f"User Said:{query}\n") 
    except Exception as e:
        print(e)
        print("Say that again Please...")    
        return "None"
    return query    
if __name__ == "__main__":
    wishme()
    while 5:
        query = takeCommand().lower()

        # logic for executing task
        if 'wikipedia' in query:
            speak("Searching wikipedia...")
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to wikipedia")
            print(results)
            speak(results)
        
        elif 'open youtube' in query:
            webbrowser.open_new("youtube.com")
       
                
        elif 'open google' in query:
            webbrowser.open_new("google.com") 
        
        elif 'open Oasis Infobyte' in query:
            webbrowser.open_new("oasisinfobyte.com")         

        elif 'what is the time'in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")    
            speak(f"The Time is {strTime}")
    

    
  