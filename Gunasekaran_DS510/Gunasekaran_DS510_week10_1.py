# File :    Gunasekaran_DS510_week10_1.py
# Name :    Ragunath Gunasekaran
# Date :    05/16/2020
# Course :  DSC-510 - Introduction to Programming
# Assignment :
# Create a program which uses the Request library to make
#   a GET request of the following API: Chuck Norris Jokes.
# The program will receive a JSON response which includes various pieces of data.
#   You should parse the JSON data to obtain the “value” key.
#   The data associated with the value key should be displayed for the user (i.e., the joke).
# Program should allow the user to request a Chuck Norris joke as many times as they would like.

import requests
import datetime
from requests.exceptions import HTTPError


# get Joke method will call API and get the values in JSON and display only value
def get_joke():
    try:
        # get the API value into response
        response = requests.get('https://api.chucknorris.io/jokes/random')
        # returns an HTTPError object if an error has occurred during the process
        response.raise_for_status()
        # convert response details into jsonresponse as JSON format
        jsonresponse = response.json()
        # print only value in the JSON
        print(jsonresponse.get("value"))
    # Exception Handling
    except HTTPError as http_err:
        print(f'HTTP error occurred: {http_err}')
    except Exception as err:
        print(f'Other than HTTP error occurred: {err}')


# Format Print method to print the jokes from url
def format_print():
    # Iscontinue, IsvalidInput are used to control the flow
    Iscontinue = True
    IsvalidInput = True
    # Loop continue until the user want to see Jokes or exit
    while (Iscontinue):
        if (IsvalidInput):
            # Calling the Joke from API
            get_joke()
        print("------------------------------------------")
        result = input("Do you want to see another Joke ? \n")
        # Verify the input Sting. we used to lower to make sure we can handle the Case sensitive case
        if (result.lower() == 'yes' or result.lower() == 'y'):
            Iscontinue = True
            IsvalidInput = True
        elif (result.lower() == 'no' or result.lower() == 'n'):
            Iscontinue = False
            IsvalidInput = True
            print("Thank You for using this Application!")
        else:
            print("Invalid Input. Please enter Yes or Y to view another Joke. No or N to exit from the application")
            Iscontinue = True
            IsvalidInput = False


def main():
    now = datetime.datetime.now()
    print("Welcome to the API Integration Program :  Chuck Norris Jokes")
    print('Date : ' + now.strftime("%Y-%m-%d %H:%M:%S"))  # printing date & time
    print("------------------------------------------")
    # Calling Format Print method to print the Jokes
    format_print()


if __name__ == '__main__':
    main()
