"""
Created on Thu Apr  7 01:52:31 2022
@author: GRACE ESTRADA

Day 1 50 Days of Python

Write a function called divide_or_square that takes one argument (a number), 
and returns the square root of the number if it is divisible by 5, 
returns its remainder if it is not divisible by 5.

For example, if you pass 10 as an argument, then your function should return 3.16 as the square root.

"""

# Importing functions
from math import sqrt

# Defining divide_or_square function
def divide_or_square(n):
    """
    Takes one argument (a number), and returns the following:
        - square root of the number if it is divisible by 5,
        - remainder if it is not divisible by 5
    :param n(int): a number to be divided or squared
    :return: int
    """
    if n % 5 == 0:
        return sqrt(n)
    else:
        return n % 5


#Execute the function with user input
prompt = ''

while prompt.lower() != 'no':
    user_input = int(input('\nPlease input a number: '))
    print(divide_or_square(user_input))
    prompt = input('Continue? Yes or No?: ')

input('\nPress ENTER to exit')