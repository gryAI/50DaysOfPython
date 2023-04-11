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


"""
EXTRA CHALLENGE: Your Age in Minutes

Write a function called age_in_minutes that tells a user how old they are in minutes. 
Your code should ask the user to enter their year of birth, and it should return their age in minutes (by subtracting their year of birth to the current year). 

Here are things to look out for:
    a. The user can only input a 4 digit year of birth. 
       For example, 1930 is a valid year. 
       However, entering any number longer or less than 4 digits long should render input invalid. 
       Notify the user to input a four digits number.

    b. If a user enters a year before 1900, your code should tell the user that input is invalid. 
       If the user enters the year after the current year, the code should tell the user, to input a valid year.
       The code should run until the user inputs a valid year. 
       
Your function should return the user's age in minutes. 
For example, if someone enters 1930, as their year of birth your function should return:
You are 48,355,200 minutes old.

"""

#Define age_in_minutes function

import datetime

def age_in_minutes():
    while True:
        year = input("Please enter your year of birth (four digits): ")
        if len(year) != 4:
            print("Invalid input. Please enter a four-digit year.")
        elif int(year) < 1900 or int(year) > datetime.datetime.now().year:
            print("Invalid input. Please enter a valid year.")
        else:
            break
    
    age_in_years = datetime.datetime.now().year - int(year)
    age_in_minutes = age_in_years * 365 * 24 * 60
    print("You are {} minutes old.".format(age_in_minutes))


age_in_minutes()
