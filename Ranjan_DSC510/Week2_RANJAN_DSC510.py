# Title     : Week2 - Programming Assignment
# Author    : Vikas Ranjan
# Date      : 3/22/2020
# Purpose   : Create a program with the following requirements:
#               Using comments, create a header at the top of the program indicating the purpose of the program, assignment number, and your name. Use the SIUE Style Guide as a reference.
#               Display a welcome message for your user.
#               Retrieve the company name from the user.
#               Retrieve the number of feet of fiber optic cable to be installed from the user.
#               Calculate the installation cost of fiber optic cable by multiplying the total cost as the number of feet times $0.87.
#               Print a receipt for the user including the company name, number of feet of fiber to be installed, the calculated cost, and total cost in a legible format.
#               Include appropriate comments throughout the program.

# Import datetime
import datetime

# Display a welcome message for your user.
print("Hello, Welcome to Python Cables!", "Hope you are having a good day!\n", sep="\n")

# Retrieve the company name from the user.
companyName = input("Please enter your Company Name!\n")

# Retrieve the number of feet of fiber optic cable to be installed from the user.

# Make sure to accept only integer or floating values
while True:
    cableLength = input("How many feet of fiber optic cable you would want to be installed?\n")
    try:
        int(cableLength)
        break
    except ValueError:
        try:
            float(cableLength)
            break
        except ValueError:
             print("Please check and enter valid length!\n")

# Calculate the installation cost of fiber optic cable by multiplying the total cost as the number of feet times $0.87
installationCost = float(cableLength) * 0.87
print("Total installation cost is $" + str(installationCost) + "\n")

# Print a receipt for the user including the company name, number of feet of fiber to be installed, the calculated cost, and total cost in a legible format.
print("=======================================================================")
print(" Python Cables Invoice")
print("=======================================================================")
print("Company where installed: " + companyName)
print("Date/Time of service: " + str(datetime.datetime.now()))
print("length of fiber cable installed: " + cableLength + " Feet")
print("TOTAL installation cost: $" + str(installationCost))
print("=======================================================================")
print(" Thank you for your business!")
print("=======================================================================")
