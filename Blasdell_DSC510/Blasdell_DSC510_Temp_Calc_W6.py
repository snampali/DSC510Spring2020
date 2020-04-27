# course: DSC510
# assignment: 6.1
# date: 04/14/20
# name: Blaine Blasdell
# description: Customer Fiber Optic cable calculator


def temp_calc_min(list_of_temps):  # function to calculate minimum temp - receive list of temps
    temp_min_current = 0.0
    for i in range(len(list_of_temps)):  # for loop - number of temps
        if i == 0:
            temp_min_current = float(list_of_temps[i])  # first temp  - set to min
        else:
            if temp_min_current >= list_of_temps[i]:  # compare to first temp and replace if less
                temp_min_current = list_of_temps[i]
    return temp_min_current  # return min temp


def temp_calc_max(list_of_temps_max):  # function to calculate maximum temp - receive list of temps
    temp_max_current = 0.0
    for i in range(len(list_of_temps_max)):  # for loop - number of temps
        if i == 0:
            temp_max_current = float(list_of_temps_max[i])  # first temp  - set to max
        else:
            if temp_max_current <= list_of_temps_max[i]:  # compare to first temp and replace if more
                temp_max_current = list_of_temps_max[i]
    return temp_max_current  # return max temp


def temp_average(list_of_temps):  # calculate average of all temps  - receive list of temp
    temp_total = 0.0
    for i in range(len(list_of_temps)):  # for loop - number of temps
        temp_total = temp_total + list_of_temps[i]  # add up temps
    temp_avg = temp_total / (i + 1)  # calc avg and return
    return temp_avg


def temp_convert(temp):  # function to convert to celsius
    temp_cel = 0.0
    temp_cel = (temp - 32) / 1.8
    return temp_cel


def user_input(dis_message):  # function to get user input and check for error
    while True:
        try:
            user_number = float(input(dis_message))
        except ValueError:
            print('Please enter a valid temperature:')
            continue
        else:
            return user_number
            break


# main program

# Welcome
print('\r')
print('\r')
print('Welcome to the Temperature Calculator\r')

temperatures = list()  # set empty list of temps
looping = True
count_num_temp: int = 1

# while loops to get temps using exit value of 9999
while looping:
    temp_input = user_input("Enter each temp in Fahrenheit (Type 9999 to exit): ")

    if int(temp_input) == 9999:
        looping = False
    else:
        temperatures.append(float(temp_input))
        count_num_temp = count_num_temp + 1

print('\r')
print('\r')
print('--------------------------------------------------------------------------\r')
print('\r')
print('For the', (count_num_temp - 1), 'temperatures: \r')  # print total number of temps
print('\r')

# calculate and print min temp
min_temp = temp_calc_min(temperatures)
min_temp_celc = temp_convert(min_temp)
print('Minimum Temperature is', format(min_temp, '.2f'), 'F and', format(min_temp_celc, '.2f'), 'C.')
print('\r')

# calculate and print max temp
max_temp = temp_calc_max(temperatures)
max_temp_celc = temp_convert(max_temp)
print('Maximum Temperature is', format(max_temp, '.2f'), 'F and', format(max_temp_celc, '.2f'), 'C.')
print('\r')

# calculate and print avg temp
avg_temp = temp_average(temperatures)
avg_temp_celc = temp_convert(avg_temp)
print('Average Temperature is', format(avg_temp, '.2f'), 'F and', format(avg_temp_celc, '.2f'), 'C.')

# Print and exit
print('\r')
print('--------------------------------------------------------------------------')
print('\r')
print('Thank you for using the temperature calculator.')
print('Have a nice day!')
