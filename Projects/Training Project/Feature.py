# -*- coding: utf-8 -*-
"""
Created on Thu Jul 18 20:06:47 2019

@author: slamb
"""

import tkinter as tk
from tkinter.ttk import Treeview
from Component import Feature
from DataLayer import DalPackage 
from tkinter import messagebox

class MyFeature:
    def __init__(self,pid):
        self.root=tk.Toplevel()
        self.root.grab_set()
        
        self.Feature=tk.StringVar()
        self.PackageId=pid
        
        self.root.geometry("440x350")
        self.root.title("Feature")
        
        self.lbl1=tk.Label(self.root,text="Feature")
        self.lbl1.place(x=10,y=40)
        
        self.ent1=tk.Entry(self.root,textvariable=self.Feature)
        self.ent1.place(x=100,y=40)
        
        self.btn1=tk.Button(self.root,text="Add",width=5,command=self.AddClicked)
        self.btn1.place(x=250,y=40)
        
        self.btn2=tk.Button(self.root,text="Delete Feature",command=self.DeleteClicked,width=12)
        self.btn2.place(x=10,y=310)
        
        self.btn2=tk.Button(self.root,text="Close",command=self.root.destroy)
        self.btn2.place(x=370,y=310)
        
        self.tree1=Treeview(self.root)
        self.tree1.place(x=10,y=80)
        
        self.tree1['columns']=["c1"]
        self.tree1.heading("c1",text="Feature")
        
        objDal=DalPackage()
        AllFeatures=objDal.GetFeature(self.PackageId)
        
        i=0
        for fet in AllFeatures:
            self.tree1.insert("",i,text=fet.FeatureId,values=(fet.Feature))
            i=i+1
            
        
    def AddClicked(self):
        feat=Feature()
        feat.Feature=self.Feature.get()
        feat.PackageId=self.PackageId
        
        objDal=DalPackage()
        if objDal.AddFeature(feat)==True:
            messagebox.showinfo("Feature","Feature Added Successfully..!")
            
    def DeleteClicked(self):
        ret=messagebox.askyesno("Feature","Do you want delete the selected Feature ?")
         
        if ret==True:
            key=self.tree1.focus()
            fid=int(self.tree1.item(key,"text"))
         
            objDal=DalPackage()
            objDal.DeleteFeature(fid)
             
            self.tree1.delete(key)
         
        
        
        
        

        
        