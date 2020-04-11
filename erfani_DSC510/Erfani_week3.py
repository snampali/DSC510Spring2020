# Hedyeh Erfani
# Assignment for week three
# Purpose: To create a receipt for a user based on number of feet of cable purchased

# Greet the user
print('Hello user')

# Inquire about the company name
name: str = input("Please enter your company name:\n")

# Inquire about how much cable they are purchasing
feet = float(input("How many feet are you purchasing? :\n"))

# Calculate cost and applicable discounts
if feet <= 100:
    cost = feet * 0.87
elif 100 < feet <= 250:
    cost = feet * 0.80
elif 250 < feet <= 500:
    cost = feet * 0.70
elif feet > 500:
    cost = feet * 0.50

# Give the user a receipt
print(f'Here is your receipt:')
print(f'Company name:{name}')
print(f'Total feet:{feet}')
print(f'Total cost:{cost}')
