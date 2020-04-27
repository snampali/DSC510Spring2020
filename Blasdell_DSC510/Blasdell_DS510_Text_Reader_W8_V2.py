import operator


# course: DSC510
# assignment: 8.1
# date: 04/26/20
# name: Blaine Blasdell
# description: Text

# Function to print
def pretty_print(final_dict):
    # sort
    sorted_word_dict = dict(sorted(final_dict.items(), key=operator.itemgetter(1), reverse=True))

    # Length of dictionary
    print(len(sorted_word_dict))

    # formatting
    print(format(" Word", "<22")," Count of Word")
    print(format("------", "<22"),"---------------")
    # print dictionary
    for word in sorted_word_dict:
        if word:
            new_count = sorted_word_dict[word]
            print(format(word, " <25"), new_count)


# Function to check for a number
def isitanumber(test_v):
    try:
        float(test_v)
        return True
    except ValueError:
        pass

    return False


# Add Word to Dictionary
def add_word(new_word, new_dict):
    if new_word in new_dict:
        new_dict[new_word] += 1
    else:
        new_dict[new_word] = 1

    return new_dict


# Process Line Function
def process_line(rec_line, rec_dict):
    # define punctuation
    punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''

    # Split Line
    split_line = rec_line.split()

    count = 0

    for each_word in split_line:

        # remove punctuation from the string
        clean_word = ""
        for char in each_word:
            if char not in punctuations:
                clean_word = clean_word + char

        temp_word = clean_word.rstrip()
        test_for_number = isitanumber(temp_word)

        if len(temp_word) > 0:
            if not test_for_number:
                if count == 0:
                    rev_dict = add_word(clean_word, rec_dict)
                    rec_dict = rev_dict
                else:
                    rev_dict = add_word(clean_word, rec_dict)
                    rec_dict = rev_dict
                count = count + 1

    return rec_dict


# Main Function
def main():
    gettysburg_address = open('gettysburg.txt', 'r')  # open File

    # Create dictionary
    word_dictionary = {}
    temp_dict = {}

    # Go through file one line at a time
    for line in gettysburg_address:
        temp_dict = process_line(line, word_dictionary)
        word_dictionary = temp_dict

    pretty_print(word_dictionary)




# Start of Program
main()

# End of Program
