# -*- coding: utf-8 -*-
"""
Created on Sun Apr 12 02:45:19 2020

@author: slamb
"""

lt=[3,2,5,6]
mn=lt[0]
for i in lt:
    if mn > lt[i+1]:
        temp=mn
        mn=lt[i+1]
        lt[i+1]=temp
        