Created on Sun Sep 27 23:44:37 2020

@author: Sushmita

s1 = input("Enter the first string\n")
s2= input("Enter the second string\n")
s = s1 + s2
lens1 = len(s1)
lens2 = len(s2)
lens = len(s)
x=''
if lens1>lens2:
    for i in range(lens2):
        x = x + s[i]+s[lens-1-i]
    print(x+s[lens2:lens2+(lens1-lens2)])
    
else:
    for i in range(lens1):
        x = x + s[i]+s[lens-1-i]
    print(x+s[lens1:lens1+(lens2-lens1)])
    
    
