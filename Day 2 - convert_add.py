"""
Created on Thu Apr 21 12:08:31 2022
@author: GRACE ESTRADA

Day 2 50 Days of Python

Write a function called convert_add that takes a list of strings as an argument and
converts it to integers and sums the list.

For example, [‘1’, ‘3’, ‘5’] should be converted to [1, 3, 5] and summed to 9.

"""

# Define the convert_add function
def convert_add(num):
    """
    Takes a list of strings as an argument and converts it to integers and sums the list.
    :param num(list): list of strings
    :return: int
    """
    int_list = [int(x) for x in num]
    result = sum(int_list)

    return int_list, result


# Simulate the function
int_list, result = convert_add(num = ['1', '3', '5'])
print(f'The new list is: {int_list}\n'
      f'Sum of values is: {result}')


