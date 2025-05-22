# -*- coding: utf-8 -*-
"""
Created on Wed Sep 11 01:44:12 2019

@author: slamb
"""

import pyodbc
from abc import ABC

class DBOperation(ABC):
    def __init__(self):
        self.con=pyodbc.connect("Driver={Sql Server},Server=")