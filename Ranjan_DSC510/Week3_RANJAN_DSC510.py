# Title     : Week3 - Programming Assignment
# Author    : Vikas Ranjan
# Date      : 3/29/2020
# Purpose   :This week we will implement “if statements” in a program. Your program will calculate the cost of fiber optic cable installation by multiplying the number of feet needed by $0.87. We will also evaluate a bulk discount. You will prompt the user for the number of fiber optic cable they need installed. Using the default value of $0.87 calculate the total expense. If the user purchases more than 100 feet they are charged $0.80 per foot. If the user purchases more than 250 feet they will be charged $0.70 per foot. If they purchase more than 500 feet, they will be charged $0.50 per foot.
#              Your program must have a header. Use the SUI--Edwardsville Programming Style Guide for guidance.
#              Display a welcome message for your program.
#              Get the company name from the user.
#              Get the number of feet of fiber optic cable to be installed from the user.
#              Evaluate the total cost based upon the number of feet requested.
#              Display the calculated information including the number of feet requested and company name.

# Import datetime
import datetime

def main():
    user_input()
    calc_install_cost(cableLength)
    print_receipt(companyName, cableLength, installationCost)

def user_input():
    # Display a welcome message for your user.
    print("Hello, Welcome to Python Cables!", "Hope you are having a good day!\n", sep="\n")

    # Retrieve the company name from the user.
    global companyName
    companyName = input("Please enter your Company Name!\n")

    # Retrieve the number of feet of fiber optic cable to be installed from the user.
    # Make sure to accept only integer or floating values
    while True:
        global cableLength
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

def calc_install_cost(cableLength):
    # Calculate the installation cost of fiber optic cable by multiplying the total cost as the number of feet times $0.87
    cableLengthInt = int(cableLength)
    if cableLengthInt > 500:
        install_rate = 0.50
    elif cableLengthInt > 250:
        install_rate = 0.70
    elif cableLengthInt > 100:
        install_rate = 0.80
    else:
        install_rate = 0.87
    global installationCost
    installationCost = float(cableLengthInt) * install_rate
    print("Total installation cost is $" + str(installationCost) + "\n")

def print_receipt(companyName, cableLength, installationCost):
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

if __name__ == '__main__':
    main()
