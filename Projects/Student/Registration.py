# -*- coding: utf-8 -*-
"""
Created on Tue Aug  6 16:19:05 2019

@author: slamb
"""

import tkinter as tk

class Registration:
    def __init__(self):
        self.root=tk.Tk()
        self.root.geometry("300x300")
        self.root.title("Student Registration")
        
        self.name=tk.StringVar()
        self.fname=tk.StringVar()
        self.gender=tk.StringVar()
        
        self.lbl1=tk.Label(self.root,text="Student Redistration",font=("bold"))
        self.lbl1.place(x=80,y=10)
        
        self.lbl2=tk.Label(self.root,text="Name")
        self.lbl2.place(x=10,y=40)
        
        self.ent1=tk.Entry(self.root,textvariable=self.name)
        self.ent1.place(x=110,y=40)
        
        self.lbl3=tk.Label(self.root,text="Father's Name")
        self.lbl3.place(x=10,y=80)
        
        self.ent2=tk.Entry(self.root,textvariable=self.fname)
        self.ent2.place(x=110,y=80)
        
        self.lbl4=tk.Label(self.root,text="Gender")
        self.lbl4.place(x=10,y=120)
        
        self.radio1=tk.Radiobutton(self.root,text="Male",variable=self.gender,value="Male")
        self.radio1.place(x=110,y=120)
        
        self.radio2=tk.Radiobutton(self.root,text="Female",variable=self.gender,value="Female")
        self.radio2.place(x=180,y=120)
        
        self.lbl5=tk.Label(self.root)
        
        self.root.mainloop()
        
obj=Registration()