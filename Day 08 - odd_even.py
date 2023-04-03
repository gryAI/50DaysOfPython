"""
Created on Tue Mar 29 2023
@author: GRACE ESTRADA

Day 8 of 50 Days of Python

Write a function called odd_even that has one parameterand takes a list of numbers as an argument. 

The functionreturns the difference between the largest even number in the list and the smallest odd number in the list. 
For example, if you pass [1,2,4,6] as an argument the function should return '6 - 1 = 5'
"""

#Define string_range function

def odd_even(list_nums):
    max_even = max(list(filter(lambda x: x%2 == 0, list_nums)))
    min_odd = min(list(filter(lambda x: x%2 != 0, list_nums)))

    return f'{max_even} - {min_odd} = {max_even - min_odd}'


odd_even([1,2,4,6])  



