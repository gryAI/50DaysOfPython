"""
Created on Tue Apr 04 2023
@author: GRACE ESTRADA

Day 11 of 50 Days of Python

Write a function called equal_strings. The function takes two strings as arguments and compares them. 
If the strings are equal (if they have the same characters and have equal length), it should return True, if they are not, it should return False. 

For example, ‘love’ and ‘evol’ should return True.

"""

#Define equal_strings function

def equal_strings(str1, str2):
    
    #check if the strings have equal length
    if len(str1) == len(str2):
        
        #convert strings to list
        list_str1 = list(str1)
        list_str2 = list(str2)
        
        #sort the lists
        list_str1.sort()
        list_str2.sort()

        if list_str1 == list_str2:
            return True
        
        else:
            return False
        
    else:
        return False


equal_strings('love', 'eol')

