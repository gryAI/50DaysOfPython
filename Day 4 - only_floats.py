"""
Created on Tue Mar 02 2023
@author: GRACE ESTRADA

Day 4 of 50 Days of Python

Write a function called only_floats, which takes two parameters a
and b, and returns 2 if both arguments are floats, returns 1 if only 
one argument is a float, and returns 0 if neither argument is a float.
If you pass (12.1, 23) as an argument, your function should return a 
1

"""

#Define only_floats function
def only_floats(a,b):
    floats = 0
    if isinstance(a, float):
        floats += 1
    elif isinstance(b, float):
        floats += 1
    else: floats += 0

    return floats

only_floats(1,1.2)
