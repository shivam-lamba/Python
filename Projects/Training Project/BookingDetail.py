# -*- coding: utf-8 -*-
"""
Created on Tue Jul 23 18:21:25 2019

@author: slamb
"""

import tkinter as tk
from tkinter.ttk import Treeview
from DataLayer import DalBooking

class BookingDetails:
    def __init__(self,bid):
        self.root=tk.Toplevel()
        self.root.grab_set()
        
        self.BookingId=bid
        
        self.root.geometry("830x300")
        self.root.title("Booking")
        
        self.tree1=Treeview(self.root)
        self.tree1.place(x=10,y=40)
        
        self.tree1['columns']=["c1","c2","c3"]
        self.tree1.heading("c1",text="Passenger Name")
        self.tree1.heading("c2",text="Gender")
        self.tree1.heading("c3",text="Age")
        
        objDal=DalBooking()
        
        AllPassengers=objDal.GetPassenger(self.BookingId)
        
        i=0
        for pas in AllPassengers:
            self.tree1.insert("",i,text=pas.PassengerId,values=(pas.PName,pas.Gender,pas.Age))
            i=i+1
            