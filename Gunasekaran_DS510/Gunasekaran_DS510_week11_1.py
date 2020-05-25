# File :    Gunasekaran_DS510_week11_1.py
# Name :    Ragunath Gunasekaran
# Date :    05/24/2020
# Course :  DSC-510 - Introduction to Programming
# Assignment :
    # Welcome message for the user.
    # One class called CashRegister.
    # Instance method called addItem which takes one parameter for price.
    #   The method should also keep track of the number of items in your cart.
    # Two getter methods.
    # getTotal – returns totalPrice
    # getCount – returns the itemCount of the cart
    #  A loop which allows the user to continue to add items to the cart until they request to quit.
    #  Print the total number of items in the cart.
    #  Print the total $ amount of the cart.
    # The output should be formatted as currency.
    #  Using  locale.setlocale and locale.currency.

import datetime
import locale

# Using SetLocale module to format numbers as currency ($)
locale.setlocale(locale.LC_ALL, 'en_US')


# CashRegister Class
class CashRegister(object):
    # init method
    def __init__(self):
        self.total_price = 0
        self.item_count = 0

    # Instance method - addItem  : Keep Total items and Total price in the Cart
    def add_item(self, price):
        self.total_price += int(price)
        self.item_count += 1

    def get_total(self):
        return self.total_price

    def get_count(self):
        return self.item_count


# Format Print method to print the jokes from url
def format_print():
    # Instance of class
    register = CashRegister()

    Isselection = True
    IsvalidInput = True
    # Loop - Will Allow users to enter the details until they enter N or Quit
    while Isselection:
        Isselection = input("Would you like to add another item to the cart Y or N\n\t").lower()
        # if we select Y or Yes, we will keep add the items and price into cart items
        if Isselection == "y" or Isselection == "yes":
            price = input("What is the price of the item?\n\t")
            register.add_item(price)
        # if we select N or Quit, we will keep print the total items and price in cart
        elif (Isselection.lower() == 'no' or Isselection.lower() == 'n' or Isselection.lower() == "quit"):
            Iscontinue = False
            IsvalidInput = True
            TotalValue = register.get_total()
            print("The Summary of Cart Details as below")
            print("#######################################")
            print("Total Number of Items in cart : " + str(register.get_count()))
            print("Total Amount of the cart (in $) : " + locale.currency(TotalValue, grouping=True))
            Isselection = False
            print("Thank You for using this Application! Come back Soon")
        # if we type other than Y, N, Quit, we will ask users to type the correct option
        else:
            print(
                "Invalid Input. Please enter Yes/Y to add new item in the cart. No/N or Quit to exit")
            Isselection = True
            IsvalidInput = False


def main():
    now = datetime.datetime.now()
    print("Welcome to the RAGU's Shoping World!")
    print('Date : ' + now.strftime("%Y-%m-%d %H:%M:%S"))  # printing date & time
    print("------------------------------------------")
    # Calling Format Print method to print the Jokes
    format_print()


if __name__ == '__main__':
    main()
