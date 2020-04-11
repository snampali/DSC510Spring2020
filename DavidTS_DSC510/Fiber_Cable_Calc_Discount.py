'''
Cource: DSC510
Assignment: 3.1 Programming
Name: David TS
Description: Fibre Optic Cable Installation Cost Calculator
'''
#Welcome Message
print('Welcome to David Cable Installation Cost Calculation')
Company_Name = input('Please enter company name : ')
Cable_Length = float(input('Please enter fiber cable length in feet : '))
Cable_Cost = 0.87
if Cable_Length > 500: #discount cost for more than 500 feet
    Installation_Cost = Cable_Length * 0.50
    Cable_Cost = 0.50
elif Cable_Length > 250: #discount cost for more than 250 feets
    Installation_Cost = Cable_Length * 0.70
    Cable_Cost = 0.70
elif Cable_Length > 100: #discount cost for more than 100 feet
    Installation_Cost = Cable_Length * 0.80
    Cable_Cost = 0.80
else: #default cost
    Installation_Cost = Cable_Length * Cable_Cost
print('\r')
print('***************Receipt*****************')
print('Company Name               :',Company_Name)
print('Fiber cable length in feet :',Cable_Length)
print('Installation Cost per feet : $',Cable_Cost)
print('Total Cost                 : $',Installation_Cost)
print('***************************************')
#End