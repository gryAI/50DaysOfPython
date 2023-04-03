"""
Created on Tue Feb 03 2023
@author: GRACE ESTRADA

Day 3 of 50 Days of Python

Write a function called register_check that checks how many students 
are in school. The function takes a dictionary as a parameter. If the 
student is in school, the dictionary says ‘yes’. If the student is not in 
school, the dictionary says ‘no’. Your function should return the number 
of students in school. Use the dictionary below. Your function should 
return 3.

"""

# Define the register_check function
def register_check(register):
    """
    Takes a dictionary of students and returns the number of students that are in school.
    :param register(dictionary): dictionary of students
    :return: int
    """
    
    num = sum(1 for value in register.values() if value.lower() == 'yes')

    return num


# Simulate the function
register = {'Michael':'yes', 'John':'no', 'Peter':'yes', 'Mary':'yes'}
number_of_enrolled = register_check(register)

print(f'Number of Enrolled Students: {number_of_enrolled}')




