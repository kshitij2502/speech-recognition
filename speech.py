from speech_recognition import *
from requests import *
from pyttsx3 import *
from smtplib import *
from wikipedia import *
from webbrowser import *
from datetime import *
from os import *
from math import *
e=init('sapi5')
v=e.getProperty('voices')
e.setProperty('voices',v[1].id)
def sendEmail(to, content):
    server = SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('bhrishikesh36@gmail.com', '0024158879')
    server.sendmail('bhrishikesh36@gmail.com',to,content)
    server.close()
    speak("sent")
        

def speak(g):
    e.say(g)
    e.runAndWait()
def greetings():
    h=int(datetime.now().hour)
    if h>=0 and h<12:
        speak("Good Morning")
    if h>=12 and h<16:
        speak("Good Afternoon")
    if h>=16:
        speak("Good Evening")
    speak("This is Albert Sir How may I help you")
def ear():
    r=Recognizer()
    with Microphone() as source:
        print("......I am listening.......")
        r.pause_threshold=1
        audio=r.listen(source)
    try:
        print(".......Recognizing........")
        h=r.recognize_google(audio)
        print("User command",h)
        return h
    except:
        speak("Say that again please could not hear")
        ear()
while(True):
    greetings()
    p=ear()
    if p=="bye" or p=="quit" or p=="shut down":
        speak("Have a nice day")
        break
    
    if p=="open Wikipedia":
        speak("What do you want to search in wikipdia")
        m=ear()
        if m=="go back":
            continue
        o=summary(m)
        print(o)
        speak(o)
    elif p=="what is the time":
        g=datetime.now().second
        h=datetime.now().hour
        m=datetime.now().minute
        speak("The time is {} hours {} minutes {} seconds".format(h,m,g))
    elif p=="what is the date":
        h=datetime.now().day
        i=datetime.now().strftime("%B")
        j=datetime.now().year
        speak("The date is {} {} {}".format(h,i,j))
    elif p=="open Google":
        open_new("http://www.google.com")
    elif p=="open Facebook":
        open_new("www.facebook.com")
    elif p=="open WhatsApp web":
        open_new("https://web.whatsapp.com/")
    elif p=="current weather":
        url="https://www.accuweather.com/en/in/mumbai/3352495/weather-forecast/3352495"
        open_new(url)
    elif p=="perform arithmetic calculation":
        speak("Enter the expression")
        m=ear()
        if m=="go back":
            continue
        try:
            k=m.replace("plus","+")
            k=k.replace("divided by","/")
            k=k.replace("into","*")
            k=k.replace("minus","-")
            k=k.replace(" ","")
            k=k.replace("cube","**3")
            k=k.replace("raise to","**")
            k=k.replace("square","**2")
            speak("The answer is {}".format(eval(k)))
        except:
            speak("Sorry could not evaluate")
    elif p=="send email":
        u=input("Message:")
        y=input("Recipient:")
        sendEmail(y,u)
    
    
