# File :    Gunasekaran_DS510_week9_1.py
# Name :    Ragunath Gunasekaran
# Date :    05/08/2020
# Course :  DSC-510 - Introduction to Programming
# Assignment :
#           Open the file and process each line.
#           Either add each word to the dictionary with a frequency of 1
#            or update the word’s count by 1.
#           process_file, prints to the file in this case from high to low frequency
import string
import datetime


def process_line(line, word_dict):
    # Remove the leading spaces and newline character
    line = line.strip()

    # Convert the characters in line to
    # lowercase to avoid case mismatch
    line = line.lower()

    # Remove the punctuation marks from the line
    line = line.translate(line.maketrans("", "", string.punctuation))

    # Split the line into words
    words = line.split(" ")
    process_add(words, word_dict)


def process_add(words, word_dict):
    for word in words:
        # Check if the word is empty. If empty, we need ignore
        if word == "":
            continue
        # Check if the word is already in dictionary
        elif word.strip() in word_dict and word != "":
            # Increment count of word by 1
            word_dict[word] = word_dict[word] + 1
        else:
            # Add the word to dictionary with count 1
            word_dict[word] = 1


# Print the contents of dictionary
def format_print(word_dict, word_num):
    # Print the contents of dictionary
    print("{:<20} {:<15} ".format('Word', 'Count'))
    print("---------------------------")
    # for key in list((d.keys())):
    for key in sorted(word_dict, key=word_dict.get, reverse=True):
        # print(key, ":", d[key])
        print("{:<20} {:<15} ".format(key, word_dict[key]))


# write the contents of dictionary into output file
def process_file(word_dict, outputfile_name):
    # Print the contents of dictionary
    output_file = open(outputfile_name, "w")  # write mode
    output_file.write("---------------------------" + "\n")
    output_file.write("---------------------------" + "\n")
    output_file.write("{:<20} {:<15} ".format('Word', 'Count') + "\n")
    output_file.write("---------------------------" + "\n")

    for key in sorted(word_dict, key=word_dict.get, reverse=True):
        # print(key, ":", d[key])
        ## print("{:<20} {:<15} ".format(key, word_dict[key]))
        # Write-Overwrites
        output_file.write("{:<20} {:<15} ".format(key, word_dict[key]) + "\n")
    output_file.close()


def main():
    # Receive the file name to write the output
    outputfile_name = input("enter your output file name :")
    datevalue = datetime.datetime.now()
    # Adding the date value after the output file name
    outputfile_name = outputfile_name + "_" + datevalue.strftime("%d %B %Y") + ".txt"
    # Open the file in read mode
    input_file = open("gettysburg.txt", "r")
    # Create an empty dictionary
    word_dict = dict()
    # Loop through each line of the file
    for line in input_file:
        process_line(line, word_dict)
    input_file.close()
    # Write the length of the dict in the outputfile
    output_file = open(outputfile_name, "w")  # write mode
    output_file.write('Length of the dictionary :' + str(len(word_dict)) + "\n")


    # call the processfile method by passing dict, filename to print the words and length of dict
    process_file(word_dict, outputfile_name)
    # call the format print method to print the words and length of dict
    format_print(word_dict, len(word_dict))


if __name__ == '__main__':
    main()
