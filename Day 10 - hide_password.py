"""
Created on Tue Apr 03 2023
@author: GRACE ESTRADA

Day 10 of 50 Days of Python

Write a function called hide_password that takes no parameters. 

The function takes an input( a password) from a user and returns ahidden password. 
For example, if the user enters ‘hello’ as a password the function should return ‘*****’ as a password 
and tell the user that the password is 5 characters long.
"""

#Define hide_password function

def hide_password():
    password = input('Please enter your password: ')
    password_chars = len(password)
    password_hidden = password_chars * '*'

    return f'Your password is {password_hidden}. It is {password_chars} characters long'
    

hide_password()

"""
EXTRA CHALLENGE: Strings With A Thousand Separator

Your new company has a list of figures saved in a list. 
The issue is that these numbers have no separator. 
The numbers are saved in the following format: [1000000, 2356989, 2354672, 9878098]

You have been asked to write a code that will convert each of the numbers in the list into a string. 
Your code should then add a comma on each number as a thousand separator for readability. 

When you run your code on the above list, your output should be :
['1,000,000', '2,356,989', '2,354,672', '9,878,098']

Write a function called convert_numbers that will take one argument, a list of numbers above
"""


#Define convert_numbers function

def convert_numbers(nums_list):
    #converted = list(map(lambda x: "{:,}".format(x), nums_list)) -- or
    converted = list(map(lambda x: f"{x:,}", nums_list))
    return converted

convert_numbers([1000000, 2000000])