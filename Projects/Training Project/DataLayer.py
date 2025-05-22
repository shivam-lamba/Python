# -*- coding: utf-8 -*-
"""
Created on Sat Jul 13 00:35:13 2019

@author: slamb
"""

import pyodbc
from abc import ABC
from Component import Location
from Component import Vehicle
from Component import Hotel
from Component import Package
from Component import Feature
from Component import Booking
from Component import Passenger
from Component import LocationWiseBooking
from Component import Collection

class DBOperation(ABC):
    def __init__(self):
        self.con=pyodbc.connect("Driver={Sql Server};Server=LAPTOP-LUENULQT\SQLEXPRESS;Database=ProjectDb;Uid=sa;Pwd=mydatabase")
        
class DalLocation(DBOperation):
    def __init__(self):
        DBOperation.__init__(self)
        
    def __del__(self):
        self.con.close()
        self.con=None
        
    def AddLocation(self,loc):
        try:
            cur=self.con.cursor()
            query="insert into Locations values(?,?)"
            row=(loc.LocationName,loc.Distance)
            cur.execute(query,row)
            self.con.commit()
            return True
        except:
            return False
        
    def GetLocation(self):
        cur=self.con.cursor()
        cur.execute("select * from Locations")
        records=cur.fetchall()
        
        AllLocations=[]
        
        for record in records:
            loc=Location()
            loc.LocationId=record[0]
            loc.LocationName=record[1]
            loc.Distance=record[2]
            
            AllLocations.append(loc)
            
        return AllLocations
    
    def DeleteLocation(self,locationid):
        cur=self.con.cursor()
        query="Delete from Locations where LocationId=?"
        row=(locationid)
        cur.execute(query,row)
        self.con.commit()
        
class DalVehicle(DBOperation):
    def __init__(self):
        DBOperation.__init__(self)
        
    def __del__(self):
        self.con.close()
        self.con=None
        
    def AddVehicle(self,veh):
        try:
            cur=self.con.cursor()
            query="insert into Vehicles values(?,?,?)"
            row=(veh.VehicleNo,veh.VType,veh.Capacity)
            cur.execute(query,row)
            self.con.commit()
            return True
        except:
            False
            
    def GetVehicle(self):
        cur=self.con.cursor()
        cur.execute("select * from Vehicles")
        records=cur.fetchall()
        
        AllVehicles=[]
        
        for record in records:
            veh=Vehicle()
            veh.VehicleId=record[0]
            veh.VehicleNo=record[1]
            veh.VType=record[2]
            veh.Capacity=record[3]
            
            AllVehicles.append(veh)
            
        return AllVehicles
    
    def DeleteVehicle(self,vehicleid):
        cur=self.con.cursor()
        query="delete from Vehicles where VehicleId=?"
        row=(vehicleid)
        cur.execute(query,row)
        self.con.commit()
        
class DalHotel(DBOperation):
    def __init__(self):
        DBOperation.__init__(self)
        
    def __del__(self):
        self.con.close()
        self.con=None
        
    def AddHotel(self,hot):
        try:
            cur=self.con.cursor()
            query="insert into Hotels values(?,?,?,?,?)"
            row=(hot.HotelName,hot.Address,hot.City,hot.ContactNo,hot.HType)
            cur.execute(query,row)
            self.con.commit()
            return True
        except:
            return False
        
    def GetHotel(self):
        cur=self.con.cursor()
        cur.execute("select * from Hotels")
        records=cur.fetchall()
        
        AllHotels=[]
        
        for record in records:
            hot=Hotel()
            hot.HotelId=record[0]
            hot.HotelName=record[1]
            hot.Address=record[2]
            hot.City=record[3]
            hot.ContactNo=record[4]
            hot.HType=record[5]
            
            AllHotels.append(hot)
        
        return AllHotels
    
    def DeleteHotel(self,hotelid):
        cur=self.con.cursor()
        query="delete from Hotels where HotelId=?"
        row=(hotelid)
        cur.execute(query,row)
        self.con.commit()
        
class DalPackage(DBOperation):
    def __init__(self):
        DBOperation.__init__(self)
        
    def __del__(self):
        self.con.close()
        self.con=None
        
    def AddPackage(self,pac):
        try:
            cur=self.con.cursor()
            query="insert into Packages values(?,?,?)"
            row=(pac.LocationId,pac.Nod,pac.Charges)
            cur.execute(query,row)
            self.con.commit()
            return True
        except:
            return False
        
    def GetPackage(self):
        cur=self.con.cursor()
        cur.execute("select p.PackageId, l.LocationName, p.Nod, p.Charges from Packages as [p], Locations as[l] where p.LocationId=l.LocationId")
        records=cur.fetchall()
        
        AllPackages=[]
        
        for record in records:
            pac=Package()
            pac.PackageId=record[0]
            pac.LocationName=record[1]
            pac.Nod=record[2]
            pac.Charges=record[3]
            
            AllPackages.append(pac)
            
        return AllPackages
    
    def DeletePackage(self,packageid):
        cur=self.con.cursor()
        cur.execute("delete from Packages where PackageId=?",(packageid))
        self.con.commit()
        
    def AddFeature(self,feat):
        cur=self.con.cursor()
        cur.execute("insert into Features values(?,?)",(feat.Feature,feat.PackageId))
        self.con.commit()
        
    def GetFeature(self,packageid):
        cur=self.con.cursor()
        cur.execute("select * from Features where PackageId=?",(packageid))
        records=cur.fetchall()
        
        AllFeatures=[]
        
        for record in records:
            feat=Feature()
            feat.FeatureId=record[0]
            feat.Feature=record[1]
            
            AllFeatures.append(feat)
            
        return AllFeatures
    
    def DeleteFeature(self,featureid):
        cur=self.con.cursor()
        cur.execute("delete from Features where FeatureId=?",(featureid))
        self.con.commit()
        
