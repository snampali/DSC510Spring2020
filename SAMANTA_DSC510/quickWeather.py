# course: DSC510
# assignment: 12.1 - Final Project
# date: 05/30/2020
# name: Arindam Samanta
'''
description: This program is an application that interacts with a webservice in order to obtain weather data.
It will prompt the user for their city or zip code and request weather forecast data from OpenWeatherMap.
The program will display the weather information in a READABLE format to the user.
'''
# !python3


import requests


# This below function takes in an input and verifies if it is an integer or not


def is_number(n):
    try:
        int(n)  # type-casting the string to 'integer',
        # if string is not a valid integer it will
        # raise value error
    except ValueError:
        return False
    return True


# This below function will verify (basic verification) of the city name and zip codes entered by the user


def verify_city_zip(entry, opt):
    if opt == 1:  # Entry is a city name
        cn = entry
        for each_letter in cn:
            if is_number(each_letter):
                print('City name cannot have numbers:' + entry)
                return False
        return True
    elif opt == 2:  # Entry is a zip code
        zip_code = entry
        for each_letter in zip_code:
            if not is_number(each_letter):
                print('zip code should have numbers :' + entry)
                return False
        if len(zip_code) != 5:
            print('Enter a valid zip code(5 number) :' + entry)
            return False
        return True


# This validate_input function is to determine if the user choice is for city name or zip code and returns the choice


def validate_input(in_str):
    user_input = in_str
    if is_number(user_input):
        choice = int(user_input)
        if choice in (1, 2, 3):
            return choice
        else:
            print('Invalid choice of number :' + in_str)
            return choice
    else:
        if isinstance(user_input, (str)):
            print('Oops! Invalid entry: ' + in_str)
            return 4


# The below process_api function generates the api and gets the output from the Rest API call
# The return value is in json format.
# If the call succeeds then pretty print function is called to print the output


def process_api(inp, opt):
    api_key = '6625186c92cf439ddeef88b17b89dc03'
    country = 'us'  # Country code: us
    usr_inp = inp
    if opt == 1:  # City name search
        api_base_url = 'http://api.openweathermap.org/data/2.5/weather?q='
    else:  # zip code search
        api_base_url = 'http://api.openweathermap.org/data/2.5/weather?zip='

    final_url = '{bu}{inp_n},{c}&appid={api}&units=imperial'.format(inp_n=usr_inp, c=country, api=api_key,
                                                                    bu=api_base_url)

    try:
        response = requests.get(final_url)  # Getting the response from the request
        response.raise_for_status()
        print('Connection Successful!')
        pretty_print(response.json())
    except EnvironmentError:
        print('Connection not successful. Check url! ' + final_url)
    except ValueError:
        print('User Input :' + inp + ' not found. Please try again !')


# This is the pretty_print function to print the output in the readable format


def pretty_print(json_input):
    print('*' * 32 + '*' * len(json_input["name"]))
    print('Current Weather Conditions for {}'.format(json_input["name"]))
    print('*' * 32 + '*' * len(json_input["name"]))

    print('Current Temp:'+' '* 5 +'{}F'.format(json_input["main"]["temp"]))
    print('High Temp:'+' '* 8 +'{}F'.format(json_input["main"]["temp_max"]))
    print('Low Temp:'+' ' * 8 + ' {}F'.format(json_input["main"]["temp_min"]))
    print('Pressure:'+' '* 8 + ' {}hPa'.format(json_input["main"]["pressure"]))
    print('Humidity:'+ ' ' * 8 + ' {}%'.format(json_input["main"]["humidity"]))
    print('Cloud Cover:'+' ' * 5 +' {}'.format(json_input["weather"][0]["description"]))

    print('*' * 32 + '*' * len(json_input["name"]))


#  This is the main function.


def main():
    user_input = input('Would you like to lookup weather data by US City or zip code? Enter 1 for US city 2 for '
                       'zip 3 to exit:')
    user_choice = validate_input(user_input)

    while user_choice > 0:
        if user_choice == 1:
            ask_city = input('Please enter the city name: ')
            if verify_city_zip(ask_city, user_choice):
                process_api(ask_city, user_choice)
            user_choice = 0

        elif user_choice == 2:
            ask_zip = input('Please enter the zip code: ')
            if verify_city_zip(ask_zip, user_choice):
                process_api(ask_zip, user_choice)
            user_choice = 0

        elif user_choice == 3:
            print('Good Bye!')
            exit()

        user_input = input('Would you like to do another lookup of weather data? 1 for US city 2 for zip 3 to exit:')
        user_choice = validate_input(user_input)


# Checking to see if the main function exists before calling
if __name__ == "__main__":
    main()
