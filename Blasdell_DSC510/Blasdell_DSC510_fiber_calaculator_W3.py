# course: DSC510
# assignment: 3.1
# date: 3/17/20
# name: Blaine Blasdell
# description: Customer Fiber Optic cable calculator

# Get Today's date for receipt
import datetime

today_date = datetime.datetime.today()


# Function to calculate the price based on two inputs feet & price
def calculate_cost(cable_ft, cable_pr):
    return cable_ft * cable_pr


# welcome message
print('Welcome to Blasdell\'s IT Services')
print('\r')
print('Fiber Optic Cable Cost Calculator')
print('\r')

# input customer's company name
company_name = input('Please enter your company name: ')
print('\r')

# input customer's cable need
cable_feet = input('Please enter the amount of fiber you need (in feet): ')

print('\r')

# Check to ensure a cable amount is entered (check for null)
if cable_feet:

    # convert input string to a float
    cable_feet_float = float(cable_feet)

    # check to ensure numeric amount is greater then zero
    if cable_feet_float > 0:

        #    set default cable price
        default_price = 0.87
        cable_price = default_price

        # calculate bulk discount
        # > 100 feet = 0.80
        # > 250 feet = 0.70
        # > 500 feel = 0.50
        if cable_feet_float > 500.0:
            cable_price = 0.50
        elif cable_feet_float > 250.0:
            cable_price = 0.70
        elif cable_feet_float > 100.0:
            cable_price = 0.80
        else:
            cable_price = default_price

        # calculate customer price feet * default price
        # installation_cost = cable_feet_float * cable_price
        installation_cost = calculate_cost(cable_feet_float, cable_price)

        # calculate VA State (Prince William County) sales tax and total cost
        sales_tax = 0.053
        sales_tax_cost = installation_cost * sales_tax
        total_cost = sales_tax_cost + installation_cost

        # receipt display
        print('\r')
        print('\r')
        print('------------------------------------------------------------')
        print('                  Blasdell\'s IT Services\r')
        print('                          Receipt\r')
        print('                        ', today_date.strftime("%m/%d/%y"))
        print('\r')
        print('\r')
        print('Company: ', company_name)
        print('Fiber optic cable amount (in feet)', format(cable_feet_float, '.2f'))
        print('Fiber Cable installation price: $ ', format(cable_price, '.2f'))
        print('\r')
        print('Installation total: $', format(installation_cost, '.2f'))
        print('VA Sales Tax: $', format(sales_tax, '.3f'))
        print('Total Cost (including Tax): $', format(total_cost, '.2f'))
        print('\r')
        print('------------------------------------------------------------')
    else:
        # Print error is number is not greater then zero
        print('\r')
        print('*** Error ***')
        print('Please enter a valid amount of fiber cable (1 - 1,000,000)')
        print('\r')
else:
    # Print error if no value entered for cable
    print('\r')
    print('*** Error ***')
    print('Please enter a valid amount of fiber cable (1 - 1,000,000)')
    print('\r')
# end program
