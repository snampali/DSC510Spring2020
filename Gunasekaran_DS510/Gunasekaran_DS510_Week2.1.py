# File :    Gunasekaran_DS510_week2_1.py
# Name :    Ragunath Gunasekaran
# Date :    03/20/2020
# Course :  DSC-510 - Introduction to Programming
# Assignment :
#           Using comments, create a header at the top of the program indicating the purpose of the program, assignment number, and your name. Use the SIUE Style Guide as a reference.
#           Display a welcome message for your user.
#           Retrieve the company name from the user.
#           Retrieve the number of feet of fiber optic cable to be installed from the user.
#           Calculate the installation cost of fiber optic cable by multiplying the total cost as the number of feet times by price by feet purchased.
#               Price is $0.87
#               Print a receipt for the user including the company name, number of feet of fiber to be installed, the calculated cost, and total cost in a legible format.
# Desc :    Program to calculate total cost of fiber cable installation
# Usage :
#           The program prompts the user for company name, required feet of fiber optical cable to be installed
#           The program will calculate the cost of prints the receipt for the user
import datetime

# This function will calculate the total cost
def calculate_total(length_of_fiber_cable: int):
    return length_of_fiber_cable * 0.87 # 0.87 as price per feet

# This function will print the customer receipt
def print_receipt(company_name: str, length_of_fiber_cable: int, total_cost: float):
    now = datetime.datetime.now()
    print(format(company_name) + ", here is your receipt :")
    print("-------------------------------")
    print('Receipt Date : ' + now.strftime("%Y-%m-%d %H:%M:%S"))  # printing date & time
    print('Invoice for : {0}'.format(company_name))  # printing company name
    print('Purchased length of feet : {:,}'.format(length_of_fiber_cable))  # printing the fiber length
    print('Total cost is : ', total_cost)  # sale price
    print('Total formatted cost is :', '${:,.2f}'.format(total_cost))  # sale formatted price

def main():
    print("Welcome to the RAGU's Fiber Optics")
    company_name: str = input("Enter your company name \n")
    while True:  # making sure the entered input is valid number
        try:
            length_of_fiber_cable: int = int(input("Enter the length of fiber cable in feet \n"))
            if (length_of_fiber_cable < 0):
                print("Oops!  That was no valid number.  Try again...")
                continue
            else:
                break
        except ValueError:
            print("Oops!  That was no valid number.  Try again...")

    # calling function which returns the total price
    total_cost = calculate_total(length_of_fiber_cable)

    # printing the receipt to the customer
    print_receipt(company_name, length_of_fiber_cable, total_cost)


if __name__ == '__main__':
    main()
