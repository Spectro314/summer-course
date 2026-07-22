
########################
## Problem 1a
########################

# user_name = input("What is your full name? ")
# #  user_name_len = len(user_name)
# favorite_number = input("What is your favorite number? ")

# num_asterisks = 35
# print('*' * num_asterisks) 

# greeting = 'Hello, ' + user_name.strip().title() + '!' 
# white_space_length = (35 - len(greeting) - 3) 
# print('* ' + greeting + ' ' * white_space_length + '*')

# favorite_number = 'Your favorite number is ' + favorite_number
# print('* ' + favorite_number + '  *')

# print('*' * num_asterisks) 

# user_name = input("What is your full name? ")
# user_number = input("Enter your favorite integer number: ")

# def personalized_card(symbol: str, name: str, favorite_number: int):
#     num_asterisks = 35
#     print(symbol * num_asterisks) 

#     greeting = 'Hello, ' + name.strip().title() + '!' 
#     white_space_length = (35 - len(greeting) - 3) 
#     print(symbol + ' ' + greeting + ' ' * white_space_length + symbol)

#     favorite_number_str = 'Your favorite number is ' + str(favorite_number)
#     print(symbol + ' ' + favorite_number_str + '  ' + symbol)

#     print(symbol * num_asterisks)

# personalized_card('*', user_name, int(user_number)) 

# print(list(range(1, 16)))
# print(list(range(2, 31, 2)))
# print(list(range(20, -1, -1))) 

print('Problem 04 - Road Trip Fuel Estimate')
user_distance = input('Distance (miles)       : ')
user_distance = float(user_distance) # convert to float for calculations
user_efficiency = input('Fuel efficiency (MPG)  : ')
user_efficiency = float(user_efficiency) # convert to float for calculations
user_price = input('Gas price ($/gal)      : ')
user_price = float(user_price) # convert to float for calculations

gals_needed = round(user_distance / user_efficiency, 2)
total_cost = gals_needed * user_price

print() 
print(f'Gallons needed: {gals_needed}')
print(f'Total fuel cost: ${round(total_cost, 2)}')

# print(f"Gallons needed: {gals_needed:.2f}")
# print(f"Total fuel cost: ${total_cost:.2f}")