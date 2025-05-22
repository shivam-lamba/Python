# -*- coding: utf-8 -*-
"""
Created on Mon Jul 15 23:03:51 2019

@author: slamb
"""

import tkinter as tk
from Component import Vehicle
from tkinter.ttk import Combobox
from DataLayer import DalVehicle
from tkinter import messagebox
from tkinter.ttk import Treeview

class MyVehicle:
    def __init__(self):
        self.root=tk.Toplevel()
        self.root.grab_set()
        
        self.VehicleNo=tk.StringVar()
        self.VehicleType=tk.StringVar()
        self.Capacity=tk.StringVar()
        
        self.root.geometry("350x200")
        self.root.title("Vehicle")
        
        self.lbl1=tk.Label(self.root,text="VehicleNo")
        self.lbl1.place(x=10,y=40)
        
        self.ent1=tk.Entry(self.root,textvariable=self.VehicleNo)
        self.ent1.place(x=100,y=40)
        
        self.lbl2=tk.Label(self.root,text="Vehicle Type")
        self.lbl2.place(x=10,y=80)
        
        self.cmb1=Combobox(self.root,state="readonly",textvariable=self.VehicleType)
        self.cmb1.place(x=100,y=80)
        self.cmb1['values']=["Bus","Mini Bus","Car"]
        
        self.lbl3=tk.Label(self.root,text="Capacity")
        self.lbl3.place(x=10,y=120)
        
        self.ent2=tk.Entry(self.root,textvariable=self.Capacity)
        self.ent2.place(x=100,y=120)
        
        self.btn1=tk.Button(self.root,text="Add",command=self.AddClicked,width=5)
        self.btn1.place(x=100,y=170)
        
        self.btn2=tk.Button(self.root,text="Close",command=self.root.destroy)
        self.btn2.place(x=180,y=170)
        
    def AddClicked(self):
        veh=Vehicle()
        veh.VehicleNo=self.VehicleNo.get()
        veh.VType=self.VehicleType.get()
        veh.Capacity=self.Capacity.get()
        
        objDal=DalVehicle()
        if objDal.AddVehicle(veh)==True:
            messagebox.showinfo("Vehicle","Vehicle Added Successfully..!")
            
class VehicleList:
    def __init__(self):
        self.root=tk.Toplevel()
        self.root.grab_set()
        
        self.root.geometry("830x300")
        self.root.title("Vehicle")
        
        self.tree1=Treeview(self.root)
        self.tree1.place(x=10,y=10)
        
        self.tree1['columns']=["c1","c2","c3"]
        self.tree1.heading("c1",text="Vehicle Number")
        self.tree1.heading("c2",text="Vehicle Type")
        self.tree1.heading("c3",text="Capacity")
        
        self.btn1=tk.Button(self.root,text="Delete Vehicle",command=self.DeleteClicked,width=12)
        self.btn1.place(x=300,y=250)
        
        objDal=DalVehicle()
        AllVehicles=objDal.GetVehicle()
        
        i=0
        for veh in AllVehicles:
            self.tree1.insert("",i,text=veh.VehicleId,values=(veh.VehicleNo,veh.VType,veh.Capacity))
            i=i+1
            
    def DeleteClicked(self):
        ret=messagebox.askyesno("Vehicle","Do you want to delete selected Vehicle ?")
        
        if ret==True:
            key=self.tree1.focus()
            vid=int(self.tree1.item(key,"text"))
            
            objDal=DalVehicle()
            objDal.DeleteVehicle(vid)
            
            self.tree1.delete(key)
            
        
        
        
        
        
            
        

        
        
        