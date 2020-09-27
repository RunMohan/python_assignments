# -*- coding: utf-8 -*-
"""
Created on Sun Sep 27 21:24:40 2020

@author: Sushmita
"""

lst1=[10,20,30,40,50]
lst=[]
for i in range(len(lst1)):
    lst.append(lst1[len(lst1)-1-i])
    
print(*lst)