# Gettysburg Address Word Dictionary

def main():

    """
Institution: Bellevue University
Course: DSC510
Assignment: 8.1
Date: 10 May 2020
Name: Alfred Rossman
Interpreter: Python 3.8
    """
# Print docstring header
print(main.__doc__)

#! python3
# Open 'gettysburg.txt' in local directory for read-only
# Count the total number of words and the occurrences of each specific word (dates at present are words)
# Print results in stdout in a formatted (pretty), alphabetical output

import os
import string
import pprint
path = os.getcwd()
print ('Path: ', path)
gba_file = open('gettysburg.txt', 'r')

# Add each word to wordDict
def add_word(newWord, wordDict):
    if newWord in wordDict:
        wordDict[newWord] += 1
    else:
        wordDict[newWord] = 1

    return None

# Split words by whitespace (blanks, tabs, newlines), strip off excess whitespace and punctuation, convert to lower case
def process_line(textLine, wordDict):
    eachLine = textLine.split()
    for eachWord in eachLine:
        eachWord = eachWord.strip(string.punctuation)
        eachWord = eachWord.rstrip()
        eachWord = eachWord.lower()
        if len(eachWord) > 0:               # zero length words don't count
            add_word(eachWord, wordDict)

    return None

#Print dictionary in readable format (alphabetically sorted)
def pretty_print(printDict):
    pprint.pprint(printDict)

    return None

#Main program functionality
wordDict = {}

for line in gba_file:
    process_line(line, wordDict)

print('\nTotal Number of Words: ',len(wordDict), '\n')
pretty_print(wordDict)

#End of Program

