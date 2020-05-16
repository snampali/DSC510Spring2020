# course: DSC510
# assignment: 10.1
# date: 05/03/20
# name: Blaine Blasdell
# description: Chuck Norris Jokes - API

import requests
import json


# User Input Function
def user_input(dis_message):  # function to get user input and check for error
    while True:
        try:
            user_response = (input(dis_message))
        except ValueError:
            print('Please enter a valid input:')
            continue
        else:
            return user_response.lower()
            break


# Created a function to display welcome and closing messages- receive message
def print_message(u_message):
    print('\r')
    print('-' * 45)  # Formatting
    print(u_message)  # Print Message
    print('-' * 45)
    print('\r')


# Function to print joke - receive Joke
def print_joke(joke):
    print('\r')
    print('Joke:\r')
    print(joke)  # Print Joke
    print('\r')


# Main Function
def main():
    next_joke = True  # Set Flag for looping
    url = "https://api.chucknorris.io/jokes/random"  # URL for Chuck Norris Jokes

    # Set params for response call
    querystring = ""
    headers = {'cahce-control': 'no-cache'}

    # Print Welcome Message
    print_message('\rWelcome to the Chuck Norris Joke Generator\r')

    # While loop for continued joeks
    while next_joke:
        response = requests.request("GET", url, headers=headers, params=querystring)  # Query API
        parsed_joke = json.loads(response.text)  # Parse JSON joke to parts

        print_joke(parsed_joke["value"])  # Get Joke from JSON

        # Call user input
        u_response = user_input('\rWould you like another joke (Y/N): ')

        # Check User Input for lower Y
        if u_response != 'y':
            next_joke = False

    print_message('\rThank you for visiting Chuck Norris !!!\r')


# Start of Program
# Validate Main Function exists before calling
if __name__ == "__main__":
    main()
# End of Program
