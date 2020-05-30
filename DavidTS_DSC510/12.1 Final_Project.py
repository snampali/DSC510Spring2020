# Course: DSC510
# Assignment: 12.1 Programming Function
# Name: David TS
# Date: 05/30/2020
# Description: Python program to find current weather details of US city/zip using openweathermap api

import requests


# Get user input of city / zip and validations based on the combination
def city_zip_val(user_pref, lkp_con):
    while True:
        city_zip = input('Please enter the US ' + lkp_con + ' : ')
        if user_pref == '1' and not city_zip.isalpha():
            print('Not a valid City name... try again !')
        elif user_pref == '2' and (not city_zip.isnumeric() or len(city_zip) != 5):
            print('Not a valid Zip code... try again !')
        else:
            return city_zip


# Get the weather data through api call and related validations
def weather_api(query, message):
    try:
        req_weather = requests.get('http://api.openweathermap.org/data/2.5/weather?'
                                   + query + '&APPID=b35975e18dc93725acb092f7272cc6b8&units=imperial')
        w_data = req_weather.json()
        str_length = 32 + len(w_data['name'])
        weather_report(w_data, str_length)
    except EnvironmentError:  # connection failure validation
        print('Connection failure... Please try later !')
        exit()
    except (ValueError, Exception):   # data not found validation
        print(message + ' not found, Please start again !')
        exit()


# To print the weather data to the user based on the requirement
def weather_report(w_data, str_length):
    print('Weather site connection successful !')
    print('*' * str_length)
    print("Current weather condition for " + w_data['name'])
    print('*' * str_length)
    print("Current temperature: {}°F ".format(w_data['main']['temp']))
    print("High Temp: {}°F".format(w_data['main']['temp_max']))
    print("Low Temp: {}°F".format(w_data['main']['temp_min']))
    print("Pressure: {}hPa".format(w_data['main']['pressure']))
    print("Humidity: {}%".format(w_data['main']['humidity']))
    print("Cloud Cover: {}".format(w_data['weather'][0]['description']))
    print('*' * str_length)


# Main function to call the functions and format the input accordingly
def main():
    while True:
        lkp_pref = input('Would you like to lookup weather data by US City or Zip code? Enter 1 for City 2 for Zip: ')
        if lkp_pref == '1':  # call functions based on city name to validate and report the weather data
            city_name = city_zip_val(user_pref='1', lkp_con='City')
            url_input = 'q=' + city_name + ',US'
            print()
            weather_api(url_input, message='City')
        elif lkp_pref == '2':  # call functions based on zip code to validate and report the weather data
            zip_code = city_zip_val(user_pref='2', lkp_con='Zip code')
            url_input = 'zip=' + zip_code + ',US'
            print()
            weather_api(url_input, message='Zip code')
        else:
            print("Oops!  That was not valid number.  Try again...")
        lkp_weather = input('Would you like to perform another weather lookup? (Y/N): ')
        if lkp_weather.upper() != 'Y':
            print('Thank You !')
            return False


# Call main function
if __name__ == '__main__':
    main()
