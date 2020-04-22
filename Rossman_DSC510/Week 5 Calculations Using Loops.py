"""
Calculations Using Loops

Institution: Bellevue University
Course: DSC510
Assignment: 5.1
Date: 19 Apr 2020
Name: Alfred Rossman
Interpreter: Python 3.8
"""


def performCalculation(operation):
# User Input of Two Numeric Operands, Perform {+, -, *, /} Calculation

    print('Enter Numeric Data - Real or Integer only, Result will be Real')
    operand1 = float(input('Enter Operand 1: '))
    operand2 = float(input('Enter Operand 2: '))
    if operation == '+': result = operand1 + operand2
    if operation == '-': result = operand1 - operand2
    if operation == '*': result = operand1 * operand2
    if operation == '/': result = operand1 / operand2
    return result

def calculateAverage():
# Average of Inputted Values, Total Number of Entries Must Be Inputted

    numValues = int(input('Enter Number of Values (Real or Integer) to be Averaged: '))
    total = 0
    for i in range(numValues):
        print('#', i + 1, 'Enter Value: ')
        value = float(input())
        total += value
    return (total / numValues)


# (1) Perform inputted binary Add, Subtract, Multiply, or Divide operations (TAB completes program)
# (2) Calculate Arithmetic Mean (Average) of multiple values
# (3) Print Results
# NOTE: Minimal verifications of validity of user inputted data

operation = ' '
while operation != '\t':
    operation = input('\nInput Operator Symbol (Add +, Subtract -, Multiply *, Divide /) or Enter TAB Key to Terminate: ')
    if operation == '\t':
        break

    result = performCalculation(operation)
    print('Result of ', operation, 'is: ', result)

    average = calculateAverage()
    print('Arithmetic Mean = ', average)
