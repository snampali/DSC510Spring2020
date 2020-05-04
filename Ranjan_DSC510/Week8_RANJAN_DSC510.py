# Title     : Week8 - Programming Assignment
# Author    : Vikas Ranjan
# Date      : 5/2/2020
# Purpose   : We will create a program which performs three essential operations. It will process this .txt file: Gettysburg.txt.
#             Calculate the total words, and output the number of occurrences of each word in the file.
#                   Open the file and process each line.
#                   Either add each word to the dictionary with a frequency of 1 or update the word’s count by 1.
#                   Nicely print the output, in this case from high to low frequency. You should use string formatting for this. (See discussion 8.3).
#             We want to achieve each major goal with a function (one function, one action). We can find four functions that need to be created.
#                   add_word: Add each word to the dictionary. Parameters are the word and a dictionary. No return value.
#                   Process_line: There is some work to be done to process the line: strip off various characters, split out the words, and so on. Parameters are a line and the dictionary. It calls the function add word with each processed word. No return value.
#                   Pretty_print: Because formatted printing can be messy and often particular to each situation (meaning that we might need to modify it later), we separated out the printing function. The parameter is a dictionary. No return value.
#                   main: We will use a main function as the main program. As usual, it will open the file and call process_line on each line. When finished, it will call pretty_print to print the dictionary.
#             In the main function, you will need to open the file. We will cover more regarding opening of files next week but I wanted to provide you with the block of code you will utilize to open the file, see below.

import operator
import re

def main():
    # Create an empty Dictionary
    gettysburg_dict = {}

    # Open Lincoln's gettysburg address file and read gettysburg address file, one line at a time
    gettysburg_lincoln = open("C:/Users/F6PDP2A/PycharmProjects/PythonCourse/gettysburg.txt", 'r')
    for line in gettysburg_lincoln:
        if len(line.strip()) != 0:
            process_line(line, gettysburg_dict)

    # Invoke Pretty_print to print the contents of the dictionary
    pretty_print(gettysburg_dict)

def process_line(line, gettysburg_dict):
    # Remove special characters from the line string
    line = re.sub("[^0-9a-zA-Z']+", ' ', line).rstrip()
    line_list = line.split(' ')
    for word in line_list:
        if word.isdigit() == False and len(word) > 0:
            add_word(word, gettysburg_dict)

def add_word(word, gettysburg_dict):
    if word in gettysburg_dict:
        gettysburg_dict[word] += 1
    else:
        gettysburg_dict[word] = 1

def pretty_print(gettysburg_dict):
    # Print length of dictionary
    print("Length of the dictionary: {}".format(len(gettysburg_dict)))

    print('{0} \t\t\t {1}'.format('Word', 'Count'))
    print(format('-----------------------'))

    # Sort and print the dictionary
    for key, value in sorted(gettysburg_dict.items(), key=operator.itemgetter(1), reverse=True):
        print(format(key, " <18"), value)

if __name__ == '__main__':
    main()
