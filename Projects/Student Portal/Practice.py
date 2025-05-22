# -*- coding: utf-8 -*-
"""
Created on Sun Apr 12 13:42:05 2020

@author: slamb
"""

class A:
    def show(self):
        print("Parent class.")
        
class B(A):
    def show(self):
        print("Child class.")
        
a=A()
a.show()
a=B()
a.show()