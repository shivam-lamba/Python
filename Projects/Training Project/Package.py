# -*- coding: utf-8 -*-
"""
Created on Wed Jul 17 00:58:34 2019

@author: slamb
"""

import tkinter as tk
from Component import Package
from tkinter.ttk import Combobox
from tkinter import messagebox
from tkinter.ttk import Treeview 
from DataLayer import DalLocation
from DataLayer import DalPackage
from Feature import MyFeature

class MyPackage:
    def __init__(self):
        self.root=tk.Toplevel()
        self.root.grab_set()
        
        self.Nod=tk.StringVar()
        self.Charges=tk.StringVar()
        
        self.root.geometry("350x250")
        self.root.title("Package")
        
        self.lbl1=tk.Label(self.root,text="Location")
        self.lbl1.place(x=10,y=40)
        
        self.cmb1=Combobox(self.root,state="readonly")
        self.cmb1.place(x=100,y=40)
        
        objDal=DalLocation()
        self.AllLocations=objDal.GetLocation()
        
        list1=[]
        
        for loc in self.AllLocations:
            list1.append(loc.LocationName)
            
        self.cmb1['values']=list1
            
        self.lbl2=tk.Label(self.root,text="Days")
        self.lbl2.place(x=10,y=80)
        
        self.cmb2=Combobox(self.root,textvariable=self.Nod)
        self.cmb2.place(x=100,y=80)
        
        self.cmb2['values']=["1","2","3","4","5","6","7"]
        
        self.lbl3=tk.Label(self.root,text="Charges")
        self.lbl3.place(x=10,y=120)
        
        self.ent1=tk.Entry(self.root,textvariable=self.Charges)
        self.ent1.place(x=100,y=120)
        
        self.btn1=tk.Button(self.root,text="Save",command=self.SaveClicked,width=5)
        self.btn1.place(x=100,y=170)
        
        self.btn2=tk.Button(self.root,text="Close",command=self.root.destroy,width=5)
        self.btn2.place(x=180,y=170)
        
    def SaveClicked(self):
        index=self.cmb1.current()
        LocationId=self.AllLocations[index].LocationId
        
        pac=Package()
        pac.LocationId=LocationId
        pac.Nod=self.Nod.get()
        pac.Charges=float(self.Charges.get())
        
        objDal=DalPackage()
        if objDal.AddPackage(pac)==True:
            messagebox.showinfo("Package","Package Added Successfully..!")
            
class PackageList:
    def __init__(self):
        self.root=tk.Toplevel()
        self.root.grab_set()
        
        self.root.geometry("840x300")
        self.root.title("Package")
        
        self.tree1=Treeview(self.root)
        self.tree1.place(x=10,y=10) 
        
        self.tree1['columns']=["c1","c2","c3"]
        self.tree1.heading("c1",text="Location Name")
        self.tree1.heading("c2",text="Days")
        self.tree1.heading("c3",text="Charges")
        
        self.btn1=tk.Button(self.root,text="Delete Package",command=self.DeleteClicked,width=12)
        self.btn1.place(x=10,y=250)
        
        self.btn2=tk.Button(self.root,text="Features",command=self.FeatureClicked)
        self.btn2.place(x=740,y=250)
        
        objDal=DalPackage()
        AllPackages=objDal.GetPackage()
        
        i=0
        for pac in AllPackages:
            self.tree1.insert("",i,text=pac.PackageId,values=(pac.LocationName,pac.Nod,pac.Charges))
            i=i+1
        
    def DeleteClicked(self):
        ret=messagebox.askyesno("Package","Do you want to delete selected Package ?")
        
        if ret==True:
            key=self.tree1.focus()
            pid=int(self.tree1.item(key,"text"))
            
            objDal=DalPackage()
            objDal.DeletePackage(pid)
            
            self.tree1.delete(key)
        
    def FeatureClicked(self):
        selectedkey=self.tree1.focus()
        packageid=int(self.tree1.item(selectedkey,"text"))
        
        obj=MyFeature(packageid)
        
        