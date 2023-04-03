"""
Created on Tue Apr 03 2023
@author: GRACE ESTRADA

Day 10 of 50 Days of Python

Write a function called hide_password that takes no parameters. 

The function takes an input( a password) from a user and returns ahidden password. 
For example, if the user enters ‘hello’ as a password the function should return ‘*****’ as a password 
and tell the user that the password is 5 characters long.
"""

#Define biggest_odd function

def hide_password():
    password = input('Please enter your password: ')
    password_chars = len(password)
    password_hidden = password_chars * '*'

    return f'Your password is {password_hidden}. It is {password_chars} characters long'
    

hide_password()
