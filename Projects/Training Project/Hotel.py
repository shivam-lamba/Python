# -*- coding: utf-8 -*-
"""
Created on Tue Jul 16 00:52:55 2019

@author: slamb
"""

import tkinter as tk
from Component import Hotel
from DataLayer import DalHotel
from tkinter import messagebox
from tkinter.ttk import Treeview

class MyHotel:
    def __init__(self):
        self.root=tk.Toplevel()
        self.root.grab_set()
        
        self.HotelName=tk.StringVar()
        self.Address=tk.StringVar()
        self.City=tk.StringVar()
        self.ContactNo=tk.StringVar()
        self.HotelType=tk.StringVar()
        
        self.root.geometry("350x300")
        self.root.title("Hotel")
        
        self.lbl1=tk.Label(self.root,text="Hotel Name")
        self.lbl1.place(x=10,y=40)
        
        self.ent1=tk.Entry(self.root,textvariable=self.HotelName)
        self.ent1.place(x=100,y=40)
        
        self.lbl2=tk.Label(self.root,text="Address")
        self.lbl2.place(x=10,y=80)
        
        self.ent2=tk.Entry(self.root,text=self.Address)
        self.ent2.place(x=100,y=80)
        
        self.lbl3=tk.Label(self.root,text="City")
        self.lbl3.place(x=10,y=120)
        
        self.ent3=tk.Entry(self.root,textvariable=self.City)
        self.ent3.place(x=100,y=120)
        
        self.lbl4=tk.Label(self.root,text="Contact No ")
        self.lbl4.place(x=10,y=160)
        
        self.ent4=tk.Entry(self.root,textvariable=self.ContactNo)
        self.ent4.place(x=100,y=160)
        
        self.lbl5=tk.Label(self.root,text="Hotel Type")
        self.lbl5.place(x=10,y=200)
        
        self.ent5=tk.Entry(self.root,textvariable=self.HotelType)
        self.ent5.place(x=100,y=200)
        
        self.btn1=tk.Button(self.root,text="Add",command=self.AddClicked)
        self.btn1.place(x=100,y=250)
        
        self.btn2=tk.Button(self.root,text="Close",command=self.root.destroy)
        self.btn2.place(x=180,y=250)
        
    def AddClicked(self):
        hot=Hotel()
        hot.HotelName=self.HotelName.get()
        hot.Address=self.Address.get()
        hot.City=self.City.get()
        hot.ContactNo=self.ContactNo.get()
        hot.HType=self.HotelType.get()
        
        objDal=DalHotel()
        if objDal.AddHotel(hot)==True:
            messagebox.showinfo("Hotel","Hotel Added Successfully..!")
            
class HotelList:
    def __init__(self):
        self.root=tk.Toplevel()
        self.root.grab_set()
        
        self.root.title("Hotel")
        self.root.geometry("1230x300")
        
        self.tree1=Treeview(self.root)
        self.tree1.place(x=10,y=10)
        
        self.tree1['columns']=["c1","c2","c3","c4","c5"]
        self.tree1.heading("c1",text="Hotel Name")
        self.tree1.heading("c2",text="Address")
        self.tree1.heading("c3",text="City")
        self.tree1.heading("c4",text="Contact Number")
        self.tree1.heading("c5",text="Hotel Type")
        
        self.btn1=tk.Button(self.root,text="Delete Hotel",command=self.DeleteClicked,width=12)
        self.btn1.place(x=580,y=250)
        
        objDal=DalHotel()
        AllHotels=objDal.GetHotel()
        
        i=0
        for hot in AllHotels:
            self.tree1.insert("",i,text=hot.HotelId,values=(hot.HotelName,hot.Address,hot.City,hot.ContactNo,hot.HType))
            i=i+1
            
    def DeleteClicked(self):
        ret=messagebox.askyesno("Hotel","Do you want to delete selected Hotel ?")
        
        if ret==True:
            key=self.tree1.focus()
            hid=int(self.tree1.item(key,"text"))
            
            objDal=DalHotel()
            objDal.DeleteHotel(hid)
            
            self.tree1.delete(key)
        
        
        
        
        