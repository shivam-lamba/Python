# -*- coding: utf-8 -*-
"""
Created on Sun Aug  4 00:56:20 2019

@author: slamb
"""

import pyttsx3
import speech_recognition as sr
import datetime

class Daniel:
    def __init__(self):
        self.engine=pyttsx3.init('sapi5')
        self.voices=self.engine.getProperty('voices')
        #print(self.voices)
        self.engine.setProperty('voice',self.voices[0].id)
        
    def speak(self,audio):
        #print("Daniel :")
        self.engine.say(audio)
        print("Daniel :",audio)
        self.engine.runAndWait()
        
    def command(self):
        self.r=sr.Recognizer()
        
        with sr.Microphone() as source:
            print("Listening...")
            self.r.pause_threshold=1
            self.audio=self.r.listen(source,phrase_time_limit=5)
            
        try:
            self.query=self.r.recognize_google(self.audio)
            print("Boss :",self.query)
            
        except:
            print("Uninteligible text ..!\n Please say that again.")
        
    def intro(self):
        self.speak("All system have been started. Now I am online.")
        
    def wishme(self):
        self.hour=int(datetime.datetime.now().hour)
        if self.hour>=0 and self.hour<12:
            self.speak("Good Morning !")
            
        elif self.hour>=12 and self.hour<18:
            self.speak("Good Afternoon !")
            
        else:
            self.speak("Good Evening !")
            
        self.speak("I am Daniel Sir. How may I help you ?")
        
    def main(self):
        self.intro()
        self.wishme()
        self.query=self.command()
        
        if 'who created you' or 'who invented you' or 'boss' in self.query:
            self.speak("As according to the fact..I was designed by Mr. Shivam Lamba in Chandigarh")
            
        elif 'how are you' or 'whats up' or 'it going' or 'you up to' or 'you doing' in self.query:
            self.speak("I am doing great Sir. What about you ?")
            
        elif 'bye daniel' or 'see you' or 'quit' or 'exit' in self.query:
            self.speak("Okay Sir have good day. I'll see you next time. ")
        
obj=Daniel()
obj.main()
        
            
        
        
        