# use python 3.7.4
# pip install pyttsx3
# pip isntall pywin32   # for windows this addtional package
# pip install speechRecognition

# pip install windows 32 / 64 pyaudio from website for python 3.7.4
# move it to scripts and then pip install file_name.whl


import speech_recognition as sr # pip install speechRecognition
import pyttsx3 # pip install pyttsx3
import wikipedia # pip install wikipedia
import webbrowser
import smtplib

import datetime
import time
import random

import os

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
rate = engine.getProperty('rate')




engine.setProperty('voice',voices[1].id)
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
        results = wikipedia.summary(query,sentences=5)
    except:
        results = 'Not found anything..'
    speak('According to wikipedia ' + results)
    print(query,'? : ',results)
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


if __name__ == '__main__':
    wishMe()
    speak('how are you doing today?')


    while True:

        query = take_command()

        # wikipedia
        if 'wikipedia' in query:
            wiki(query)


        # open websties in browser
        elif 'open youtube' in query:  # here  webbrowser.open use 'default browser'
            webbrowser.open('youtube.com')  # how ever it's not functional like selenium webscraping

        elif 'open google' in query:
            webbrowser.open('google.com')

        elif 'open stack overflow' in query:
            webbrowser.open('stackoverflow.com')

        
        # play music
        elif 'play music' in query:
            play_music()


        # ask time
        elif 'what\'s the time' in query:
            tell_time()


        # open any application here(vscode)
        elif 'open vs code' in query or 'open v s code' in query or 'open visual studio code' in query:
            start_vscode()

        
        # send email
        elif 'send email' in query:
            try:
                speak('What should i send?')
                content = take_command()
                to = 'rangersfoji1@gmail.com'
                
                send_email(to,content)
                speak('email has been sent successfully!!')
            except:
                speak('there is some server issue, please try again later!!')