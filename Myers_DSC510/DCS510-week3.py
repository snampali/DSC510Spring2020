# -*- coding: utf-8 -*-
"""
Created on Sun Mar 29 12:52:45 2020

@author: Cody's PC
"""

#Name: Cody Myers
#Assignment number: Week 3 #1
#Purpose: The purpose of this program is to create a reciept for users regarding an install
#         of fiber optic cables while incorporating a bulk discount

#Prompt user with a welcome meessage
print("Hello! Welcome to our store, we install fiber optic cable!")

#Get user's company
print("What company are you looking to order for? Please press Enter when you're done typing")
company = input()

#Get the amount of fiber optic cable is needed for the installation
print("How many feet will be needed for this installation? Press Enter when you're done typing")
amount = int(input())

#Calculate the cost of the installation's product
cost = 0.0
if amount <= 100:
    cost = 0.87
elif amount in range(100,250) and amount != 100:
    cost = 0.80
elif amount in range(250,500) and amount != 250:
    cost = 0.70
else:
    cost = 0.50

newCost = amount*cost

#format the cost into a dollar amount
totalCost = "{:.2f}".format(newCost)

#Give the customer their receipt
print("Here is your reciept.")
reciept = ("\ncompany: {} \nNumber of feet: {}ft \ncalculated cost: ${} \ntotal cost: ${}").format(company, amount, totalCost, totalCost)
print(reciept)