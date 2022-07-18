"""
Created at Mon 18 Jul 2022 03:41:40 PM EAT


Write a function called hide_password that takes no parameters.
The function takes an input( a password) from a user and returns a
hidden password. For example, if the user enters ‘hello’ as a
password the function should return ‘****’ as a password and tell the
user that the password is 4 characters long.
"""


def hidden_password():
    return "*" * len(str(input("Enter Your Password here to be hidden:  ").strip()))



if __name__ == '__main__':
    print(hidden_password())
