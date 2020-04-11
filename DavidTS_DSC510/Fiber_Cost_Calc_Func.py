'''
Cource: DSC510
Assignment: 4.1 Programming Function
Name: David TS
Description: Fibre Optic Cable Installation Cost Calculator
'''
#Welcome Message
print('Welcome to David Cable Installation Cost Calculation')
Company_Name = input('Please enter company name : ')
Cable_Length = float(input('Please enter fiber cable length in feet : '))
Cable_Cost = 0.87
def cost_calc(x,y): #function to calculate the installation cost
    Installation_Cost = x*y
    return round(Installation_Cost,2)
if Cable_Length > 500: #discount cost for more than 500 feet
    Total_Cost = cost_calc(x=Cable_Length,y=0.50)
    Cable_Cost = 0.50
elif Cable_Length > 250: #discount cost for more than 250 feets
    Total_Cost = cost_calc(x=Cable_Length, y=0.70)
    Cable_Cost = 0.70
elif Cable_Length > 100: #discount cost for more than 100 feet
    Total_Cost = cost_calc(x=Cable_Length, y=0.80)
    Cable_Cost = 0.80
else: #default cost
    Total_Cost = cost_calc(x=Cable_Length, y=Cable_Cost)
print('\r')
print('***************Receipt*****************')
print('Company Name               :',Company_Name)
print('Fiber cable length in feet :',Cable_Length)
print('Installation Cost per feet : $',Cable_Cost)
print('Total Cost                 : $',Total_Cost)
print('***************************************')
#End