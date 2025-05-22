# -*- coding: utf-8 -*-
"""
Created on Thu Aug  1 15:49:48 2019

@author: slamb
"""

class Sum:
    def __init__(self):
        self.total=0
        self.no=0
        self.evensum=0
        self.oddsum=0
        self.list=[]
        self.diff=0
        
    def entry(self):
        self.total=int(input("Enter total Number of element in the list :"))
        
        for i in range(0,self.total):
            self.no=int(input("Enter the "+str(i+1)+" Number :"))
            self.list.append(self.no)
            
    def totalsum(self):
        for i in self.list:
            if i % 2==0:
                self.evensum=self.evensum+i
            else:
                self.oddsum=self.oddsum+i
        
        self.diff=self.evensum-self.oddsum
            
    def show(self):
        print("List :",self.list)
        print("Even sum :",self.evensum)
        print("Odd sum :",self.oddsum)
        print("Differene :",self.diff)
    
obj=Sum()
obj.entry()
obj.totalsum()
obj.show()
            