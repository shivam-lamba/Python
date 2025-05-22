# -*- coding: utf-8 -*-
"""
Created on Sat Jul 13 02:18:14 2019

@author: slamb
"""

import tkinter as tk 
from Location import MyLocation
from Location import LocationList
from Vehicle import MyVehicle 
from Vehicle import VehicleList
from Hotel import MyHotel
from Hotel import HotelList
from Package import MyPackage
from Package import PackageList
from Booking import MyBooking
from BookingList import MyBookingList
from LocWiseBooking import MyLocationWiseBooking
from Collection import MyCollection
from DataLayer import DalBooking

class Menu:
    def __init__(self):
        self.root=tk.Toplevel()
        
        self.root.geometry("350x300")
        self.root.title("Cruiser Tour and Travels")
        
        self.lbl1=tk.Label(self.root,text="CRUISER TOUR AND TRAVEL",font="Verdana 16 bold",fg="#DEB887")
        self.lbl1.place(x=2,y=10)
        
        self.topstrip=tk.Menu(self.root)
        self.root.config(menu=self.topstrip)
        
        self.master=tk.Menu(self.topstrip,tearoff=0)
        self.topstrip.add_cascade(label="Masters",menu=self.master)
        
        self.location=tk.Menu(self.master,tearoff=0)
        self.master.add_cascade(label="Location",menu=self.location)
        
        self.location.add_command(label="Add Location",command=self.AddLocationClicked)
        self.location.add_command(label="View Location",command=self.ViewLocationClicked)
        
        self.Vehicle=tk.Menu(self.master,tearoff=0)
        self.master.add_cascade(label="Vehicle",menu=self.Vehicle)
        
        self.Vehicle.add_command(label="Add Vehicle",command=self.AddVehicleClicked)
        self.Vehicle.add_cascade(label="View Vehicle",command=self.ViewVehicleClicked)
        
        self.Hotel=tk.Menu(self.master,tearoff=0)
        self.master.add_cascade(label="Hotel",menu=self.Hotel)
        
        self.Hotel.add_command(label="Add Hotel",command=self.AddHotelClicked)
        self.Hotel.add_cascade(label="View Hotel",command=self.ViewHotelClicked)
        
        self.Package=tk.Menu(self.topstrip,tearoff=0)
        self.topstrip.add_cascade(label="Package",menu=self.Package)
        
        self.Package.add_command(label="Add Package",command=self.AddPackageClicked)
        self.Package.add_command(label="View Package",command=self.ViewPackageClicked)
        
        self.booking=tk.Menu(self.topstrip,tearoff=0)
        self.topstrip.add_cascade(label="Booking",menu=self.booking)
        
        self.booking.add_command(label="Add Booking",command=self.AddBookingClicked)
        self.booking.add_command(label="View Booking",command=self.ViewBookingClicked)
        
        self.reporting=tk.Menu(self.topstrip,tearoff=0)
        self.topstrip.add_cascade(label="Reporting",menu=self.reporting)
        
        self.reporting.add_command(label="Number of Bookings",command=self.ViewLocationBookingClicked)
        self.reporting.add_command(label="Collection",command=self.CollectionClicked)
        
        self.lbl2=tk.Label(self.root,text="Top Attractions:",font=(46))
        self.lbl2.place(x=10,y=120)
        
        objDal=DalBooking()
        AllTopDestination=objDal.TopDestination()
        
        yCor=150
        for loc in AllTopDestination:
            self.lbl=tk.Label(self.root,text=loc.LocationName)
            self.lbl.place(x=15,y=yCor)
            yCor+=20
            
        self.lbl3=tk.Label(self.root,text="Famous Hotels:",font=(46))
        self.lbl3.place(x=220,y=120)
        
        objDal=DalBooking()
        AllTopHotels=objDal.TopHotel()
        
        yCor=150
        for hot in AllTopHotels:
            self.lbl=tk.Label(self.root,text=hot.HotelName)
            self.lbl.place(x=225,y=yCor)
            yCor+=20
            
        self.lbl4=tk.Label(self.root,text="*The contents contained in this application are copyright protected.")
        self.lbl4.place(x=1,y=260)
        
        self.load1=tk.PhotoImage(file=r"images.png")
        self.load1=self.load1.zoom(8)
        self.load1=self.load1.subsample(35)
        
        self.lbl5=tk.Label(self.root,image=self.load1)
        self.lbl5.place(x=2,y=50)
        
        self.load2=tk.PhotoImage(file=r"images (1).png",height=500)
        self.load2=self.load2.zoom(8)
        self.load2=self.load2.subsample(65)
        
        self.lbl6=tk.Label(self.root,image=self.load2)
        self.lbl6.place(x=140,y=50)
        
        self.load3=tk.PhotoImage(file=r"images (2).png")
        self.load3=self.load3.zoom(8)
        self.load3=self.load3.subsample(30)
        
        self.lbl7=tk.Label(self.root,image=self.load3)
        self.lbl7.place(x=280,y=50)
        
        self.root.grab_set()
        
    def AddLocationClicked(self):
        obj=MyLocation()
            
    def ViewLocationClicked(self):
        obj=LocationList()
            
    def AddVehicleClicked(self):
        obj=MyVehicle()
        
    def ViewVehicleClicked(self):
        obj=VehicleList()
        
    def AddHotelClicked(self):
        obj=MyHotel()
        
    def ViewHotelClicked(self):
        obj=HotelList()
        
    def AddPackageClicked(self):
        obj=MyPackage()
        
    def ViewPackageClicked(self):
        obj=PackageList()
        
    def AddBookingClicked(self):
        obj=MyBooking()
        
    def ViewBookingClicked(self):
        obj=MyBookingList()
        
    def ViewLocationBookingClicked(self):
        obj=MyLocationWiseBooking()
    
    def CollectionClicked(self):
        obj=MyCollection()
        

            

            
        
        