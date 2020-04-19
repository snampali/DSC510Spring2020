'''
Course: DSC510
Assignment: 5.1 Programming Function
Name: David TS
Date: 04/12/2020
Description: Perform various calculations (addition, subtraction, multiplication, division, and average calculation)
'''
# Math Calculation Function
def performCalculation(x):
    while True: #Input Validation
        try:
            b = float(input('Please enter the first number : '))
            break
        except ValueError:
            print("Oops!  That was not valid number.  Try again...")
    while True: #Input Validation
        try:
            c = float(input('Please enter the second number : '))
            break
        except ValueError:
            print("Oops!  That was not valid number.  Try again...")
    if x == 1:
        d = b + c
        msg = 'Addition'
    elif x == 2:
        d = b - c
        msg = 'Substraction'
    elif x == 3:
        d = b * c
        msg = 'Multiplication'
    else:
        d = b / c
        msg = 'Division'
    return d,msg

# Average Calculation Funtion
def calculateAverage():
    mi=1
    nums = ''
    while True: #Input Validation
        try:
            mx = int(input('How many numbers to enter : '))
            break
        except ValueError:
            print("Oops!  That was not valid number.  Try again...")
    if mx < 1: #Error Handling
        print('Please enter valid number !')
        exit(0)
    while mi <= mx:
        while True: #Input Validation
            try:
                y = int(input('Please enter the ' + str(mi) + ' numbers : '))
                break
            except ValueError:
                print("Oops!  That was not valid number.  Try again...")
        nums = nums + str(y)
        mi += 1
    z = 0
    for ci in nums:
        z = z + float(ci)
    average = z / mx
    return average

# Main program
def main():
    while True: #Input Validation
        try:
            op = int(input('Please select the option -> [1] for ADD [2] for SUBSTRACT [3] for MULTIPLY [4] '
                       'for DIVIDE [5] for AVERAGE: '))
            break
        except ValueError:
            print("Oops!  That was not valid number.  Try again...")
    if op == 0 or op > 5: #Error Handling
        print('Please enter valid number (1 - 5) !')
        exit(0)
    elif op <= 4:
        result,msg = performCalculation(op)
        print(msg,'Result is : ',result)
    else:
        print('Calculated Average is : ', calculateAverage())

if __name__ == '__main__':
    main()



