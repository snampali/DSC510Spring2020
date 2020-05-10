# course: DSC510
# assignment: 9.1
# date: 05/03/20
# name: Blaine Blasdell
# description: Text Reader - With File Save

import string


def process_file(word_dictionary, file_out):
    with open(file_out, 'a') as fo:
        # sort dictionary
        dictlist = []
        for key, value in word_dictionary.items():
            temp = [value, key]
            dictlist.append(temp)
        dictlist.sort(reverse=True)

        # formatting and header
        fo.write('\n')
        output_string = '{:22s}{:22s}'.format('Word', 'Count')
        fo.write(output_string)
        fo.write('\n')
        output_string = '{:22s}{:22s}'.format('----', '-----')
        fo.write(output_string)
        fo.write(' '*21)
        fo.write('\n')
        # print dictionary in columns
        for value, key in dictlist:
            output_string = '{:23s}{:<3d}'.format(key, value)
            fo.write(output_string)
            fo.write('\n')


# Function to print
def pretty_print(word_dictionary):
    # sort dictionary
    dictlist = []
    for key, value in word_dictionary.items():
        temp = [value, key]
        dictlist.append(temp)
    dictlist.sort(reverse=True)

    # formatting and header
    print(format(" Word", "<22"), " Count of Word")
    print(format("------", "<22"), "---------------")
    # print dictionary in columns
    for value, key in dictlist:
        print(format(key, ' <27'), value)


# Add Word to Dictionary
def add_word(new_word, word_dictionary):  # Get the new word and current dictionary
    if new_word in word_dictionary:
        word_dictionary[new_word] += 1  # if in dictionary  - increment count
    else:
        word_dictionary[new_word] = 1  # if not in dictionary - add with count of 1


# Process Line Function
def process_line(rec_line, word_dictionary):
    # Split Line
    split_line = rec_line.split()

    for each_word in split_line:  # Loop through each word in line, clean, call add to dictionary
        each_word = each_word.strip(string.punctuation)  # Remove punctuation
        each_word = each_word.rstrip()  # Strip any blank spaces
        each_word = each_word.lower()  # convert to lower space

        if len(each_word) > 0:  # ignore blank lines
            if each_word != "--":
                add_word(each_word, word_dictionary)  # call add word to dictionary function


# Main Function
def main():
    import pathlib

    # Get name of file
    file_name = input("What is the name of the file to import: ")
    # set file and path
    file = pathlib.Path(file_name)

    # Check to ensure file exists
    if file.exists():
        print("Opening File....")
        open_file = open(file, 'r')

        # Create dictionary
        word_dictionary = {}

        # Go through file one line at a time
        for line in open_file:
            process_line(line, word_dictionary)  # process each line

        # Length of dictionary
        total_words = str(len(word_dictionary))
        # Get name of file
        file_name_out = input("What is the name of the file to export: ")
        # set file and path
        file_out = pathlib.Path(file_name_out)

        with open(file_out, 'w') as fo:
            output_string = "There are {} words in the file.".format(total_words)
            fo.write('\r')
            fo.write(output_string)
            fo.write('\r')

        pretty_print(word_dictionary)  # Call Print Function
        process_file(word_dictionary, file_out)
    else:
        print("File not exist - Please ensure you enter a valid file.")


# Start of Program
# Validate Main Function exists before calling
if __name__ == "__main__":
    main()
# End of Program
