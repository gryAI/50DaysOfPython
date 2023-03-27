"""
Created on Tue Mar 27 2023
@author: GRACE ESTRADA

Day 6 of 50 Days of Python

Write a function called user_name that generates a username from the user’s email. 

The code should ask the user to input an email and the code should return everything before the @ sign as their user name. 
For example, if someone enters ben@gmail.com, the code should return ben as their user name
"""

#Define user_name function

def user_name():
    email = input('Please enter your email: ')
    username = email.split('@')[0]

    return f'Your username is: {username}'

user_name()