class DalBooking(DBOperation):
    def __init__(self):
        DBOperation.__init__(self)
        
    def AddBooking(self,booking):
        cur=self.con.cursor()
        query="insert into Bookings values(GETDATE(),?,?,?,?,?)"
        row=(booking.BookedDate,booking.PackageId,booking.HotelId,booking.VehicleId,booking.Charges)
        cur.execute(query,row)
        self.con.commit()
        
        cur.execute("select Top 1 * from Bookings order by BookingId desc")
        record=cur.fetchone()
        
        bookingid=int(record[0])
        
        query="insert into Passengers values(?,?,?,?)"
        
        for passenger in booking.Passengers:
            row=(passenger.PName,passenger.Gender,passenger.Age,bookingid)
            cur.execute(query,row)
            
        self.con.commit()
        
    def GetBooking(self,year,month,locationid):
        cur=self.con.cursor()
        cur.execute("select b.BookingId, b.BookingDate, b.BookedDate, l.LocationName, h.HotelName, v.VehicleNo from Bookings as [b], Locations as [l], Hotels as [h], Vehicles as [v], Packages as [pac] where b.HotelId=h.HotelId and b.PackageId=pac.PackageId and b.VehicleId=v.VehicleId and pac.LocationId=l.LocationId and DATEPART(Year,B.BookedDate)=? and DATEPART(Month,b.BookedDate)=? and l.LocationId=?",(year,month,locationid))
        records=cur.fetchall()

        AllBookings=[]
        
        for record in records:
            book=Booking()
            book.BookingId=record[0]
            book.BookingDate=record[1]
            book.BookedDate=record[2]
            book.LocationName=record[3]
            book.HotelName=record[4]
            book.VehicleNo=record[5]
            
            AllBookings.append(book)
            
        return AllBookings
        
    def GetPassenger(self,bookingid):
        cur=self.con.cursor()
        cur.execute("select * from Passengers where BookingId=?",(bookingid))
        records=cur.fetchall()
        
        AllPassengers=[]
        
        for record in records:
            pas=Passenger()
            pas.PassengerId=record[0]
            pas.PName=record[1]
            pas.Gender=record[2]
            pas.Age=record[3]
            pas.BookingId=record[4]
            
            AllPassengers.append(pas)
            
        return AllPassengers
    
    def GetLocationWiseBooking(self):
        cur=self.con.cursor()
        cur.execute("select (select LocationName from Locations, Packages where Locations.LocationId=Packages.LocationId and Packages.PackageId=B.PackageId) as [Location], COUNT (*) as [NoB] from Bookings as [B] group by PackageId")
        records=cur.fetchall()
        
        AllLocationBookings=[]
        
        for record in records:
            book=LocationWiseBooking()
            book.LocationName=record[0]
            book.NoB=record[1]
            
            AllLocationBookings.append(book)
            
        return AllLocationBookings
    
    def GetCollection(self):
        cur=self.con.cursor()
        cur.execute("select DATENAME(Month,BookedDate) as [Month], SUM(Charges) as [TotalCharges] from Bookings group by DATENAME(Month,BookedDate)")
        records=cur.fetchall()
        
        AllCollections=[]
        
        for record in records:
            col=Collection()
            col.Month=record[0]
            col.Charges=record[1]
            
            AllCollections.append(col)
            
        return AllCollections
    
    def TopDestination(self):
        cur=self.con.cursor()
        cur.execute("select LocationName from Locations where LocationId IN(select LocationId from Packages where PackageId IN(select top 4 PackageId from Bookings group by PackageId order by COUNT (*) desc))")
        records=cur.fetchall()
        
        AllTopDestinations=[]
        
        for record in records:
            loc=Location()
            loc.LocationName=record[0]
            
            AllTopDestinations.append(loc)
            
        return AllTopDestinations
    
    def TopHotel(self):
        cur=self.con.cursor()
        cur.execute("select HotelName from Hotels where HotelId IN(select top 4 HotelId from Bookings group by HotelId order by COUNT(*) desc)")
        records=cur.fetchall()
        
        AllTopHotels=[]
        
        for record in records:
            hot=Hotel()
            hot.HotelName=record[0]
            
            AllTopHotels.append(hot)
            
        return AllTopHotels
    
            
        
            
        
        

            
            