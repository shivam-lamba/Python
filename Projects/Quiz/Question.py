# -*- coding: utf-8 -*-
"""
Created on Wed Sep 11 01:18:58 2019

@author: slamb
"""

import tkinter as tk
from Component1 import AddQuestion

class MyQuestion:
    def __init__(self):
        self.root=tk.Tk()
        
        self.Question=tk.StringVar()
        self.Answer=tk.StringVar()
        
        self.root.geometry("300x200")
        self.root.title("Add Questions")
        
        self.lbl1=tk.Label(self.root,text="Question")
        self.lbl1.place(x=10,y=20)
        
        self.ent1=tk.Entry(self.root,textvariable=self.Question)
        self.ent1.place(x=80,y=20)
        
        self.lbl2=tk.Label(self.root,text="Answer")
        self.lbl2.place(x=10,y=80)
        
        self.ent1=tk.Entry(self.root,textvariable=self.Answer)
        self.ent1.place(x=80,y=80)
        
        self.btn1=tk.Button(self.root,text="Save",command=self.AddClicked)
        self.btn1.place(x=80,y=150)
        
        self.btn2=tk.Button(self.root,text="Close",command=self.root.destroy)
        self.btn2.place(x=160,y=150)
        
        self.root.mainloop()
        
    def AddClicked(self):
        pass
        
obj=MyQuestion()

