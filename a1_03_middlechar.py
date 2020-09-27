# -*- coding: utf-8 -*-
"""
Created on Sun Sep 27 23:27:10 2020

@author: Sushmita
"""

strng1 = input("Enter a string with odd number of charachters\n")
n = len(strng1)
newlen = n - 3
startpos = int(newlen/2)
print(strng1[startpos:startpos+3])
