# -*- coding: utf-8 -*-
"""
Created on Tue Jul 23 19:40:13 2019

@author: slamb
"""

import tkinter as tk
from tkinter.ttk import Treeview
from DataLayer import DalBooking

class MyCollection:
    def __init__(self):
        self.root=tk.Toplevel()
        self.root.grab_set()
        
        self.root.geometry("630x300")
        self.root.title("Collection")
        
        self.tree1=Treeview(self.root)
        self.tree1.place(x=10,y=40)
        
        self.tree1['columns']=["c1","c2"]
        self.tree1.heading("c1",text="Package")
        self.tree1.heading("c2",text="Total Charges")
        
        objDal=DalBooking()
        AllCollection=objDal.GetCollection()
        
        i=1
        for col in AllCollection:
            self.tree1.insert("",i,text=i,values=(col.Month,col.Charges))
            i=i+1