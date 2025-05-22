# -*- coding: utf-8 -*-
"""
Created on Fri Jul 12 23:37:25 2019

@author: slamb
"""

class Location:
    def __init__(self):
        self.LocationId=0
        self.LocationName=""
        self.Distance=0
        
class Vehicle:
    def __init__(self): 
        self.VehicleId=0
        self.VehicleNo=0
        self.VType=""
        self.Capacity=0
        
class Hotel:
    def __init__(self):
        self.HotelId=0
        self.HotelName=""
        self.Address=""
        self.City=""
        self.ContactNo=""
        self.HType=""
        
class Package:
    def __init__(self):
        self.PackageId=0
        self.LocationId=0
        self.LocationName=""
        self.Nod=0
        self.Charges=0
        
class Feature:
    def __init__(self):
        self.FeatureId=0
        self.Feature=""
        self.PackageId=0
        
class Booking:
    def __init__(self):
        self.BookingId=0
        self.BookingDate=0
        self.BookedDate=0
        self.PackageId=0
        self.HotelId=0
        self.VehicleId=0
        self.Passengers=[]
        self.LocationName=""
        self.HotelName=""
        self.VehicleNo=""
        self.Charges=0
        
class Passenger:
    def __init__(self):
        self.PassengerId=0
        self.PName=""
        self.Gender=""
        self.Age=0
        self.BookingId=0
        
class LocationWiseBooking:
    def __init__(self):
        self.LocationId=0
        self.PackageId=0
        self.LocationName=""
        self.BookingId=0
        self.NoB=0
        
class Collection:
    def __init__(self):
        self.Month=""
        self.Charges=0