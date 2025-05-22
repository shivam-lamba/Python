# -*- coding: utf-8 -*-
"""
Created on Wed Sep 11 17:50:15 2019

@author: slamb
"""

import tkinter as tk
from Component2 import Hostel
from DataLayer2 import DalHostel
from tkinter import messagebox

class MyHostel:
    def __init__(self):
        self.root=tk.Tk()
        
        self.Hostel=tk.StringVar()
        self.Block=tk.StringVar()
        
        self.root.geometry("300x200")
        self.root.title("Hostel")
        
        self.lbl1=tk.Label(self.root,text="Hostel")
        self.lbl1.place(x=20,y=20)
        
        self.ent1=tk.Entry(self.root,textvariable=self.Hostel)
        self.ent1.place(x=100,y=20)
        
        self.lbl2=tk.Label(self.root,text="Block")
        self.lbl2.place(x=20,y=80)
        
        self.ent2=tk.Entry(self.root,textvariable=self.Block)
        self.ent2.place(x=100,y=80)
        
        self.btn1=tk.Button(self.root,text="Save",command=self.AddClicked)
        self.btn1.place(x=100,y=150)
        
        self.btn2=tk.Button(self.root,text="Close",command=self.root.destroy)
        self.btn2.place(x=180,y=150)
        
        self.root.mainloop()
        
    def AddClicked(self):
        hos=Hostel()
        hos.Hostel=self.Hostel.get()
        hos.Block=self.Block.get()
        
        objDal=DalHostel()
        if objDal.AddHostel(hos)==True:
            messagebox.showinfo("Hostel","Hostel Added Successfully.")
            
class HostelList:
    def __init__(self):
        self.root=tk.Tk()
        
        self.root.geometry("300x300")
        self.root.title("Hostel")
        
        self.lbl1=tk.Label(self.root,text="Search")
        self.lbl1.place(x=20,y=20)
        
        
            
            
    
obj=MyHostel()