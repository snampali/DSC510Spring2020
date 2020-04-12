def main():
    """
Simple I/O and Arithmetic

Institution: Bellevue University
Course: DSC510
Assignment: 2.1
Date: 6 Apr 2020
Name: Alfred Rossman
Intepreter: Python 3.8
    """

# Print docstring header
print(main.__doc__)

# Fiber Optic Input, Calculation, and Print Receipt
COST = 0.87
company_name = input('Hello\nPlease Enter Company Name: ')
fo_length = input('Enter Fiber Optic Length in Feet: ')
install_cost = float(fo_length) * COST
install_cost = round(install_cost, 2)
print('Receipt for:',company_name)
print('Fiber Optic Length in Feet:', fo_length)
print('Cost per foot: $', COST)
print('Total Installed Cost: $', install_cost)

