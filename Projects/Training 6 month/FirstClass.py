# -*- coding: utf-8 -*-
"""
Created on Fri Jan 15 15:24:12 2021

@author: slamb
"""

#Integer

x = 1
print("Type of integer : ",type(x))

#Float

y = 2.15
print("Type of float : ",type(y))

#Complex Numbers

cmp = 3 + 4j
print("Type of complex : ",type(cmp))

cmpfunc = complex(3,4)
print("Type 2 of integer : ",type(cmpfunc))

compstr = complex('3+4j')
print("Complex number : ",compstr)

#Boolean

boo = 0
print("Type of boolean : ",type(boo))

#List

ls = [1,2,3]
print("Type of list : ",type(ls))

#Tuple

tup = (1,2,3)
print("Type of tuple : ",type(tup))

tup1 = 1,2,3
print("Type 2 of tuple : ",type(tup1))

#Range

rg = range(5)
for i in rg:
    print(i)
print()    
rg1 = range(2,5)
for i in rg1:
    print(i)
    
print()
rg2 = range(2,10,2)
for i in rg2:
    print(i)

#String________

st = 'abcd'
print("Printing string : ",st)

st1 = "abcd"
print("Printing string :",st1)

st2 = '''abcd 
jhdds'''
print("Printing multi line string : ",st2)

st3 = """bhlfjodf kndn"""
print("Printing multi line string : ",st3)

#Dictionary________

dic = dict(A=1, B=2)
print("Dictionary : ",dic)

l1 = list("ABCD")

l2 = list("1234")

print("Dictionary with two lists : ",dict(zip(l1, l2)))

l = [("A", 1), ("B", 9), ("C", 5)]
dict(l)

dict1 = {"A" : 1, "B" :2}
print("Dictionary : ",dict1)

st = {1,1,2,5,8,6,55}
print("Set : ",st)

ls3 = [1,2,3,4,1]
print("Set : ",set(ls3))

print("Immutable Frozen Set : ",frozenset((0,2,8,6)))

ls4 = [1,2,3,4]
#print(hash(ls4))

#hash(dict(A=1,B=4))

#dict1 = {"A" : 1,"B": 2}

ls5 = [1,2,3]
#print(set(ls5))
#print(set(dict1))

print(bool(0))

print(bool(0.0))

print(bool(False))

print(bool(None))

print(bool())

print(bool([]))

print(bool(()))

print(bool({}))

print(bool(''))

print([0])

print(10 or 20)

print(0 or 10)

print(10 and 20)

print(0 and 10)

print()

ls6 = [2,4,6]

print(ls6 or [] )

a = 3

b = a

print(id(a))
print(id(b))

print( a is b)

print(7/2.3)

print(abs(3+4j))

print(float("10.26"))

a = 34 + 4j
print(a.conjugate())

print(divmod(10, 3))

print(pow(2,2))


#Checking Muttability of List 

ls7 = [1,2,3,4]
print(ls7)
print("Memmory Address for ls7 : ",id(ls7))

ls7[3] = 8
print(ls7)
print("Memory Address for ls7 after mutability",id(ls7))

#Checking Mutability of Tuples

tup5 = 1,5,6,7

print(tup5)
print(id(tup5))

tup5 = tup5 + (0,)
print(tup5)
print(id(tup5))
