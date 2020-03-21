# course: DSC510
# assignment: 2.1
# date: 3/17/20
# name: Blaine Blasdell
# description: Customer Fiber Optic cable calculator

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
installation_cost = format(cable_feet * cable_price, '.2f')

# receipt display
print('\r')
print('\r')
print('------------------------------------------------------')
print('Blasdell\'s IT Services\r')
print('Receipt\r')
print('\r')
print('\r')
print('Company: ', company_name)
print('Fiber optic cable amount (in feet)', cable_feet)
print('Fiber Cable installation price: $ ', format(cable_price, '.2f'))
print('\r')
print('Installation total: $', installation_cost)
print('\r')
print('------------------------------------------------------')
# end program
