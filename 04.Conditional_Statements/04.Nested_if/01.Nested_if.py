""" Nested if Syntax

if condition1:
    code block if the conditon1 is ture
        if condition 2 
            code block if the condition2 is ture
        else 
            code block if the condition2 is false
else
    code block if the condition1 is flase
    
"""

# Find positive or negitve 

x=-10
y=3

if x>0:
    if  y>0:
     print("Both x and y are positive ")
    else:
     print(" x is positive ,y is negative ")
else:
   print("x is negative ")
