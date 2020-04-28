# Title     : Week6 - Programming Assignment
# Author    : Vikas Ranjan
# Date      : 4/19/2020
# Purpose   : This week we will create a program which works with lists. Your goal is to create a program which contains a list of temperatures. Your program will populate the list based upon user input. Your program will determine the number of temperatures in the program, determine the largest temperature, and the smallest temperature.
#               Your program must have a header. Use the programming style guide for guidance.
#               Create an empty list called temperatures.
#               Allow the user to input a series of temperatures along with a sentinel value which will stop the user input.
#               Evaluate the temperature list to determine the largest and smallest temperature.
#               Print the largest temperature.
#               Print the smallest temperature.
#               Print a message tells the user how many temperatures are in the list.

def main():
    # Create an empty list
    temperatures = []
    # Accept user inputs and move them into list
    acceptUserInputs(temperatures)
    # Print results
    printResults(temperatures)

def acceptUserInputs(temperatures):
    temp = 0
    while temp != "q" or temp != "Q":
        while True:
            temp = input("Enter the temperature, use q to stop: \n")
            try:
                temp = int(temp)
                break
            except ValueError:
                try:
                    temp = float(temp)
                    break
                except ValueError:
                    if temp.upper() == "Q":
                        break

                    print("Please check and enter a valid temperature!\n")
        # Break out of the loop, when user inpus "Q" or "q"
        if temp == "q" or temp == "Q":
            break
        temperatures.append(temp)

def printResults(temperatures):
    # Find min & max of the temperatures list#
    print("largest temperature entered by the user is", str(max(temperatures)))
    print("Smallest temperature entered by the user is", str(min(temperatures)))
    print("Total count of valid temperature inputs in the list is", str(len(temperatures)))

if __name__ == '__main__':
    main()

