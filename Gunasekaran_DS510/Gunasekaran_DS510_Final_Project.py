# File :    Gunasekaran_DS510_FinalProject.py
# Name :    Ragunath Gunasekaran
# Date :    05/30/2020
# Course :  DSC-510 - Introduction to Programming
# Assignment :
#     Created a header for this Program.
#     Created new API - # api_key = "09d020dd8193c479bf9e062588c60cfa"
#     Created a Python Application which asks the user for their zip code or city.
#     Used the zip code or city name in order to obtain weather forecast data from OpenWeatherMap.
#     Displayed the weather forecast in a readable format to the user.
#     Commented within the application where appropriate in order to document what the program is doing.
#     Used functions including a main function.
#     Allowed the user to run the program multiple times to allow them to look up weather conditions
#          for multiple locations.
#     Validated whether the user entered valid data.
#       If valid data isn’t presented notify the user.
#     Used the Requests library in order to request data from the webservice.
#     Used Try blocks to ensure that your request was successful.
#       If the connection was not successful display a message to the user.
#     Used try blocks when establishing connections to the webservice.
#       Printed a message to the user indicating whether or not the connection was successful

import requests
import datetime
import configparser
from requests.exceptions import HTTPError


# Class to represent config values ( apikey, units, country, language, base URl )
class Config:
    def __init__(self, apikey, units, country, language, baseurl):
        self.apikey = apikey
        self.units = units
        self.country = country
        self.language = language
        self.baseurl = baseurl


# function to retrive configuration values from config file
def get_configvalues():
    config = configparser.ConfigParser()
    config.read('config.ini')
    return Config(config['openweathermap']['api'], config['openweathermap']['units'],
                  config['openweathermap']['country'],
                  config['openweathermap']['language'], config['openweathermap']['baseurl'])


# function to request for weather data
def get_weatherdata(query,config):
    # try-except block
    try:
        api_key = config.apikey
        base_url = config.baseurl
        # base_url = "http://api.openweathermap.org/data/2.5/"
        complete_url = base_url + query + "&appid=" + api_key  # "&cnt=3"  # +"&units=metric"
        # get the API value into response
        print('Web Serivce requesting...')
        response = requests.get(complete_url)
        # returns an HTTPError object if an error has occurred during the process
        response.raise_for_status()
        # if status code 200 is succefully received the data from API
        if response.status_code == 200:
            print('sucessfull received data from Web Serivce')
        # convert response details into jsonresponse as JSON format
        return response.json()
    # Exception Handling
    except HTTPError as http_err:
        print(f'HTTP error occurred: {http_err}')
    except Exception as err:
        print(f'Other than HTTP error occurred: {err}')


# function to display results from Json
def display_results(weathers, weatherData):
    # try-except block
    try:
        print("Here is the Weather details of the given City or Zip Code")

        print("---------------------------------------------------------")
        print("{:<20} {:<15} {:<15} {:<15} {:<15} {:<15}{:<15} {:<15}{:<15}{:<15}".format('Date', 'Temp', 'Temp Min',
                                                                                          'Temp Max',
                                                                                          'Pressure', 'Humidity',
                                                                                          'description', 'Pressure',
                                                                                          'Wind_Speed', 'Wind Deg'))
        print(
            "--------------------------------------------------------------------------------------------------------------------------------------------------------")
        # Looping the weathers list of JSON objects to print the weather details for the selected Range
        if (weatherData == "2"):
            print("Name of the Place : " + (weathers['city']['name']))
            for i in weathers['list']:
                print(
                    "{:<20} {:<15} {:<15} {:<15} {:<15} {:<15}{:<15} {:<15}{:<15}{:<15}".format(i["dt_txt"],
                                                                                                i["main"]["temp"],
                                                                                                i["main"]["temp_min"]
                                                                                                , i["main"]["temp_max"],
                                                                                                i['main']['pressure'],
                                                                                                i['main']['humidity']
                                                                                                , i['weather'][0][
                                                                                                    'description'],
                                                                                                i['main']['pressure']
                                                                                                , i['wind']['speed'],
                                                                                                i['wind']['deg']
                                                                                                ))
        # Current Weather details
        elif (weatherData == "1"):
            print("Name of the Place : " + (weathers['name']))
            print(
                "{:<20} {:<15} {:<15} {:<15} {:<15} {:<15}{:<15} {:<15}{:<15}{:<15}".format("now",
                                                                                            weathers['main']['temp'],
                                                                                            weathers["main"]["temp_min"]
                                                                                            , weathers["main"][
                                                                                                "temp_max"],
                                                                                            weathers['main'][
                                                                                                'pressure'],
                                                                                            weathers['main']['humidity']
                                                                                            , weathers['weather'][0][
                                                                                                'description'],
                                                                                            weathers['main']['pressure']
                                                                                            , weathers['wind']['speed'],
                                                                                            weathers['wind']['deg']
                                                                                            ))
        else:
            print("Invalid Entry")
        print(
            "--------------------------------------------------------------------------------------------------------------------------------------------------------")
    except:
        print("Unable to get weather information for the given City. Please try again")


