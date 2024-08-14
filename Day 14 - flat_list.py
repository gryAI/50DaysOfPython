"""
Created on Tue Aug 14 2024
@author: GRACE ESTRADA

Day 14 of 50 Days of Python

Write a function called flat_list that takes one argument, a nested list. 
The function converts the nested list into a one-dimension list. 
For example [[2,4,5,6]] should return [2,4,5,6]
"""

def flatten_list(nested_list):
    flat_list = []
    for item in nested_list:
        if isinstance(item, list):
            flat_list += flatten_list(item)  # Recursively flatten the list
        else:
            flat_list.append(item)  # Append the item if it's not a list
    return flat_list


list_3d = [
    [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ],
    [
        [10, 11, 12],
        [13, 14, 15],
        [16, 17, 18]
    ],
    [
        [19, 20, 21],
        [22, 23, 24],
        [25, 26, 27]
    ]
]

flat_list = flatten_list(list_3d)
print(flat_list)
