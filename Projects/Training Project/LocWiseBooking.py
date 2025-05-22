# -*- coding: utf-8 -*-
"""
Created on Tue Jul 23 19:14:26 2019

@author: slamb
"""

import tkinter as tk
from DataLayer import DalBooking
from tkinter.ttk import Treeview
from Component import LocationWiseBooking

class MyLocationWiseBooking:
    def __init__(self):
        self.root=tk.Toplevel()
        self.root.grab_set()
        
        self.root.geometry("640x300")
        self.root.title("Number of Bookings")
        
        self.tree1=Treeview(self.root)
        self.tree1.place(x=10,y=40)
        
        self.tree1['columns']=["c1","c2"]
        self.tree1.heading("c1",text="Location")
        self.tree1.heading("c2",text="Number of Bookings")
        
        objDal=DalBooking()
        AllLocationBookings=objDal.GetLocationWiseBooking()
        
        i=1
        for book in AllLocationBookings:
            self.tree1.insert("",i,text=i,values=(book.LocationName,book.NoB))
            i=i+1