'''
Course: DSC510
Assignment: 6.1 Programming Function
Name: David TS
Date: 04/19/2020
Description: Get different temperatures from user and determine largest, smallest and count
'''
# Declare empty temperature list
temperature = []
while True:
    while True:  # Input Validations
        try:
            TempVal = int(input('Enter the temperature or enter 1000 to end : '))
            break
        except ValueError:
            print("Oops!  That was not valid number.  Try again...")
    if TempVal != 1000:
        temperature.append(TempVal)  # to add the temperature
    else:
        break
temperature.sort()
print('Largest Temperature : ' + str(temperature[-1]))
print('Smallest temperature : ' + str(temperature[0]))
print('Total nummber of temperatures : ' + str(len(temperature)))
