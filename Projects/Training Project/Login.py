# -*- coding: utf-8 -*-
"""
Created on Tue Jul 23 21:21:38 2019

@author: slamb
"""

import tkinter as tk
from tkinter import messagebox
from Gateway import Menu

class Login:
    def __init__(self):
        self.root=tk.Tk()
        
        self.root.geometry("300x300")
        self.root.title("Login")
        
        self.Uid=tk.StringVar()
        self.Pwd=tk.StringVar()
        
        self.lbl1=tk.Label(self.root,text="CRUISER TOUR AND TRAVELS",font=("bold"))
        self.lbl1.place(x=30,y=10)
        
        self.lbl2=tk.Label(self.root,text="User Id")
        self.lbl2.place(x=20,y=80)
        
        self.ent1=tk.Entry(self.root,textvariable=self.Uid)
        self.ent1.place(x=120,y=80)
        
        self.lbl3=tk.Label(self.root,text="Password")
        self.lbl3.place(x=20,y=120)
        
        self.ent2=tk.Entry(self.root,textvariable=self.Pwd,show="*")
        self.ent2.place(x=120,y=120)
        
        self.btn1=tk.Button(self.root,text="Login",command=self.LoginClicked)
        self.btn1.place(x=120,y=180)
        
        self.btn2=tk.Button(self.root,text="Exit",command=self.root.destroy)
        self.btn2.place(x=200,y=180)
        
        self.btn3=tk.Button(self.root,text="Show",command=self.ShowClicked)
        self.btn3.place(x=250,y=120)
        
        self.load=tk.PhotoImage(file=r"login.png")
        self.load=self.load.zoom(8)
        self.load=self.load.subsample(20)
        
        self.lbl4=tk.Label(self.root,image=self.load)
        self.lbl4.place(x=1,y=160)
        
        self.root.mainloop()
        
    def LoginClicked(self):
        if self.Uid.get()=="admin" and self.Pwd.get()=="123":
            obj=Menu()
        else:
            messagebox.showinfo("Login","Access Denied !\nIncorrect UserName or Password..!")
            
    def ShowClicked(self):
        self.ent2.config(show="")
        
obj=Login()