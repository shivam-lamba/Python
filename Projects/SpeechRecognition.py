# -*- coding: utf-8 -*-
"""
Created on Fri Jul 19 02:09:11 2019

@author: slamb
"""

import speech_recognition as sr

r=sr.Recognizer()

with sr.Microphone() as source:
    print("Speak anything :")
    audio=r.listen(source)
    
    try:
        text=r.recognize_google(audio)
        print("You Said :",text)
    except:
        print("Sorry could not recognise.")
            