# main function
def main():
    # try-except block
    try:
        now = datetime.datetime.now()
        # Fetching Default Parameter Country as US and Units - Imperial from configuration file
        config = get_configvalues()
        unitsparameter = config.units
        countryparameter = config.country
        Languageparameter = config.language
        weatherdataoption = "weather"
        countparameter = 1
        print("Welcome to the API :  Weather Forecast Data")
        print('Date : ' + now.strftime("%Y-%m-%d %H:%M:%S"))  # printing date & time
        # Driving Variable to allow User to enter multiple times
        iscontinue = True

        while (iscontinue):
            print("************MAIN MENU**************")
            inputselection = input("Select your choice : \n"
                                   "1. Temperature Unit Selection - Default " + unitsparameter + " \n"
                                   + "2. Country Selection - Default " + countryparameter + " \n"
                                   + "3. Language Selection - Default " + Languageparameter + " \n"
                                   + "4. Search City or Zip \n"
                                   + "5. Exit \n")
            # If User wants to change to metric C
            if inputselection == "1":
                inputunitsparameters = input("Please Enter Units : 1. metric (celcius) or 2. imperial (fahrenheit)\n")
                if inputunitsparameters == "1":
                    unitsparameter = "metric"
                elif inputunitsparameters == "2":
                    unitsparameter = "imperial"
                else:
                    " Please enter 1 or 2 to update Units"
            # If User wants to change the Country from US to different Country
            elif inputselection == "2":
                countryparameter = input("Please Enter the 2 digit Country ISO Code\n")
            # If User wants to change the Country from US to different Country
            elif inputselection == "3":
                Languageparameter = input("Please Enter Language to view\n")
            # If Users choose to search by City or Zip code
            elif inputselection == "4":
                city = input('Enter zip code or City name: \n')
                inputweatherDataoption = input(
                    'Enter Your Choice of Weather Data : 1. Current Weather Data 2. 3 hour forecast data \n')
                if inputweatherDataoption == "1":
                    weatherdataoptionparameter = "weather"
                elif inputweatherDataoption == "2":
                    countparameter = input("Please enter Number of Forecasting (only Integer days) \n")
                    weatherdataoptionparameter = "forecast"
                else:
                    print("Invalid Input. Please select the option 1 or 2")
                    continue
                if city.isdigit():
                    query = weatherdataoptionparameter + '?zip=' + city + "," + countryparameter + "&" + "units=" + unitsparameter + "&" + "lang=" + Languageparameter + "&cnt=" + str(
                        countparameter)
                else:
                    query = weatherdataoptionparameter + '?q=' + city + "," + countryparameter + "&" + "units=" + unitsparameter + "&" + "lang=" + Languageparameter + "&cnt=" + str(
                        countparameter)
                # Calling get_weatherdata function to get the API response details as JSON
                w_data = get_weatherdata(query, config);
                # Calling display_results function to display all the details
                display_results(w_data, str(inputweatherDataoption))

            # Exit Option
            elif inputselection == "5":
                SystemExit
                iscontinue = False

            # Invalid Option
            else:
                print("Invalid Input : Please enter 1,2,3,4,5 Only")

    except Exception as err:
        print(f'Other than HTTP error occurred: {err}')


if __name__ == '__main__':
    main()
