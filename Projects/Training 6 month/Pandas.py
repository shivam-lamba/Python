# -*- coding: utf-8 -*-
"""
Created on Tue Jan 19 13:14:46 2021

@author: slamb
"""

import numpy as np
import pandas as pd

s1 = pd.Series([1, 2, 3, 5, 8], index = list("ABCDE"), name = "Test")
print(s1)
print()

#Series made from Dictionary
s2 = pd.Series({"A" : 1, "B" : 2, "C" : 4})
print(s2)

#Scaler Value
s3 = pd.Series(5, index = list("ABCD"))
print(s3)

print(s1.to_numpy())

print(s1['A'])

print(s2.get('D', 0)) #Default value

s2["C"] = 3
print(s2)

print(s1 + s1)

s4 = pd.Series([1, 2, 9, 5, 6], index = list("ABCDE"))
s5 = pd.Series([5, 6, 8, 1, 3], index = list("EDCBA"))

print(s4 + s5)
