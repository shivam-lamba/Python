# -*- coding: utf-8 -*-
"""
Created on Wed Sep 11 18:10:41 2019

@author: slamb
"""

import pyodbc
from abc import ABC
from Component2 import Hostel

class DBOperation(ABC):
    def __init__(self):
        self.con=pyodbc.connect("Driver={Sql Server};Server=LAPTOP-4ACUBH1G\SQLEXPRESS;Database=HostelDb;Uid=sa;Pwd=mydatabase")
        
class DalHostel(DBOperation):
    def __init__(self):
        DBOperation.__init__(self)
        
    def __del__(self):
        self.con.close()
        self.con=None
        
    def AddHostel(self,hos):
        cur=self.con.cursor()
        query="insert into Hostel values(?,?)"
        row=(hos.Hostel,hos.Block)
        cur.execute(query,row)
        self.con.commit()
        