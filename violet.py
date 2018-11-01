#!/usr/bin/env python3


import speech_recognition as sr
from time import ctime
import time
import os
import random
from gtts import gTTS
import webbrowser

def speak(audioString):
    print(audioString)
    tts = gTTS(text=audioString, lang='en-us')
    tts.save("audio.mp3")
    os.system("mpg321 audio.mp3")

def recordAudio():
    # Record Audio
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Say something!")
        audio = r.listen(source)
    
    # Speech recognition using Google Speech Recognition
    data = ""
    try:
        # Uses the default API key
        # To use another API key: `r.recognize_google(audio, key="GOOGLE_SPEECH_RECOGNITION_API_KEY")`
        data = r.recognize_google(audio)
        print("You said: " + data)
    except sr.UnknownValueError:
        print("I'm sorry but I didn't catch that")
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))
    
    return data

def violet(data):
    
    if "violet you up" in data:
        speak(random.choice(["For you Boss, always"]))
    
    if "hi" in data:
        speak(random.choice(["Hi boss", "Hello boss", "Hey there, boss"]))
    
    if "what is violet" in data:
        speak("Yours truly.")
    
    if "are you a robot" in data:
        speak("I don't mean to brag but I got an A minus on the Turing Test")
    
    if "are you a man or a woman" in data:
        speak("I don't think that really matters")
    
    if "do you smoke" in data:
        speak("That's not healthy, I wouldn't recommend it.")
    
    if "violet are you up" in data:
        speak("For you Boss, always.")
    
    if "how do I look" in data:
        speak("On a scale of 1 to 10. I'll bet you're a 78.")
    
    if "beatbox for me" in data:
        speak("Ok listen to this. Boots n cats Boots n cats Boots n cats Boots n cats Boots n cats Boots n cats Boots n cats Boots n cats Boots n cats Boots n cats Boots n cats Boots n cats. Is that good enough?")
    if "Beatbox for me" in data:
        speak("Ok listen to this. Boots n cats Boots n cats Boots n cats Boots n cats Boots n cats Boots n cats Boots n cats Boots n cats Boots n cats Boots n cats Boots n cats Boots n cats. Is that good enough?")
    
    if "when is the world going to end" in data:
        speak("I don't know, but I wouldn't worry about it. There are other perfectly good universes")
    
    if "what is your best pick up line" in data:
        speak("Are you bluetooh? Cause I'm feeling a connection.")
    
    if "testing 1, 2, 3" in data:
        speak("I'm completely operational and all my circuits are functioning perfectly.")
    
    if "testing 123" in data:
        speak("I'm completely operational and all my circuits are functioning perfectly.")
    
    if "how do I look violet" in data:
        speak("Particularly Ravishing!")
    
    if "what time is it" in data:
        speak(ctime())
    
    if "where is" in data:
        data = data.split(" ")
        location = data[2]
        speak("Hold on boss, I will show you where " + location + " is.")
        webbrowser.open("https://www.google.nl/maps/place/" + location + "/&amp;")

    if "open my email" in data:
        speak("Opening your email")
        webbrowser.open("https://www.gmail.com")

    if "open my university portal" in data:
        speak("Opening your login portal")
        webbrowser.open("https://vtopbeta.vit.ac.in/vtop/")

    if "open my University portal" in data:
        speak("Opening your login portal")
        webbrowser.open("https://vtopbeta.vit.ac.in/vtop/")

    if "show me the latest news" in data:
        speak("showing news")
        webbrowser.open("https://www.wsj.com/india")
            
            
    if "current weather of vellore":
       speak("Hold on boss, I will show you weather of vellore")
       webbrowser.open(" https://www.accuweather.com/en/in/vellore/190795/weather-forecast/190795")

  

    if "violet i love u" in data:
        speak("Fuck u i don't")

    if "violet i love you" in data:
        speak("Fuck u i don't")

    if "brilliant" in data:
        speak("Good to hear that")
    
    if "hey violet" in data:
        speak("Yes Boss?")
    
    if "violet" in data:
        speak("Yes Boss?")
    
    if "yeah" in data:
        speak("Cool Cool Cool Cool Cool Cool ")
    
    if "i am good" in data:
        speak("Good to hear that")
    
    if "I'm good" in data:
        speak("Glad to hear that")
    
    if "i'm good" in data:
        speak("Glad to hear that")



# initialization
time.sleep(1)
speak(random.choice(["Hey Boss, how are we doing today?", "Hi Boss, at your service"]))

while 1:
    data = recordAudio()
    violet(data)
