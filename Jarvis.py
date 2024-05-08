#PROJECT 1 - PY BOT
import pyttsx3
import speech_recognition as sr
import datetime
import os
#import cv2
import random
from requests import get
import wikipedia
import webbrowser
import pywhatkit


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
#print(voices[0].id)
engine.setProperty('voices',  voices[0].id)

# text to speach
def speak(audio):
    engine.say(audio)
    print(audio)
    engine.runAndWait()

def wishme():
    speak("welcome back Sir!!")
    pause_threshold =2
    speak("All systems for your interface will be prepaired in few seconds")
    pause_threshold =20
    hour = datetime.datetime.now().hour
    if hour >=6 and hour<12:
        speak("Good morning sir!")
    elif hour >=12 and hour<16:
        speak("Good afternoon sir!")
    elif hour >=16 and hour<24:
        speak("Good evening sir!")   
    else:
        speak("Good night sir!")
    pause_threshold =5
    speak("Your Bot is ready at your service. Please tell me how can i help you?")

wishme()

def time():
    Time = datetime.datetime.now().strftime("%I:%M:%S")
    speak(Time)

def date():
    year = int(datetime.datetime.now().year)
    month = int(datetime.datetime.now().month)
    day = int(datetime.datetime.now().day)
    speak(date)
    speak(month)
    speak(year)
def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recongnizing...")
        query = r.recognize_google(audio, language='en-in')
        print(query)

    except Exception as e:
        print(e)
        speak("Say that again please....")

        return "None"
    return query

if __name__ == "__main__":
    
        #while True:
        if 1:
            query = takeCommand().lower()

        #logic building for task

        if "alexa" in query:
         speak("sir!!")
         pause_threshold =15
         speak("how can i help You")

        elif "what is the time" in query:
            speak("the current time is")
            time()

        elif "what is today's date" in query:
            speak("todays date is")
            date()

        elif "open notepad" in query:
            npath = "C:\\Windows\\system32\\notepad.exe" 
            os.startfile(npath)
        
        elif "open calculator" in  query:
            cpath = "C:\\Windows\\system32\\calc.exe "
            os.startfile(cpath)

        elif "wikipedia" in query:
            speak("searching wikipedia.....")
            query = query.replace("wikipedia"," ")
            results = wikipedia.summary(query, sentences=2)
            speak("according to wikipedia")
            speak(results)
            print(results)

        elif "what is my ip address" in query:
            ip = get('https://api.ipify.org').text
            speak("your IP Address is {ip}")

        elif "open youtube" in query:
            webbrowser.open("www.youtube.com")

        elif "open google" in query:
            speak("sir! what should i search on google")
            cm = takeCommand().lower()
            webbrowser.open(f"{cm}")
           
        elif "shutdown" in query:
            speak("thank you for using me sir, have a good day!!!")
            pause_threshold =15
            speak("all systems are shutting down please wait")
            pause_threshold =50
            speak("Ten seconds remaining for shuttingdown")
            pause_threshold =500
            speak("good bye sir!!")
            sys.Exception()
            

