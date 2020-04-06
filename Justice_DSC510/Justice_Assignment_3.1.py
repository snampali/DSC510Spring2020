# Course: DSC510
# Assignment: 3.1
# Date: 03/29/20
# Name: William Justice
# Description: Program that calculates cost of cable installation

# Display welcome message to user
WelcomeMSG = "Welcome to the Justice Cable Calculator!!!"
print(WelcomeMSG)

# Retrieve the company name from the user
CompanyName = input("What is your company name?")

#Retrieve the number of feet of fiber optic cable to be installed from the user
Numft = int(input("How many feet do you need installed?"))

# Calculate the installation cost of fiber optic cable by... multiplying the total cost as the number of feet times bulk price discount rate.
instCost = Numft*.87
if Numft >= 101:
    instCost = Numft*.80
if Numft >= 251:
    instCost = Numft*.70
if Numft >= 501:
    instCost = Numft*.50

# Print a receipt for the user including the company name, number of feet of fiber to be installed, the calculated cost, and total cost in a legible format.
print("*****Your Receipt******")
print("Company Name:                " + CompanyName)
print("Feet to be installed:        " + str(Numft)+"ft")
print("Total Cost:                 $" + str(instCost))
