# course: DSC510
# assignment: 2.1
# date: 3/17/20
# name: Blaine Blasdell
# description: Customer Fiber Optic cable calculator

# Get Today's date for receipt
import datetime
today_date = datetime.datetime.today()

# welcome message
print('Welcome to Blasdell\'s IT Services')
print('\r')
print('Fiber Optic Cable Cost Calculator')
print('\r')

# input customer's company name
company_name = input('Please enter your company name: ')
print('\r')

# input customer's cable need
cable_feet: float = float(input('Please enter the amount of fiber you need (in feet): '))
print('\r')

# set default cable price
default_price = 0.87
cable_price = default_price

# calculate bulk discount
# > 100 feet = 0.80
# > 250 feet = 0.70
# > 500 feel = 0.50

if cable_feet > 500.0:
    cable_price = 0.50
elif cable_feet > 250.0:
    cable_price = 0.70
elif cable_feet > 100.0:
    cable_price = 0.80

# calculate customer price feet * default price
installation_cost = cable_feet * cable_price

# calculate VA State (Prince William County) sales tax and total cost
sales_tax = 0.053
sales_tax_cost = installation_cost * sales_tax
total_cost = sales_tax_cost + installation_cost





# receipt display
print('\r')
print('\r')
print('------------------------------------------------------')
print('            Blasdell\'s IT Services\r')
print('                    Receipt\r')
print('                  ', today_date.strftime("%m/%d/%y"))
print('\r')
print('\r')
print('Company: ', company_name)
print('Fiber optic cable amount (in feet)', cable_feet)
print('Fiber Cable installation price: $ ', format(cable_price, '.2f'))
print('\r')
print('Installation total: $', format(installation_cost, '.2f'))
print('Sales Tax: $', format(sales_tax, '.3f'))
print('Total Cost (including Tax): ', format(total_cost, '.2f'))
print('\r')
print('------------------------------------------------------')
# end program
