'''
Cource: DSC510
Assignment: 2.1 Programming
Name: David TS
Description: Fibre Optic Cable Installation Cost Calculator
'''
#Welcome Message
print('Welcome to the Store')
Company_Name = input('Please enter company name : ')
Cable_Length = float(input('Please enter fiber cable length in feet : '))
Cable_Cost = 0.87
Installation_Cost = Cable_Length*Cable_Cost
print('\r')
print('***************Receipt*****************')
print('Company Name               :',Company_Name)
print('Fiber cable length in feet :',Cable_Length)
print('Installation Cost per feet : $',Cable_Cost)
print('Total Cost                 : $',Installation_Cost)
print('***************************************')
#End
