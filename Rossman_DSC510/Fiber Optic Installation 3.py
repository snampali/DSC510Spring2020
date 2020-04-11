def main():
    """
Fiber Optic Install Part 3

Institution: Bellevue University
Course: DSC510
Assignment: 3.1
Date: 6 Apr 2020
Name: Alfred Rossman
Interpreter: Python 3.8
    """

# Print docstring header
print(main.__doc__)
import datetime
today_date = datetime.datetime.today()

# Cost Constants for: Base, >=100', >=250', >=500'
# NOTE: Although the assignment said "greater than" I am using "or equal to"
#       My experience is that customers will expect the price break at 100', without requiring greater than 100'
COST_BASE = 0.87
COST_100  = 0.80
COST_250  = 0.70
COST_500  = 0.50

# Sales Tax Rate: Austin, Travis County, TX
SALES_TAX = 0.0825

company_name = input('Hello\nPlease Enter Company Name: ')
fo_length = input('Enter Fiber Optic Length in Feet: ')
fo_length = float(fo_length)

# Fiber Optic Cable Install Length Cost Structure
if   fo_length >= 500: install_cost = fo_length * COST_500;  unit_cost = COST_500
elif fo_length >= 250: install_cost = fo_length * COST_250;  unit_cost = COST_250
elif fo_length >= 100: install_cost = fo_length * COST_100;  unit_cost = COST_100
else:                  install_cost = fo_length * COST_BASE; unit_cost = COST_BASE

#Calculate Total Cost and Print Receipt
total_cost = install_cost * (1.0 + SALES_TAX)
total_cost = round(total_cost, 2)
print('\nDate: ', today_date.strftime("%d/%B/%Y"))
print('Receipt for:',company_name)
print('Fiber Optic Length in Feet:', fo_length)
print('Cost Per Foot: $', format(unit_cost, '.2f'))
print('Install Cost: $', format(install_cost, '.2f'))
print('Sales Tax Rate:', SALES_TAX * 100.0, '%')
print('Sales Tax: $', format(install_cost * SALES_TAX, '.2f'))
print('Total Installed Cost: $', format(total_cost, '.2f'))
