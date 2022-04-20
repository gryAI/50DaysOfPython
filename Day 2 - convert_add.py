"""
Created on Thu Apr 21 12:08:31 2022
@author: LUMINE
"""

# Define the function
def convert_add(num):
    """
    Takes a list of strings as an argument and converts it to integers and sums the list.
    :param args: list(str): list of strings
    :return: int
    """
    numbers = [int(x) for x in num]
    result = sum(numbers)

    return result


# Simulate the function
simulation = convert_add(num = ['1', '3', '5'])
print(simulation)


