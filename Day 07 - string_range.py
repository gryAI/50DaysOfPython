"""
Created on Tue Mar 28 2023
@author: GRACE ESTRADA

Day 7 of 50 Days of Python

Write a function called string_range that takes a single number and returns a string of its range. 

The string characters should be separated by dots(.) 
For example, if you pass 6 as an argument, your function should return ‘0.1.2.3.4.5’
"""

#Define string_range function

def string_range(num):
    s_range = [str(i) + "." for i in range(num)]
    return "".join(s_range)
    

string_range(6)




