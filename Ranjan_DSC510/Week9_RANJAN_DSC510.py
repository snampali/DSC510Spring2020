# Title     : Week9 - Programming Assignment
# Author    : Vikas Ranjan
# Date      : 5/9/2020
# Purpose   : For this week we will modify our Gettysburg processing program from week 8 in order to generate a text file
#             from the output rather than printing to the screen. Your program should have a new function called process_file
#             which prints to the file (this method should almost be the same as the pretty_print function from last week.
#             Keep in mind that we have print statements in main as well. Your program must modify the print statements
#             from main as well.
#
#                   Your program must have a header. Use the programming style guide for guidance.
#                   Create a new function called process_fie. This function will perform the same operations as pretty_print from week 8 however it will print to a file instead of to the screen.
#                   Modify your main method to print the length of the dictionary to the file as opposed to the screen.
#                   This will require that you open the file twice. Once in main and once in process_file.
#                   Prompt the user for the filename they wish to use to generate the report.
#                   Use the filename specified by the user to write the file.
#                   This will require you to pass the file as an additional parameter to your new process_file function.

import operator
import re

def main():
    # Create an empty Dictionary
    gettysburg_dict = {}

    # Open Lincoln's gettysburg address file and read gettysburg address file, one line at a time
    gettysburg_lincoln = open("gettysburg.txt", 'r')
    for line in gettysburg_lincoln:
        if len(line.strip()) != 0:
            process_line(line, gettysburg_dict)
    gettysburg_lincoln.close()

    while True:
        output_file = input("Please enter a valid file name (with .txt extension) to generate the output report: ")
        try:
            if output_file.lower().endswith('.txt'):
                break
        except:
             print("Please check and enter a valid text file name!\n")
    # Invoke process_file to print the contents of the dictionary to the file
    process_file(gettysburg_dict, output_file)

def process_line(line, gettysburg_dict):
    # Remove special characters from the line string
    line = re.sub("[^0-9a-zA-Z']+", ' ', line).rstrip()
    line_list = line.split(' ')
    for word in line_list:
        if word != '--' :
            add_word(word.lower(), gettysburg_dict)

def add_word(word, gettysburg_dict):
    if word in gettysburg_dict:
        gettysburg_dict[word] += 1
    else:
        gettysburg_dict[word] = 1

def process_file(gettysburg_dict, output_file):
    # Create the file handler with open
    new_output_file = open(output_file, 'w+')
    # Write length and header data to the file
    new_output_file.write("Length of the dictionary: {} \n\n".format(len(gettysburg_dict)))
    new_output_file.write('{0} \t\t\t {1} \n'.format('Word', 'Count'))
    new_output_file.write(format('------------------------------ \n'))

    # Sort and print the dictionary data into the file
    for key, value in sorted(gettysburg_dict.items(), key=operator.itemgetter(1), reverse=True):
        new_output_file.write('{0: <25} {1} \n'.format(key, value))
    new_output_file.close()

if __name__ == '__main__':
    main()
