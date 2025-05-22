# -*- coding: utf-8 -*-
"""
Created on Sun Apr 12 04:51:27 2020

@author: slamb
"""

import re

text="mk12sh"

temp=re.compile("([a-zA-Z]+)([0-9]+)")
result=temp.match(text).groups()
print(str(result))