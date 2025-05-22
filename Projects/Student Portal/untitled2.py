# -*- coding: utf-8 -*-
"""
Created on Mon Apr 13 01:03:08 2020

@author: slamb
"""

import string 

outer = ['operating', 'alive', 'effective', 'rapid', 'progressive', 'working', 'mobile','enjoyable', 'pleasant', 'entertaining', 'amusing', 'lively', 'boisterous', 'convivial', 'merry', 'witty']


lowercase = string.ascii_lowercase
data = {lowercase[i]:[] for i in range(26)}
for word in outer:
    data[word[0]].append(word)
ft={}
for character in sorted(data.keys()):
    if len(data[character])!=0:
        ft={character:sorted(data[character])}
        print(ft)
        

