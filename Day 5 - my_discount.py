"""
Created on Mon 18 Jul 2022 02:34:31 PM EAT

Create a function called my_discount. The function takes no
arguments but asks the user to input the price and the discount
(percentage) of the product. Once the user inputs the price and
discount, it calculates the price after the discount. The function
should return the price after the discount.

For example, if the user enters 150 as price and 15% as the discount, your function should
return 127.5.
"""

def my_discount():
    price = int(input("[+] Enter price:  ").strip())
    disc =  int(input("[+] Enter the percentage discount to allow on the item: "))

    return (price - price*(disc/100)) 


if __name__ == "__main__":
    print("[+] Price after allowing discount is ", my_discount())