"""
Created on Mon 18 Jul 2022 03:20:40 PM EAT

Write a function called user_name that generates a username from
the user’s email. The code should ask the user to input an email and
the code should return everything before the @ sign as their user
name.

For example, if someone enters ben@gmail.com, the code
should return ben as their user name.
"""


def user_name(username):
    if not '@' in username:
        return "[-]Enter a Valid email!!"  # Make sure the username is correct 
    else:
        return username.split("@")[0]# the .split() function returns a list of substrings, in this case, seperated by the @ delimeter
                    # I used [0] index to access the first element in the list which is the username 




if __name__ == '__main__':
    print(user_name(str(input("Enter your username here :  "))))
