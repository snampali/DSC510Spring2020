# -*- coding: utf-8 -*-
"""
Created on Thu Jan 23 21:14:17 2020

@author: Cody's PC
"""
#Name: Cody Myers
#Assignment number: Week 2 #1
#Purpose: The purpose of this program is to create a reciept for users regarding an install
#         of fiber optic cables. 

#Prompt user with a welcome meessage
print("Hello! Welcome to our store, we install fiber optic cable!")

#Get user's company
print("What company are you looking to order for? Please press Enter when you're done typing")
company = input()

#Get the amount of fiber optic cable is needed for the installation
print("How many feet will be needed for this installation? Press Enter when you're done typing")
amount = int(input())

#Calculate the cost of the installation's product
cost = amount * 0.87

#Give the customer their receipt
print("Here is your reciept.")
reciept = ("\ncompany: {} \nNumber of feet: {}ft \ncalculated cost: ${} \ntotal cost: ${}").format(company, amount, cost, cost)
print(reciept)