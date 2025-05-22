# -*- coding: utf-8 -*-
"""
Created on Fri Jul 12 23:41:31 2019

@author: slamb
"""

import tkinter as tk
from Component import Location
from DataLayer import DalLocation
from tkinter import messagebox
from tkinter.ttk import Treeview

class MyLocation:
    def __init__(self):
        self.root=tk.Toplevel()
        
        self.LocationName=tk.StringVar()
        self.Distance=tk.StringVar()
        
        self.root.geometry("350x200")
        self.root.title("Location")
        
        self.lbl1=tk.Label(self.root,text="Loaction Name")
        self.lbl1.place(x=10,y=40)
        
        self.ent1=tk.Entry(self.root,textvariable=self.LocationName)
        self.ent1.place(x=100,y=40)
        
        self.msg1=tk.Label(self.root,fg="red")
        self.msg1.place(x=230,y=40)
        
        self.lbl2=tk.Label(self.root,text="Distance(km)")
        self.lbl2.place(x=10,y=80)
        
        self.ent1=tk.Entry(self.root,textvariable=self.Distance)
        self.ent1.place(x=100,y=80)
        
        self.msg2=tk.Label(self.root,fg="red")
        self.msg2.place(x=230,y=80)
        
        self.btn1=tk.Button(self.root,text="Add",command=self.AddClicked,width=5)
        self.btn1.place(x=100,y=130)
        
        self.btn2=tk.Button(self.root,text="Close",command=self.root.destroy,width=5)
        self.btn2.place(x=180,y=130)
        
        self.root.grab_set()
        
    def AddClicked(self):
        if self.ValidateInputs()==True:
            loc=Location()
            loc.LocationName=self.LocationName.get()
            loc.Distance=float(self.Distance.get())
            
            objDal=DalLocation()
            if objDal.AddLocation(loc)==True:
                messagebox.showinfo("Location","Location Added Successfully.")
            
            
    def ValidateInputs(self):
        res=True
        self.msg1.config(text="")
        self.msg2.config(text="")
        
        if len(self.LocationName.get())==0 or self.LocationName.get().isdigit()==True:
            self.msg1.config(text="Empty or Incorrect..!")
            res=False
            
        if self.Distance.get().isdigit()==False:
            self.msg2.config(text="Empty or Incorrect..!")
            res=False
            
        return res
    
class LocationList:
    def __init__(self):
        self.root=tk.Toplevel()
        
        self.root.geometry("625x300")
        self.root.title("Locations")
        
        self.tree1=Treeview(self.root)
        self.tree1.place(x=10,y=10)
        
        self.tree1['columns']=["c1","c2"]
        self.tree1.heading("c1",text="Location Name")
        self.tree1.heading("c2",text="Distance(km)")
        
        self.btn1=tk.Button(self.root,text="Delete Location",command=self.DeleteClicked,width=13)
        self.btn1.place(x=300,y=250)
        
        objDal=DalLocation()
        AllLocations=objDal.GetLocation()
        
        i=0
        for location in AllLocations:
            self.tree1.insert("",i,text=location.LocationId,values=(location.LocationName,location.Distance))
            i=i+1
            
        self.root.grab_set()
        
    def DeleteClicked(self):
        ret=messagebox.askyesno("Location","Do you want to delete selected Location ?")
        
        if ret==True:
            key=self.tree1.focus()
            lid=int(self.tree1.item(key,"text"))
            
            objDal=DalLocation()
            objDal.DeleteLocation(lid)
            self.tree1.delete(key)
        
       
        
        
    
            
        
        

        
