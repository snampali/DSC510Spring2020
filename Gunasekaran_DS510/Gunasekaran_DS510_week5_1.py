# File :    Gunasekaran_DS510_week5_1.py
# Name :    Ragunath Gunasekaran
# Date :    04/12/2020
# Course :  DSC-510 - Introduction to Programming
# Assignment :
#           This program will perform various calculations (addition, subtraction, multiplication, division, and average calculation)
#           This program will contain a variety of loops and functions.
#           The program will add, subtract, multiply, divide two numbers and provide the average of multiple numbers input by the user.
#           Define a function named performCalculation which takes one parameter. The parameter will be the operation being performed (+, -, *, /).
#           This function will perform the given prompt the user for two numbers then perform the expected operation depending on the parameter that's passed into the function.
#           This function will print the calculated value for the end user.
#           Define a function named calculateAverage which takes no parameters.
#               This function will ask the user how many numbers they wish to input.
#               This function will use the number of times to run the program within a for loop in order to calculate the total and average.
#               This function will print the calculated average.
#               This program will have a main section which contains a while loop. The while loop will be used to allow the user to run the program until they enter a value which ends the loop.
#           The main program should prompt the user for the operation they wish to perform.
#               The main program should evaluate the entered data using if statements.
#               The main program should call the necessary function to perform the calculation
import datetime


# Function to add two numbers

def add(num1, num2):
    return num1 + num2


# Function to subtract two numbers
def subtract(num1, num2):
    return num1 - num2


# Function to multiply two numbers
def multiply(num1, num2):
    return num1 * num2


# Function to divide two numbers
def divide(num1, num2):
    return num1 / num2


# This function will perform the Arithmetic operation of two given numbers based on the operation we choose
def performcalculation(operation_num: int, number_1: int, number_2: int):
    if operation_num == 1:
        print(number_1, "+", number_2, "=",
              add(number_1, number_2))
    elif operation_num == 2:
        print(number_1, "-", number_2, "=",
              subtract(number_1, number_2))

    elif operation_num == 3:
        print(number_1, "*", number_2, "=",
              multiply(number_1, number_2))

    elif operation_num == 4:
        print(number_1, "/", number_2, "=",
              divide(number_1, number_2))
    else:
        print("Invalid input")


# calculateAverage which takes no parameters and calculate the Avg of given numbers
def calculate_average():
    n = int(input(" How many Number You wish to Input \n "))
    total_numbers = n
    summable = 0
    for num in range(0, n):
        total = int(input("Enter the " + str(n) + " number: "))
        summable += total
        n -= 1
    print("Sum of all entered numbers = ", summable)
    average = summable / total_numbers
    print("Average of all entered numbers = ", average)


# Calculate the sum and average of multiple user-entered numbers
def calculate_average_Multiple():
    numbers = input("Enter numbers separated by space ")
    numberList = numbers.split()
    print("All entered numbers ", numberList)
    # Calculating the sum of all user entered numbers
    sum = 0
    for num in numberList:
        sum += int(num)
    print("Sum of all entered numbers = ", sum)
    avg = sum / len(numberList)
    print("Average of all entered numbers = ", avg)


def main():
    now = datetime.datetime.now()
    print("Welcome to the RAGU's Calculator")
    user_name: str = input("Enter your Name : ")
    print("Enter the 2 Numbers to perform Arithmetic Calculation : ")
    number_1 = int(input("Enter first number: "))
    number_2 = int(input("Enter second number: "))
    print("-------------------------------")
    print('Date : ' + now.strftime("%Y-%m-%d %H:%M:%S"))  # printing date & time
    print(format(user_name) + ", here is your calculated details :")
    print("Please select operation -\n"
          "1. + - Add\n"
          "2. - - Subtract\n"
          "3. * - Multiply\n"
          "4. / - Divide\n")
    operation_num: int = int(input("Select operations form 1, 2, 3, 4 : \n"))
    if operation_num in range(1, 4):
        performcalculation(operation_num, number_1, number_2)
    else:
        print("Invalid input. Please input from 1, 2, 3, 4")
    print("-------------------------------")
    print("Please select option to calculate the Average -\n"
          "1. Enter the Input numbers one by one \n"
          "2. Enter the multiple input numbers with space \n"
          )
    option_num: int = int(input("Select operations form 1, 2 : \n"))
    if option_num == 1:
        calculate_average()
    elif option_num == 2:
        calculate_average_Multiple()
    else:
        print("Invalid input. Please input from 1, 2")


if __name__ == '__main__':
    main()
