# File :    Gunasekaran_DS510_week6_1.py
# Name :    Ragunath Gunasekaran
# Date :    04/19/2020
# Course :  DSC-510 - Introduction to Programming
# Assignment :
#           Create an empty list called temperatures.
#           Allow the user to input a series of temperatures along with a sentinel value which will stop the user input.
#           Evaluate the temperature list to determine the largest and smallest temperature.
#           Print the largest temperature.
#           Print the smallest temperature.
#           Print a message tells the user how many temperatures are in the list.
import datetime

# Create an empty list called temperatures
temperatures = []


# This function will get the input of temperatures List and add it to the List
def getInput():
    print("enter a series of temperatures, use -1 (sentinel value) to stop ")
    userInput = input("")
    while int(userInput) != -1:
        print("enter a series of temperatures, use -1 (sentinel value) to stop ")
        temperatures.append(int(userInput))
        userInput = input("")
    return temperatures


# This function will print the temperatures details
def print_receipt(company_name: str, temperatureslist: list):
    now = datetime.datetime.now()
    print(format(company_name) + ", here is your Calculation of the temperature list  :")
    print("-------------------------------")
    print('Date : ' + now.strftime("%Y-%m-%d %H:%M:%S"))  # printing date & time
    print("The Series of Temperatures Entered : " + str(temperatureslist))
    print("The Largest temperature is " + str(max(temperatureslist)))
    print("The Smallest temperature is " + str(min(temperatureslist)))
    print("The Number of temperatures entered in the list is " + str(len(temperatureslist)))


def main():
    company_name: str = input("Enter your name : \n")
    temperatureslist = getInput()
    print_receipt(company_name, temperatureslist)

    # writing the details in the log file
    fileout = open("D:\Python\myfiles.txt", "w")  # Open the file for reading and writing
    fileout.write("Enter your name \n"
                  + "Name is :" + (company_name) + "\n"
                  + "The Series of Temperatures Entered : " + str(temperatureslist) + "\n"
                  + "The Largest temperature is " + str(max(temperatureslist)) + "\n"
                  + "The Smallest temperature is " + str(max(temperatureslist))
                  + "The Number of temperatures entered in the list is " + str(len(temperatureslist)))

    fileout.close()


if __name__ == '__main__':
    main()
