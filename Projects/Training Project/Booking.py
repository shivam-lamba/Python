# -*- coding: utf-8 -*-
"""
Created on Thu Jul 18 23:46:04 2019

@author: slamb
"""

import tkinter as tk
from tkinter.ttk import Treeview
from Component import Booking
from Component import Passenger
from tkinter.ttk import Combobox
from DataLayer import DalPackage
from DataLayer import DalHotel
from DataLayer import DalVehicle
from DataLayer import DalBooking
from tkinter import messagebox

class MyBooking:
    def __init__(self):
        self.root=tk.Toplevel()
        
        self.BookedDate=tk.StringVar()
        self.PassengerName=tk.StringVar()
        self.Gender=tk.StringVar()
        self.Age=tk.IntVar()
        
        
        self.root.geometry("820x450")
        self.root.title("Booking")
        
        self.lbl1=tk.Label(self.root,text="Booked Date")
        self.lbl1.place(x=10,y=40)
        
        self.ent1=tk.Entry(self.root,textvariable=self.BookedDate)
        self.ent1.place(x=100,y=40)
        
        self.lbl2=tk.Label(self.root,text="Package")
        self.lbl2.place(x=280,y=40)
        
        self.cmb1=Combobox(self.root,state="readonly")
        self.cmb1.place(x=350,y=40)
        
        objDal=DalPackage()
        self.AllPackages=objDal.GetPackage()
        
        list1=[]
        
        for pac in self.AllPackages:
            list1.append(pac.LocationName)
            
        self.cmb1['values']=list1
        
        self.lbl3=tk.Label(self.root,text="Hotel")
        self.lbl3.place(x=10,y=80)
        
        self.cmb2=Combobox(self.root,state="readonly")
        self.cmb2.place(x=100,y=80)
        
        objDal=DalHotel()
        self.AllHotels=objDal.GetHotel()
        
        list2=[]
        
        for hot in self.AllHotels:
            list2.append(hot.HotelName)
        
        self.cmb2['values']=list2
        
        self.lbl4=tk.Label(self.root,text="Vehicle")
        self.lbl4.place(x=280,y=80)
        
        self.cmb3=Combobox(self.root,state="readonly")
        self.cmb3.place(x=350,y=80)
        
        objDal=DalVehicle()
        self.AllVehicles=objDal.GetVehicle()
        
        list3=[]
        
        for veh in self.AllVehicles:
            list3.append(veh.VType)
            
        self.cmb3['values']=list3
        
        self.lbl5=tk.Label(self.root,text="Passenger Name")
        self.lbl5.place(x=10,y=120)
        
        self.ent2=tk.Entry(self.root,textvariable=self.PassengerName)
        self.ent2.place(x=110,y=120)
        
        self.lbl6=tk.Label(self.root,text="Gender")
        self.lbl6.place(x=250,y=120)
        
        self.radio1=tk.Radiobutton(self.root,text="Male",variable=self.Gender,value="Male")
        self.radio1.place(x=300,y=120)
        
        self.radio1=tk.Radiobutton(self.root,text="Female",variable=self.Gender,value="Female")
        self.radio1.place(x=350,y=120)
        
        self.lbl7=tk.Label(self.root,text="Age")
        self.lbl7.place(x=430,y=120)
        
        self.ent3=tk.Entry(self.root,textvariable=self.Age)
        self.ent3.place(x=460,y=120)
        
        self.btn1=tk.Button(self.root,text="Add",command=self.AddClicked,width=5)
        self.btn1.place(x=600,y=120)
        
        self.tree1=Treeview(self.root)
        self.tree1.place(x=10,y=160)
        
        self.tree1['columns']=["c1","c2","c3"]
        self.tree1.heading("c1",text="Passenger Name")
        self.tree1.heading("c2",text="Gender")
        self.tree1.heading("c3",text="Age")
        
        self.SerialNo=1
        
        self.booking=Booking()
        
        self.btn2=tk.Button(self.root,text="Delete",command=self.DeleteClicked,width=5)
        self.btn2.place(x=10,y=400)
        
        self.btn3=tk.Button(self.root,text="Book",command=self.BookClicked,width=5)
        self.btn3.place(x=650,y=400)
        
        self.btn4=tk.Button(self.root,text="Close",command=self.root.destroy,width=5)
        self.btn4.place(x=700,y=400)
        
        self.root.grab_set()

    def AddClicked(self):
        pas=Passenger()
        pas.PName=self.PassengerName.get()
        pas.Gender=self.Gender.get()
        pas.Age=self.Age.get()
        
        self.booking.Passengers.append(pas)
        
        self.tree1.insert("",self.SerialNo,text=self.SerialNo,values=(pas.PName,pas.Gender,pas.Age))
        self.SerialNo+=1
        
        self.PassengerName.set("")
        self.Age.set("")
        
    def DeleteClicked(self):
        pass
    
    def BookClicked(self):
        index1=self.cmb1.current()
        PackageId=self.AllPackages[index1].PackageId
        
        self.booking.BookedDate=self.BookedDate.get()
        self.booking.PackageId=PackageId
        
        index2=self.cmb2.current()
        HotelId=self.AllHotels[index2].HotelId
        self.booking.HotelId=HotelId
        
        index3=self.cmb3.current()
        VehicleId=self.AllVehicles[index3].VehicleId
        self.booking.VehicleId=VehicleId
        
        objDal=DalBooking()
        if objDal.AddBooking(self.booking)==True:
            messagebox.showinfo("Booking","Booking Confirmed..!")
            
        children=self.tree1.get_children()
        for child in children:
            self.tree1.delete(child)
            
        while len(self.booking.Passengers)>0:
            del self.booking.Passengers[0]
            
        
            
         
        
        
        
        
        
        
        