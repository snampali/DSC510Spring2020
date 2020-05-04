"""
Course: DSC510
Assignment: 8.1 Programming Assignment
Name: David TS
Date: 05/03/2020
Description: Calculate the total words, and output the number of occurrences of each word in the file
"""
import string # for string operations

# To get the words and strip off characters and split the words
def process_line(line, word_count_dict):
    line = line.strip()
    word_list = line.split()
    for word in word_list:
        if word != '--' :
            word = word.lower()
            word = word.strip()
            word = word.strip(string.punctuation)
            add_word(word, word_count_dict)

# To create the dictionary with all the words from the file
def add_word(word, word_count_dict):
    if word in word_count_dict:
        word_count_dict[word] += 1
    else:
        word_count_dict[word] = 1

# To format the output and print in specific format
def pretty_print(word_cound_dict):
    value_key_list = []
    for key, val in word_cound_dict.items():
        value_key_list.append((val,key))
    value_key_list.sort(reverse=True)
    print(' '*21)
    print('{:11s}{:11s}'.format("Word","Count"))
    print('-'*20)
    for val, key in value_key_list:
        print('{:12s} {:<3d}'.format(key,val))

# Main function to open the file and call the function to print the output
def main():
    word_count_dict={}
    try: # Error handling for file missing
        gba_file = open('Gettysburg.txt', 'r')
    except FileNotFoundError as e:
        print(e)
    for line in gba_file:
        process_line(line, word_count_dict)
    print(' ' * 21)
    print('Word count of the file :' , len(word_count_dict))
    pretty_print(word_count_dict)

# To call main function
if __name__ == '__main__':
    main()
