"""
Strings and Lists

Institution: Bellevue University
Course: DSC510
Assignment: 6.1
Date: 21 Apr 2020
Name: Alfred Rossman
Interpreter: Python 3.8
"""

# User Inputs a List of Temperatures (Celsius, Fahrenheit, or any unit, Range not validated, CR is Sentinel)
# Print Minimum, Maximum, and Number of Temperatures Entered

temperatures = []
while True:
    print('Enter Temperature ', len(temperatures) + 1, ' (or CR to complete entries): ')
    entry = input()
    if entry == '':
        break
    temperatures += [entry]
print('Minimum Temperature: ', min(temperatures))
print('Maximum Temperature: ', max(temperatures))
print('Number of Temperatures Entered: ', len(temperatures))
