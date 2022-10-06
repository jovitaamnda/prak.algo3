# -*- coding: utf-8 -*-
"""
Created on Thu Oct  6 20:08:22 2022

@author: jovita amanda putri
"""

print("membuat pembeda jenis segitiga")
s1=int(input("sisi 1: "))
s2=int(input("sisi 2: "))
s3=int(input("sisi 3: "))

if (s1==s2)and(s2==s3):
    print("jenis segitiga adalah : segitiga sama sisi. ")
elif (s1==s2)or(s2==s3): 
    print("jenis segitiga adalah : segitiga sama kai. ")
elif (s1+s2<=s3)or(s1+s3<=s2)or(s3+s2<=s1): 
    print("tidak mungkin membentuk segitiga")
else:
    print("jenis segitiga adalah : segitiga sembarang")