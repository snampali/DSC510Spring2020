#! C:\Users\arossman159618\PycharmProjects\Rossman_DSC510                   shebang line
# Week 12 Final Project - Weather App
# Prompt user for City Name or Zip Code (user's choice) and parse valid entries into a https: url
# Weather data courtesy of OpenWeatherMap.org using their API with authenticated authorization code
# Display each city's weather data in a readable form including city name
# Ask for re-entry of invalid data or exit gracefully for website unavailability

def docString():

    """
HEADER
Institution: Bellevue University
Course: DSC510
Assignment: 12.1
Date: 31 May 2020
Name: Alfred Rossman
Interpreter: Python 3.8
    """

print(docString.__doc__)                                                 # Print docstring header
import requests                                                          # HTTP/JSON  Requests Library

K_OFFSET = 273.15                                                        # 273.15K = 0C
F_CONSTANT = 1.8                                                         # C to F scaling
F_OFFSET = 32.0                                                          # 32F = 0C
HG_CONSTANT = 0.0295                                                     # mBar to in of Hg scaling


# Prompt for user input of City Name or valid numeric Zip Code
# Return proper query for whichever is entered
# Check for Python built-in ValueError

def userInput():
    while True:
        try:
            userRequest = input('\nEnter City Name or 5-Digit US Zip Code (Hit <CR><LF> key to end): ')
        except ValueError:                                               # Test for valid input
            print('Invalid Input - Try Again\n')
            continue
        else:
            if (userRequest.isnumeric()) and (len(userRequest) == 5):    # Test for numeric 5-digit zip code
                return 'zip=' + userRequest
            elif len(userRequest) > 0:                                   # Test for string entry of city name
                return 'q=' + userRequest
            else:                                                        # Return None for neither
                return None
# End of Function


# Convert unflatDict and return flattened dictionary (thanks to geeksforgeeks.com this base function)
# Default separator '_'

def flattenDict(unflatDict, separator ='_', prefix =''):
    return { prefix + separator + k if prefix else k : v
             for kk, vv in unflatDict.items()
             for k, v in flattenDict(vv, separator, kk).items()                # Recursive call
             } if isinstance(unflatDict, dict) else { prefix : unflatDict }
# End of Function


# Print relevant weather data from flattened dict
# Convert Kelvin to Fahrenheit
# Convert milliBar to Inches of Mercury (Hg)

def printRelevantWeather(flatDict):
    print('City of ', flatDict.get('name', None), end = '')
    print(' in ', flatDict.get('sys_country', None))
    print('Current Temperature: ', round(float((flatDict.get('main_temp', None) - K_OFFSET) * F_CONSTANT + F_OFFSET), 1), ' deg F')
    print('Relative Humidity: ', flatDict.get('main_humidity', None), '%')
    print('Feels Like: ', round(float((flatDict.get('main_feels_like', None) - K_OFFSET) * F_CONSTANT + F_OFFSET), 1), 'deg F')
    print('Barometric Pressure: ', round(float(flatDict.get('main_pressure', None)) * HG_CONSTANT, 2), ' inches Hg')
    print('Cloud Cover: ', flatDict.get('clouds_all', None), '%')
    print('Max. Temp: ', round(float((flatDict.get('main_temp_max', None) - K_OFFSET) * F_CONSTANT + F_OFFSET), 1), ' deg F')
    print('Min. Temp: ', round(float((flatDict.get('main_temp_min', None) - K_OFFSET) * F_CONSTANT + F_OFFSET), 1), ' deg F')
    print('Wind Speed is ', flatDict.get('wind_speed', None), ' knots ', end = '')
    print('from Azimuth ', flatDict.get('clouds_all', None), ' degrees (North is 0)')
# End of Function


def main():

# Access web for weather
# Free API of openweathermap.org restricts access to 1-min. intervals - Gracefully timeout >60 sec
# Use f-strings (Python >= 3.6)
    print('Welcome to the Weather Application\n')
    userQuery = True
    while userQuery != None:                                                         # Loop until queries completed
        userQuery = userInput()                                                      # Get query
        url = f'https://api.openweathermap.org/data/2.5/weather?{userQuery}&APPID=cf3d4fcf9113c2067859018c5b491327'
        response = requests.get(url, timeout = 60)

        if response.ok:                                                              # Requests Status Good
            parsedWeather = response.json()                                          # Parse JSON format to dict
            flatWeather = flattenDict(parsedWeather)                                 # Flatten dict
            printRelevantWeather(flatWeather)                                        # Print relevant weather data of city
        elif response.status_code == 404:                                            # Request not found - Try Again
            print('Invalid Entry or City or Zip Code not in database - Try Again' )
        else:                                                                        # User asserts completion
            break
# End of Main


# Start of program

if __name__ == '__main__':                              # Runs main() if file wasn't imported
    main()

# End of program
