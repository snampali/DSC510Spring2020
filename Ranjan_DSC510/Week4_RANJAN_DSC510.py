# Title     : Week4 - Programming Assignment
# Author    : Vikas Ranjan
# Date      : 4/5/2020
# Purpose   : Modify your IF Statement program to add a function. This function will perform the cost calculation.
#             The function will have two parameters (feet and price). When you call the function, you will pass two
#             arguments to the function; feet of fiber to be installed and the cost (remember that price is dependent
#             on the number of feet being installed). You probably should have the following:
#                   Your program must have a header. Use the SIU Edwardsville Programming Guide for guidance.
#                   A welcome message
#                   A function with two parameters
#                   A call to the function
#                   The application should calculate the cost based upon the number of feet being ordered
#                   A printed message displaying the company name and the total calculated cost

# Import datetime
import datetime

def main():
    companyName, cableLength = user_input()
    cableLengthInt = int(cableLength)
    install_rate = fetch_install_rate(cableLengthInt)
    installationCost = calc_install_cost(cableLengthInt, install_rate)
    print_receipt(companyName, cableLength, installationCost)

def user_input():
    # Display a welcome message for your user.
    print("Hello, Welcome to Python Cables!", "Hope you are having a good day!\n", sep="\n")

    # Retrieve the company name from the user.
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
                print("Please check and enter valid length!")
    return companyName, cableLength

def fetch_install_rate(cableLengthInt):
    # Calculate the installation cost of fiber optic cable based on length
    if cableLengthInt > 500:
        install_rate = 0.50
    elif cableLengthInt > 250:
        install_rate = 0.70
    elif cableLengthInt > 100:
        install_rate = 0.80
    else:
        install_rate = 0.87
    return install_rate

def calc_install_cost(cableLengthInt, install_rate):
    installationCost = float(cableLengthInt) * install_rate
    print("Total installation cost is $" + str(installationCost) + "\n")
    return installationCost

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
