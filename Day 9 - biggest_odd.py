"""
Created on Tue Mar 31 2023
@author: GRACE ESTRADA

Day 9 of 50 Days of Python

Create a function called biggest_odd that takes a string of numbers and returns the biggest odd number in the list. 

For example, if you pass ‘23569’ as an argument, your function should return 9. 
Use list comprehension.
"""

#Define biggest_odd function

def biggest_odd(str_nums):
    biggest = max([x for x in str_nums if int(x)%2 != 0])

    return f'The biggest odd number is {biggest}'
    

biggest_odd('23569')
