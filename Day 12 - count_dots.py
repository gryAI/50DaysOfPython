"""
Created on Tue Apr 05 2023
@author: GRACE ESTRADA

Day 12 of 50 Days of Python

Write a function called count_dots. 
This function takes a string separated by dots as a parameter and counts how many dots are in the string. 

For example, ‘h.e.l.p.’ should return 4 dots, and ‘he.lp.’ should return 2 dots.

"""

#Define count_dots function

def count_dots(str):
    count = str.count('.')
    
    return count

count_dots('h.e.l.p')

