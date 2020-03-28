# Course: DSC510
# Assignment: 2.1
# Date: 03/17/20
# Name: William Justice
# Description: Program that calculates cost of cable installation

# Display welcome message to user
WelcomeMSG = "Welcome to the Justice Cable Calculator!!!"
print(WelcomeMSG)

# Retrieve the company name from the user
CompanyName = input("What is your company name?")

#Retrieve the number of feet of fiber optic cable to be installed from the user
Numft = int(input("How many feet do you need installed?"))

# Calculate the installation cost of fiber optic cable by multiplying the total cost as the number of feet times $0.87.
instCost = Numft*.87

# Print a receipt for the user including the company name, number of feet of fiber to be installed, the calculated cost, and total cost in a legible format.
print("*****Your Receipt******")
print("Company Name:                " + CompanyName)
print("Feet to be installed:        " + str(Numft)+"ft")
print("Total Cost:                 $" + str(instCost))




