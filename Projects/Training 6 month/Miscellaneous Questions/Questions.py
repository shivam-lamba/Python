# -*- coding: utf-8 -*-
"""
Created on Mon Jan 18 14:26:23 2021

@author: slamb
"""

"""#7
print([item % 2 != 0 for item in range(0,10)])

#5
lst = [1, 0, 9, 0, 8, 2]
lst1 = []
for i in lst:
    if i%2 :
        lst1.append(i)
print(sum(lst1))

#4
lst = [1,5,8]
if 0 in lst:
    print(lst)
else:
    print(False)
    
"""
#1
a = "AB"
b = '25'
print("".join(list(map(lambda x,y:x*int(y) ,a,b))))

#2
lst = [2, 4, 6, 8, 1]
lst1 = [2, 7, 9, 8, 3]

print("Common elements in lists : ",list(set(lst).intersection(lst1)))

#3
lst = ["AB", "GH", "RJ", "IM", "US", "MY"]
new_List = []
for ele in lst:
    if ele.startswith(tuple("AEIOU")):
        new_List.append(ele)
        
print("List starting with vowels : ",new_List)

"""Example of startwith function 
    it takes tuple as arguement"""
#print("Abhay".startswith(tuple("AEIOU")))
    
#List Comprehension

print("List elements starting ",[ele1 for ele1 in lst if ele1.startswith(tuple("AEIOU"))])

#4
lst = [1,5,0]
if 0 in lst:
    print(lst)
else:
    print(False)    
    
    
#5
lst = [1, 0, 9, 0, 8, 2]

even_List = []

for i in lst:
    if i % 2 == 0:
        even_List.append(i)

print(even_List)
x = (i for i in lst if i%2 ==0 )
print(type(x))
print(sum(i for i in lst if i%2 ==0 ))

#6
str1 = "ABIGHOMNU"
"""
new_List = []

for i in str1:
    if not in str1:
        new_List.append(i)
        
print(new_List)
        
print("".join(mem for mem in str1 if mem not in "AEIOU"))
"""
#7

print(list(range(1,10,2)))