"""
Course: DSC510
Assignment: 11.1 Programming Assignment
Name: David TS
Date: 05/23/2020
Description: Cash Register program using python object oriented programming concepts
"""
import locale


# Cash Register class to get the item price and counts
class CashRegister:
    def __init__(self):  # Initiate the variables
        self.total = 0
        self.items = 0

    def add_item(self, price):  # price and item counter
        self.total += price
        self.items += 1

    def get_total(self):  # get the total price
        return self.total

    def get_count(self):  # get the item count
        return self.items

    def get_clear(self):  # reset the variables
        self.total = 0
        self.items = 0


# function to get the user input and validation
def user_input_validation():
    valid = False
    while not valid:
        user_cr_input = input(
            'Please enter the \n 1)Price to add an item or 2)"exit" to exit the program or 3)Empty will clear your '
            'cart \n Input : ')
        if user_cr_input.upper() == 'EXIT' or len(user_cr_input) == 0 or is_numeric(user_cr_input):
            valid = True
            return user_cr_input
        else:
            print('Not valid, please try again....')
            valid = False


# To identify Integer & Float values of user input
def is_numeric(n):
    try:
        float(n)
    except ValueError:
        return False  # the user input is alpha
    return True


# Main function to call the user input function and print the output
def main():
    print('Welcome to the Shopping Mart !')
    cr = CashRegister()
    locale.setlocale(locale.LC_ALL, '')
    user_cr_input = user_input_validation()
    while is_numeric(user_cr_input): # To add the price using class method for program output
        item_price = float(user_cr_input)
        cr.add_item(item_price)
        print('Current total price is: ', locale.currency(cr.get_total()))
        print('Current item count is: ', cr.get_count())
        user_cr_input = user_input_validation()
    else: # To handle the other cases from the user input
        if user_cr_input.upper() == 'EXIT':
            print('Thank You !')
            print('Your have ' + str(cr.get_count()) + ' items in the cart.')
            print('Your total price is: ', locale.currency(cr.get_total()))
        else:
            cr.get_clear()
            print('Cleared the cart, Please start again !')


if __name__ == '__main__':
    main()
