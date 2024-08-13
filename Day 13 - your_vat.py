"""
Created on Tue Aug 13 2024
@author: GRACE ESTRADA

Day 13 of 50 Days of Python

Write a function called your_vat. 
The function takes no parameter. 
The function asks the user to input the price of an item and VAT (vat should be a percentage). 

The function should return the price of the item plus VAT. 
If the price is 220 and, VAT is 15% your code should return a vat inclusive price of 253. 

Make sure that your code can handle ValueError. 
Ensure the code runs until valid numbers are entered. (hint: Your code should include a while loop)
"""

def your_vat():
    while True:
        try:
            price = 0
            price = input("Please enter the price of your product (or type 'exit' to quit): ")
            if price.lower() == 'exit':
                print('Exiting the program. Thank you!')
                break
            else:
                price = int(price)
            vat = int(input("Please input vat percentage (in %): "))
            price_vat_inc = round(price * (1 + (vat/100)), 2)
            print(price_vat_inc)
        
        except:
            print("Please enter a numeric value")


your_vat()
