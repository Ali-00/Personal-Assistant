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
            
        elif "wikipedia" in query:
            speak("searching wikipedia....")
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to wikipedia")
            speak(results)
            print(results)
            
        elif "ip address" in query:
            ip = get('https://api.ipify.org').text
            speak(f"Your IP address is {ip}")
            
        elif "open youtube" in query:
            webbrowser.open("www.youtube.com")

        elif "open facebook" in query:
            webbrowser.open("www.facebook.com")
            
        elif "open stack overflow" in query:
            webbrowser.open("www.stackoverflow.com")
            
        elif "open google" in query:
            speak("sir, what should i search on google")
            cm = takecommand().lower()
            webbrowser.open(f"{cm}")
            
        elif "play song on youtube" in query:
            speak("sir, which song should i play for you...")
            yt = takecommand().lower()
            kit.playonyt(f"{yt}")
            
        elif "send email" in query:
            
            speak("sir what should i say")
            query = takecommand().lower()
            if "send a file" in query:
                email = 'email.com' # Your email
                password = 'password'
                send_to_email = 'person@gmail.com'
                speak("okay sir, what is the subject for this email")
                query = takecommand().lower()
                subject = query
                speak("and sir, what is the message for this email")
                query2 = takecommand().lower()
                message = query2
                speak("sir please enter the correct path of the file into the shell")
                file_location = input("please enter the path here")

                speak("please wait, i am sending email now")

                msg = MIMEMultipart()
                msg['From'] = email
                msg['To'] = send_to_email
                msg['Subject'] = subject

                msg.attach(MIMEText(message, 'plain'))

                filename = os.path.basename(file_location)
                attachment = open(file_location, "rb")
                part = MIMEBase('application', 'octet-stream')
                encoders.encode_base64(part)
                part.add_header('Content-Dispositon', "attachment; filename= %s" % filename)

                msg.attach(part)

                server = smtplib.SMTP('smtp.gmail.com', 587)
                server.starttls()
                server.login(email,password)
                text = msg.as_string()
                server.sendmail(email,send_to_email,text)
                server.quit()
                speak("email has been sent")
              
            else:
                email = 'muzamalali.a@gmail.com'
                password = 'password'
                send_to_email = 'person@gmail.com'
                message = query

                server = smtplib.SMTP('smtp.gmail.com', 587)
                server.starttls()
                server.login(email, password)
                server.sendmail(email, send_to_email, message)
                server.quit()
                speak("email has been sent")
                
        elif "you can sleep" in query:
            speak("thanks for using me sir, have a good day.")
            sys.exit()

        elif "set alarm" in query:
            nn = int(datetime.datetime.now().hour)
            if nn==22:
                music_dir = "C:\\Users\\Hp\\Downloads\\Video" #give path of tone
                songs = os.listdir(music_dir)
                os.startfile(os.path.join(music_dir, songs[0]))
                
        elif "tell me a joke" in query:
            joke = pyjokes.get_joke()
            speak(joke)

        elif "shut down the system" in query:
            os.system("shutdown /s /t 5")
            
        elif "restart the system" in query:
            os.system("shutdown /r /t 5")

        elif "sleep the system" in query:
            os.system("rundll32.exe powrprof.dll,SetSuspendState 0,1,0")
