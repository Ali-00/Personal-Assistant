import pyttsx3
import speech_recognition as sr
import datetime
import os
import cv2
import random
from requests import get
import wikipedia
import webbrowser
import pywhatkit as kit
import smtplib
import sys
import time
import pyjokes
import pyautogui
import news_module
import requests
import instaloader
import PyPDF2

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[0].id)
engine.setProperty('voices', voices[0].id)


def speak(audio):
    engine.say(audio)
    print(audio)
    engine.runAndWait()

def takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source, timeout=10, phrase_time_limit=5)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"user said: {query}")

    except Exception as e:
        speak("Say that again please...")
        return "none"
    return query

def wish():
    hour = int(datetime.datetime.now().hour)
    tt = time.strftime("%I:%M %p")

    if hour>=0 and hour<=12:
        speak(f"Good Morning, its {tt}")
    elif hour>12 and hour<=18:
        speak(f"Good Afternoon, its {tt}")
    else:
        speak(f"Good Evening, its {tt}")
    speak("I am assistant sir. Please tell me how can I help you")

if __name__ == "__main__":
    wish()
    
    while True:

        query = takecommand().lower()

        if "open notepad" in query:
            npath = "C:\\Windows\\system32\\notepad.exe"
            os.startfile(npath)
            
        elif "open notepad for writing" in query:
            speak("what should i write on notepad file...")
            ck = takecommand().lower()
            f = open("record.txt", "w")
            f.write(ck)
            f.close()

        elif "what is your name" in query:
            speak("People call me assistant. I am created by ali.")
            
        elif "open adobe reader" in query:
            npath = "C:\\Program Files (x86)\\Adobe\\Reader 11.0\\Reader\\AcroRd32.exe"
            os.startfile(npath)
            
        elif "open command prompt" in query:
            os.system("start cmd")

        elif "close notepad" in query:
            speak("ok sir, closing notepad")
            os.system("taskkill /f /im notepad.exe")
            
        elif "open camera" in query:
            cap = cv2.VideoCapture(0)
            while True:
                ret, img = cap.read()
                cv2.imshow('webcam', img)
                k = cv2.waitKey(50)
                if k==27:
                    break;
            cap.release()
            cv2.destroyAllWindows()
            
        elif "play music" in query:
            music_dir = "C:\\Users\\Hp\\Downloads\\Video" #give your own music directory path
            songs = os.listdir(music_dir)
            rd = random.choice(songs)
            os.startfile(os.path.join(music_dir, rd))
