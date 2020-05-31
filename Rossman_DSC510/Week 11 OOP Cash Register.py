# OOP Cash Register

def docString():

    """
HEADER
Institution: Bellevue University
Course: DSC510
Assignment: 11.1
Date: 29 May 2020
Name: Alfred Rossman
Interpreter: Python 3.8
    """

print(docString.__doc__)                                # Print docstring Header
import locale                                           # Internationalization Services
locale.setlocale(locale.LC_ALL, '')                     # Set to Local Currency

def main():
# Cash Register Simulation done with OOP
#
    totalPrice = 0.0                                    # Initialize Cart Total Amount to floating point
    totalCount = 0                                      # Initialize Cart Item Count to integer
    print('Welcome: Cash Register Simulation')
    print('\nEnter Price of Item in Local Currency (Do not use any symbols [i.e. no commas or $], Enter 0 or Negative amount to end:)')

    class CashRegister:                                 # Single class (no inheritance)
        def __init__(self, totalPrice, totalCount):
            self.totalPrice = totalPrice                # Attributes
            self.totalCount = totalCount

        def addItem(self, price):                       # Method takes Item Price, Cart Amount Total, Cart Item Count
            self.getTotal(price)
            self.getCount(price)

        def getTotal(self, price):                      # Method for Cart total of item costs
            self.totalPrice += price
            return(self.totalPrice)

        def getCount(self, totalCount):                 # Method for Cart count of items
            self.totalCount += 1
            return(self.totalCount)


# Let the Cash Register begin

    instance = CashRegister(totalPrice, totalCount)     # Instantiate Cash Register Class (create object)
    while True:                                         # Loop for user input (<= 0 to complete)
        itemPrice = float(input())
        if itemPrice <= 0.0:
            break                                       # Break at Cart completion
        instance.addItem(itemPrice)
        print('Item # ', instance.totalCount, locale.currency(itemPrice, grouping = True).rjust(10, ' '))
    print('Total # of Items ', instance.totalCount, '  Total Due: ', locale.currency(instance.totalPrice, grouping = True).rjust(6, ' '))

# End of Cash Register


# Start of main

if __name__ == '__main__':                              # Runs main() if file wasn't imported
    main()

# End of main
