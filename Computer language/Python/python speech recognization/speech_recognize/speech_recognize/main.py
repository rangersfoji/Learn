import speech_recognition as sr # pip install speechRecognition
import pyttsx3 # pip install pyttsx3
import wikipedia # pip install wikipedia
import webbrowser
import smtplib

import my_google_websites
import my_search_in_google
import onedrive

from threading import Thread
from multiprocessing import Process

import datetime
import time
import random

import os

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
rate = engine.getProperty('rate')




engine.setProperty('voice',voices[2].id)
rate = engine.setProperty('rate',160) # speak speed

# master name
master = 'master'


# speak function (text --> voice)
def speak(text):
    engine.say(text)
    engine.runAndWait()


# listen function (voice --> text)
def take_command():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print('Listening...')
        r.pause_threshold = 1
        r.energy_threshold = 5000
        audio = r.listen(source)
    
    try:
        print('Recognizing...')
        query = r.recognize_google(audio,language='en-us')
        print(query)
    except:
        print('Please say that again!!!')
        print()
        return 'None'
    print()
    return query.lower()



# other functions

# wish me(good morning)
def wishMe():
    hour = int(datetime.datetime.now().hour)
    
    if hour>= 0 and hour<12:
        speak('Good morning '+master)
    elif hour>=12 and hour<18:
        speak('Good afternoon '+master)
    else:
        speak('Good Evening '+master)

# wikipedia 
def wiki(sentence):
    query = sentence.replace('wikipedia','')
    try : 
        results = wikipedia.summary(query,sentences=10)
    except:
        results = 'Not found anything..'
    print(query,'? : ',results)
    speak('According to wikipedia ' + results)
    print()
    print()

# play music
def play_music():
    songs_dir = r"C:\Users\Karan\Music"

    # create list of music
    songs = os.listdir(r"C:\Users\Karan\Music")

    # generate random number
    song_num = random.randint(0,len(songs)-1)

    # play music
    os.startfile(os.path.join(songs_dir,songs[song_num]))
    
# tell current time
def tell_time():
    time = datetime.datetime.now().strftime("%H:%M")
    def convert_time(time):
        old_time = time
        hour = int(time[0:2])
        min = int(time[-2:])

        re_hour = -1

        # hour
        if hour == 0:
            re_hour = 12
        elif 0 < hour < 13:
            re_hour = hour
        elif hour > 12 :
            re_hour = hour - 12


        time = float(hour+(min/100))


        # am / pm
        add = ''

        # pm
        if 24.00>=time> 11.59:
            add = 'PM'
        # am
        else:
            add = 'AM'
        
        time = str(re_hour)+':'+str(min)+' '+add
        return  time
    time = convert_time(time)
    speak(f'{master} it\'s {time} now')

# open any application, here(vscode)
def start_vscode():
    # how to get codepath
    # right click on app , go to properties , copy target (path)
    codePath = r"C:\Users\Karan\AppData\Local\Programs\Microsoft VS Code\Code.exe"
    os.startfile(codePath)

# send email
def send_email(to,content):
    server = smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.ehlo()

    server.login('abc078382@gmail.com','Password12344321')

    server.sendmail('abc078382@gmail.com',to,content)
    server.close()

# open scripts folder in cmd
def add_python_module():
    before = os.getcwdb().decode("utf-8")  # convert byte to string (decoding byte)
    os.chdir(r"C:\Users\Bradford Mobil\AppData\Local\Programs\Python\Python37\scripts")
    os.system("start cmd  " )
    os.chdir(before)

# open python scripts folder
def python_script():
    before = os.getcwdb().decode("utf-8")  # convert byte to string (decoding byte)
    script_dir = r"C:\Users\Bradford Mobil\AppData\Local\Programs\Python\Python37\scripts"
    os.startfile(script_dir)
    os.chdir(before)

# open many webstites in google
def websites_in_google():
    speak('What do you want to search sir?')

    ans = take_command()
    while ans == 'None':
        speak('Please say that again sir.')
        ans = take_command()

    t = Process(target=my_google_websites.google_search,args=[ans])
    t.start()  
    

# search in google
def search_in_google():
    speak('What do you want to search sir?')

    ans = take_command()
    while ans == 'None':
        speak('Please say that again sir.')
        ans = take_command()

    t = Process(target=my_search_in_google.google_search,args=[ans])
    t.start()


# onedrive
def onedrive_start():
    t = Process(target=onedrive.main,args=[300])
    t.start()
    
 

    

if __name__ == '__main__':
    webbrowser.open('google.com')
    wishMe()
    speak('how are you doing today?')


    while True:

        query = take_command()

        # wikipedia
        if 'wikipedia' in query:
            t = Process(target=wiki,args=[query])
            t.start()
           


        # open websties in browser
        elif 'open youtube' in query:  # here  webbrowser.open use 'default browser'
            webbrowser.open('youtube.com')  # how ever it's not functional like selenium webscraping

        elif 'open google' in query:
            webbrowser.open('google.com')

        elif 'open stack overflow' in query:
            webbrowser.open('stackoverflow.com')

        
        # play music
        elif 'play music' in query:
            t = Process(target=play_music)
            t.start()
            


        # ask time
        elif 'what\'s the time' in query:
            t = Process(target=tell_time)
            t.start()


        # open any application here(vscode)
        elif 'open vs code' in query or 'open v s code' in query or 'open visual studio code' in query:
            t = Process(target=start_vscode)
            t.start()

        
        # send email
        elif 'send email' in query:

            def send(to,content):
                try:    
                    send_email(to,content)
                    speak('email has been sent successfully!!')
                except:
                    speak('there is some server issue, please try again later!!')
            
            speak('What should i send?')


            content = take_command()
            while content == 'None':
                speak('Please say that again sir.')
                content = take_command()
            to = 'rangersfoji1@gmail.com'

            t = Process(target=send,args=[to,content])
            t.start()

           
        # open python script folder
        elif 'python script' in query:
            t = Process(target=python_script)
            t.start()

        # open script folder in cmd
        elif 'add module' in query:
            t = Process(target=add_python_module)
            t.start()
            
            
        # serve websites in google
        elif 'website in google' in query:
            websites_in_google()

        # search in google
        elif 'search in google' in query:
            search_in_google()

        # open onedrive
        elif 'onedrive' in query:
            onedrive_start()

        # exit
        elif 'exit python' in query:
            speak('ok {master} bye, catch you later')
            exit()


        





 

        


        