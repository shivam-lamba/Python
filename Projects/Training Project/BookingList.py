# -*- coding: utf-8 -*-
"""
Created on Sun Jul 21 23:51:31 2019

@author: slamb
"""

import tkinter as tk
from tkinter.ttk import Treeview
from Component import Booking
from Component import Passenger
from tkinter.ttk import Combobox
from DataLayer import DalLocation
from DataLayer import DalBooking
from BookingDetail import BookingDetails

class MyBookingList:
    def __init__(self):
        self.root=tk.Toplevel()
        self.root.grab_set()
        
        self.Year=tk.StringVar()
        
        self.root.geometry("1240x400")
        self.root.title("BookingList")
        
        self.lbl1=tk.Label(self.root,text="Year")
        self.lbl1.place(x=10,y=40)
        
        self.cmb1=Combobox(self.root,textvariable=self.Year,state="readonly")
        self.cmb1.place(x=70,y=40)
        
        self.cmb1['values']=["2019","2020","2021","2022","2023","2024","2025"]
        
        self.lbl2=tk.Label(self.root,text="Months")
        self.lbl2.place(x=280,y=40)
        
        self.cmb2=Combobox(self.root,state="readonly")
        self.cmb2.place(x=350,y=40)
        
        self.cmb2['values']=["Jan","Feb","Mar","Apr","May","June","July","Aug","Sep","Oct","Nov","Dec"]
        
        self.lbl3=tk.Label(self.root,text="Location")
        self.lbl3.place(x=550,y=40)
        
        self.cmb3=Combobox(self.root,state="readonly")
        self.cmb3.place(x=620,y=40)
        
        objDal=DalLocation()
        self.AllLocation=objDal.GetLocation()
        
        list1=[]
        
        for loc in self.AllLocation:
            list1.append(loc.LocationName)
            
        self.cmb3['values']=list1
        
        self.btn1=tk.Button(self.root,text="Search",command=self.SearchClicked,width=5)
        self.btn1.place(x=800,y=40)
        
        self.tree1=Treeview(self.root)
        self.tree1.place(x=10,y=100)
        
        self.tree1['columns']=["c1","c2","c3","c4","c5"]
        self.tree1.heading("c1",text="Booking Date")
        self.tree1.heading("c2",text="Booked Date")
        self.tree1.heading("c3",text="Location Name")
        self.tree1.heading("c4",text="Hotel Name")
        self.tree1.heading("c5",text="Vehicle Number")
        
        self.btn2=tk.Button(self.root,text="Passenger",command=self.PassengerClicked)
        self.btn2.place(x=50,y=350)
        
    def SearchClicked(self):
        year=int(self.Year.get())
        month=self.cmb2.current()+1
        index=self.cmb3.current()
        
        lid=self.AllLocation[index].LocationId
        
        objDal=DalBooking()
        AllBookings=objDal.GetBooking(year,month,lid)
        
        i=0
        for book in AllBookings:
            self.tree1.insert("",i,text=book.BookingId,values=(book.BookingDate,book.BookedDate,book.LocationName,book.HotelName,book.VehicleNo))
            i=i+1
            
    def PassengerClicked(self):
        key=self.tree1.focus()
        bid=int(self.tree1.item(key,"text"))
        
        obj=BookingDetails(bid)
        