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
       
def news():
    main_url = 'http://newsapi.org/v2/top-headlines?sources=techcrunch&apiKey=6863afd1ce5f4262bd31c7d09feab819'
    main_page = requests.get(main_url).json()
    articles = main_page["articles"]
    head = []
    day = ["first","second","third","fourth","fifth","sixth","seventh","eighth","ninth","tenth"]
    for ar in articles:
        head.append(ar["title"])
    for i in range (len(day)):
        speak(f"today's {day[i]} news is {head[i]}")

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
            
        elif "switch the tab" in query:
            pyautogui.keyDown("alt")
            pyautogui.press("tab")
            time.sleep(1)
            pyautogui.keyUp("alt")
            
        elif "tell me news" in query:
            speak("please wait sir, feteching the latest news")
            news()
            
        elif "where i am" in query:
            speak("wait sir, let me check")
            try:
                ipAdd = requests.get('https://api.ipify.org').text
                print(ipAdd)
                url = 'https://get.geojs.io/v1/ip/geo/'+ipAdd+'.json'
                geo_requests = requests.get(url)
                geo_data = geo_requests.json()
                city = geo_data['city']
                country = geo_data['country']
                speak(f"sir i am not sure, but i think we are in {city} city of {country} country")
            except Exception as e:
                speak("sorry sir, Due to network issue i am not able to find where we are.")
                pass
            
        elif "instagram profile" in query or "profile on instagram" in query:
            speak("sir please enter user name correctly.")
            name = input("Enter user name")
            webbrowser.open(f"www.instagram.com/{name}")
            speak(f"sir here is the profile of the user {name}")
            time.sleep(2)
            speak("sir would you like to download the profile picture of this account")
            condition = takecommand().lower()
            if "yes" in condition:
                mod = instaloader.Instaloader()
                mod.download_profile(name, profile_pic_only = True)
                speak("i am done sir, profile picture is saved in our main folder. now i am ready for next command")
            else:
                pass
            
        elif "take screenshot" in query or "take a screenshot" in query:
            speak("sir, please tell me the name for this screenshot file")
            name = takecommand().lower()
            speak("please sir hold the screen for few seconds, i am taking screenshot")
            time.sleep(2)
            img = pyautogui.screenshot()
            img.save(f"{name}.png")
            speak("i am done sir, the screenshot is saved in our main folder. now i am ready for next command.")
