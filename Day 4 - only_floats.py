"""
Created on Mon 18 Jul 2022 02:31:23 PM EAT


Write a function called only_floats, which takes two parameters a
and b, and returns 2 if both arguments are floats, returns 1 if only
one argument is a float, and returns 0 if neither argument is a float.

For example, if you pass (12.1, 23) as an argument, your function should return 1.
"""

def only_floats(a,b):
    if type(a) == float and type(b) == float :
        return 2 
    elif type(a) == float or type(b) == float:
        return 1 
    else :
        return 0 


if __name__ == '__main__':
    #test_cases
    print(only_floats(10.5,45)) # This should return 1 
    print(only_floats(13.0,0.2)) # This should return 2 
    print(only_floats(12,5)) # This should return 0 
    print(only_floats([45,15], "A string")) # This should return 0 

