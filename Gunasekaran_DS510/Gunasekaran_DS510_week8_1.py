# File :    Gunasekaran_DS510_week8_1.py
# Name :    Ragunath Gunasekaran
# Date :    05/01/2020
# Course :  DSC-510 - Introduction to Programming
# Assignment :
#           Open the file and process each line.
#           Either add each word to the dictionary with a frequency of 1
#            or update the word’s count by 1.
#           Print the output, in this case from high to low frequency
import string


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
        # Check if the word is already in dictionary
        if word in word_dict:
            # Increment count of word by 1
            word_dict[word] = word_dict[word] + 1
        else:
            # Add the word to dictionary with count 1
            word_dict[word] = 1


# Print the contents of dictionary
def format_print(word_dict, word_num):
    # Print the contents of dictionary
    print('Length of the dictionary :', len(word_dict))
    print("{:<20} {:<15} ".format('Word', 'Count'))
    print("---------------------------")
    # for key in list((d.keys())):
    for key in sorted(word_dict, key=word_dict.get, reverse=True):
        # print(key, ":", d[key])
        print("{:<20} {:<15} ".format(key, word_dict[key]))


def main():
    # Open the file in read mode
    gba_file = open("D:\Python\gettysburg.txt", "r")
    # Create an empty dictionary
    word_dict = dict()
    # Loop through each line of the file
    for line in gba_file:
        process_line(line, word_dict)
    gba_file.close()
    format_print(word_dict, len(word_dict))


if __name__ == '__main__':
    main()
