Created on Sun Sep 27 22:21:35 2020

@author: Sushmita
"""

num = int(input("enter the number of rows:"))
for i in range(1,num+1):
    print(" "*(num-i)+"* "*i)
for i in range(num,0,-1):
    print(" "*(num-i)+"* " *i)
