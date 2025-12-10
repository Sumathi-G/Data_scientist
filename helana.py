import speech_recognition as sr
import pyttsx3
import os
import datetime
import subprocess
import sys
import pywhatkit

engine = pyttsx3.init()
voices = engine.getProperty('voices')
for i, v in enumerate(voices):
    print(i, v.id, v.name, v.languages, v.gender)
engine.setProperty('voice', voices[0].id)

recognizer = sr.Recognizer()

def speak(text):
    engine.say(text)
    engine.runAndWait()

def open_software(software_name):
    software_name = software_name.lower().strip()
    if 'chrome' in software_name:
        speak('Opening Chrome...')
        program = r"c:\Users\Public\Desktop\Google Chrome.lnk"
        subprocess.Popen([program], shell= True)

    elif 'microsoft edge' in software_name:
        speak('Opening microsoft edge...')
        program = r"c:\Users\Public\Desktop\Microsoft Edge.lnk"
        subprocess.Popen([program], shell= True)

    elif 'play' in software_name:
        speak('Opening youtube')
        song = software_name.replace('play','').strip()
        pywhatkit.playonyt(song)

    elif 'notepad' in software_name:
        speak('Opening Noepad...')
        subprocess.Popen(['notepad.exe'])
    elif 'calculator' in software_name:
        speak('Opening Calculator...')
        subprocess.Popen(['calc.exe'])
    else:
        speak(f"I couldn't find the software{software_name}")

def close_software(software_name):
    name = name.lower().strip()
    if 'chrome' in software_name:
        speak('Closing Chrome...')
        os.system("taskkill /f /im chrome.exe")

    elif 'microsoft edge' in software_name :
        speak('Closing Microsoft Edge...')
        os.system("taskkill /f /im msedge.exe")
    
    elif 'notepad' in software_name:
        speak('closing Notepad...')
        os.system("taskkill /f /im notepad.exe")
    elif 'calculator' in software_name:
        speak('closing calculator...')
        os.system("taskkill /f /im calculator.exe")
    else:
        speak(f"I couldn't find any open software named {software_name}")  

def listen_for_wake_word():
    r = sr.Recognizer()
    with sr.Microphone() as src:
        r.adjust_for_ambient_noise(src, duration=0.5)
        audio = r.listen(src)
    try:
        text = r.recognize_google(audio).lower()`                           `
        if 'helana' in text:
            speak('hi dear, how can I help you?')
            return True
    except sr.UnknownValueError:
        print("Could not understand audio , please try again.")
    return False

def cmd():
    r = sr.Recognizer()
    with sr.Microphone() as src:
        r.adjust_for_ambient_noise(src, duration=0.5)
        audio = r.listen(src)
    try:
        text = r.recognize_google(audio).lower()
    except :
        speak("sorry, i didn't catch that.")
        return False
    
    print('heard:',text)
    if 'stop' in text:
        speak('Stoping .Goodbye!'); sys.exit()
    if 'open' in text:
        open_software(text.replace('open','').strip())
    elif 'close' in text :
        close_software(text.replace('close','').strip())
    elif 'time' in text :
        now = datetime.datetime.now().strftime('%I:%M %p')
        speak(now)
    elif 'who is god' in text:
        speak('ajitheyyy kadavuleyy')
    elif 'what is your name' in text:
        speak('i am helana')
    elif 'who is thalapathy' in text :
        speak('head of tvk')
    else :
        speak("command not recognized.")
    return False

if __name__ == "__main__": 
    while True :
        if listen_for_wake_word():
            while not cmd():
                pass 