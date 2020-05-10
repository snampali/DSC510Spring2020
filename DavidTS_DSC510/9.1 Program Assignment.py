"""
Course: DSC510
Assignment: 9.1 Programming Assignment
Name: David TS
Date: 05/10/2020
Description: Calculate the total words, and write the number of occurrences of each word in a file
"""
import string # for string operations
import os # for file operations

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

# To write the output in a file
def process_file(word_count_dict, output_fname):
    if os.path.isfile(output_fname): # file existence validation
        value_key_list = []
        for key, val in word_count_dict.items(): #update the dictionary with values
            value_key_list.append((val,key))
        value_key_list.sort(reverse=True)
        with open(output_fname, 'a') as output_report: #update the output reports
            output_report.write('{:11s}{:11s}'.format("Word","Count") + '\n')
            output_report.write('-'*20 + '\n')
            for val, key in value_key_list:
                output_report.write('{:12s} {:<3d}'.format(key,val) + '\n')
    else:
        print(output_fname,' file not found')

# Main function to open the file and call the function to print the output
def main():
    word_count_dict={}
    try: # Error handling for file missing
        read_file = open('Gettysburg.txt', 'r')
    except FileNotFoundError as file_error:
        print(file_error)
    except Exception as other_error:
        print(other_error)
    else:
        for line in read_file:
            process_line(line, word_count_dict)
        output_fname = input('Please enter the output report name : ') #to get the output report name
        with open(output_fname, 'w') as output_report: #open the output report in write mode to update
            output_report.write(str('Number of words in the file :'))
            output_report.write(str(len(word_count_dict)) + '\n')
            output_report.write(' ' * 21 + '\n')
        process_file(word_count_dict, output_fname)
        read_file.close()
# To call main function
if __name__ == '__main__':
    main()
