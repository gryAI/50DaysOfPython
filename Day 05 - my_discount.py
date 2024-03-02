"""
Created on Tue Mar 24 2023
@author: GRACE ESTRADA

Day 5 of 50 Days of Python

Create a function called my_discount. 

The function takes no arguments but asks the user to input the price and the discount (percentage) of the product. 

Once the user inputs the price and discount, it calculates the price after the discount. 
The function should return the price after the discount. 

For example, if the user enters 150 as price and 15% as the discount, your function should return 127.5

"""

#Define my_discount function
def my_discount():
    price = input('Please enter the price:')
    discount = input('Please enter the discount (in percentage):')

    price_float = float(price)
    discount_float = float(discount.strip('%')) / 100

    discounted = price_float * (1 - discount_float)

    return f'The price after discount is: {discounted}'

my_discount()


