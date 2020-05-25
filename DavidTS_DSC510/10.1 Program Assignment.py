"""
Course: DSC510
Assignment: 10.1 Programming Assignment
Name: David TS
Date: 05/17/2020
Description: To print Chuck Norris Jokes based on the user input along with welcome message, error and exception handling
"""
import requests
import json
import textwrap


# Format the output for better look and feel
def pretty_print(joke_text):
    joke_len = 100
    output_format = textwrap.TextWrapper(drop_whitespace=True, width=joke_len)
    lines = output_format.wrap(text=joke_text)
    for line in lines:
        print(line)
    print('-' * joke_len)


# main function to get the input from the user
def main():
    user_input = 'Y'
    input_msg_txt = 'Do you wish to read Chuck Norris Joke? (Y/N): '
    print('\n' + '*' * 30 + "Welcome to Chuck Norris Jokes collection" + '*' * 30 + '\n')  # welcome message to the user
    # loop to call norris_joke() function and print the joke multiple times
    while user_input.upper() == 'Y':
        user_input = input(input_msg_txt)  # user input for getting joke
        get_data = requests.get('https://api.chucknorris.io/jokes/random')
        if get_data.status_code != 200:  # error handling during api call
            return print('Connection Unsuccessful. Please try again after sometime.')
        elif user_input.upper() == 'Y':  # validation for correct entry
            output_data = json.loads(get_data.text)
            joke_text = output_data["value"]
            print('\n' + '-' * 40 + 'Chuck Norris Joke' + '-' * 43)
            pretty_print(joke_text)
            input_msg_txt = 'Would you like to read another Chuck Norris Joke? (Y/N): '
        elif user_input.upper() == 'N':
            return print('Thank You !')
        else:
            print('Invalid entry, Please try again !')
            main()


if __name__ == '__main__':
    main()
