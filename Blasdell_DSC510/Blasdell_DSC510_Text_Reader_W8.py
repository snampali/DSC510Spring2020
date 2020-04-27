import operator

# course: DSC510
# assignment: 8.1
# date: 04/26/20
# name: Blaine Blasdell
# description: Text Reade

# Main Program

# define punctuation
punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''

# Open File
gettysburg_address = open('gettysburg.txt', 'r')

# Create dictionary
word_dictionary = {}
count = 1

# Go through file one line at a time
for line in gettysburg_address:
    #    process_line(line, word_dictionary)
    split_line = line.split()

    for each_word in split_line:

        # remove punctuation from the string
        clean_word = ""
        for char in each_word:
            if char not in punctuations:
                clean_word = clean_word + char

        if clean_word in word_dictionary:
            word_dictionary[clean_word] += 1
        else:
            word_dictionary[clean_word] = 1

# sort
sorted_word_dict = dict(sorted(word_dictionary.items(), key=operator.itemgetter(1), reverse=True))

# formatting
print(format(" Word", "<22")," Count of Word")
print(format("------", "<22"),"---------------")
# print dictionary
for word in sorted_word_dict:
    if word:
        new_count = sorted_word_dict[word]
        print(format(word, " <25"), new_count)


