# Title     : Week5 - Programming Assignment
# Author    : Vikas Ranjan
# Date      : 4/12/2020
# Purpose   : Your program must have a header. Use the programming style guide for guidance.
#               This program will perform various calculations (addition, subtraction, multiplication, division, and average calculation)
#               This program will contain a variety of loops and functions.
#               The program will add, subtract, multiply, divide two numbers and provide the average of multiple numbers input by the user.
#               Define a function named performCalculation which takes one parameter. The parameter will be the operation being performed (+, -, *, /).
#                   This function will perform the given prompt the user for two numbers then perform the expected operation depending on the parameter that's passed into the function.
#                   This function will print the calculated value for the end user.
#               Define a function named calculateAverage which takes no parameters.
#                   This function will ask the user how many numbers they wish to input.
#                   This function will use the number of times to run the program within a for loop in order to calculate the total and average.
#                   This function will print the calculated average.
#               This program will have a main section which contains a while loop. The while loop will be used to allow the user to run the program until they enter a value which ends the loop.
#               The main program should prompt the user for the operation they wish to perform.
#               The main program should evaluate the entered data using if statements.
#               The main program should call the necessary function to perform the calculation.

def main():
    continueExecution = 'Y'
    while continueExecution == 'Y':
        operation = input("Enter the operation to be performed! \n")
        performCalculation(operation)
        calculateAverage()
        continueExecution = input("Do you still want to continue, Y or N \n")
        if continueExecution.upper() == 'Y':
            continueExecution = 'Y'
        elif continueExecution.upper() == 'N':
            continueExecution = 'N'

def performCalculation(operation):
    # Prompt user to input 1st number.
    while True:
        number1 = input("Enter 1st number. \n")
        try:
            number1 = int(number1)
            break
        except ValueError:
            try:
                number1 = float(number1)
                break
            except ValueError:
                print("Please check and enter number1!\n")
    # Prompt user to input 2nd number.
    while True:
        number2 = input("Enter 2nd number. \n")
        try:
            number2 = int(number2)
            break
        except ValueError:
            try:
                number2 = float(number2)
                break
            except *ValueError:
                print("Please check and enter number2!\n")

    if operation == '+':
        result = number1 + number2
    elif operation == '-':
        result = number1 - number2
    elif operation == '*':
        result = number1 * number2
    elif operation == '/':
        result = number1 / number2
    print("Result of the calculation of " + str(number1) + " " + str(operation) + " " + str(number2) + " is " + str(result) + "\n")

def calculateAverage():
    # Ask the user how many numbers they wish to input.
    totalOfNumbers = 0
    countofnumbers = int(input("How many mumbers you wish to input? \n"))
    for count in range(countofnumbers):
        while True:
            number = input("Enter number - ")
            try:
                number = int(number)
                break
            except ValueError:
                try:
                    number = float(number)
                    break
                except ValueError:
                    print("Please check and enter number!\n")

        totalOfNumbers = totalOfNumbers + number
    average = totalOfNumbers/countofnumbers
    print("The sum total of the numbers is " + str(totalOfNumbers) + " and average of the numbers is " + str(average) + "\n")

if __name__ == '__main__':
    main()
