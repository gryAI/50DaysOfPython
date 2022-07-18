"""
Created on Mon 18 Jul 2022 02:19:53 PM EAT


Day 3  50 Days of Python

Write a function called register_check that checks how many students
are in school. The function takes a dictionary as a parameter. If the
student is in school, the dictionary says ‘yes’. If the student is not in
school, the dictionary says ‘no’. Your function should return the number
of students in school.

For example using the dictionary below, your function should return 3.
register = {'Michael':'yes','John': 'no',
'Peter':'yes', 'Mary': 'yes'}
"""

def register_check(param):
    found = 0 # initialize found to 0, then increment its value every time we find a True value in the dictionary

    for key, value in param.items():
        if value.upper() == "YES":
            found+= 1 
        else:
            pass 


    return found



if __name__ == '__main__':

    print(register_check({"Hanna":"Yes", "Juliet":"No", "Montana":"Yes"}))#  this should return 2

    #Run more Test cases with custom dictionaries 