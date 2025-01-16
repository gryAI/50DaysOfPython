"""
Created on Thu Aug 14 2024
@author: GRACE ESTRADA

Day 14 of 50 Days of Python

Write a function called same_in_reverse that takes a string and checks 
if the string reads the same in reverse.

If it is the same, the code should return True. 
If not, it should return False.

For example, 'dad' should return True because it reads the same in reverse.
"""


def same_in_reverse(text):

    text_i = len(text) - 1
    text_reverse = ""

    while text_i >= 0:
        text_reverse += text[text_i]
        text_i -= 1

    return text_reverse == text


is_same = same_in_reverse("dad")
is_same
