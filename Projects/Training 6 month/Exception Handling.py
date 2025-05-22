# -*- coding: utf-8 -*-
"""
Created on Tue Jan 19 12:22:49 2021

@author: slamb
"""

"""Exception Hnadling"""

import math

def divide(x,y):
    try:
        res = x/y
        sqrt = math.sqrt(x)
    except ZeroDivisionError:
        print("Divivsion by zero")
        
    except TypeError:
        print("Inappropriate type of parameters.")#When string as arguements are provided
        
    except ValueError:
        print("Square root of negative number.")
    else:
        print("division : ", res)
        print("square root : ", sqrt)
    finally:
        print("Final Clause.            ")
        
divide(-5,3)
divide("qwerty","asdfg")

ages = {"Jim" : 28, "Clay" : 26, "Stefan" : 56}
person  = input("Enter the name : ")

try:
    print(f'{person} is {ages[person]} years old.')
    
except KeyError:
    print("Name not in Dictionary")
    
except:
    print("Unexpected Error")
