# for number in range(1, 101):
#     if number % 3 == 0 and number % 5 == 0:
#         print("FizzBuzz")
#     elif number % 3 == 0:
#         print("Fizz")
#     elif number % 5 == 0:
#         print("Buzz")
#     else:
#         print(number)

# import random

# user = input("Enter a choice (rock, paper, scissors): ")
# computer = random.choice(["rock", "paper", "scissors"])

# if user == computer:
#     print("It's a tie!")
# elif (user == "rock" and computer == "scissors"):
#     print("You win!")

# elif (user == "paper" and computer == "rock"):
#     print("You win!")

# elif (user == "scissors" and computer == "paper"):
#     print("You win!")

# else:
#     print("You lose!")
# print(f"Computer chose: {computer}") 

# import random

# random_number = random.randint(1, 100)
# user_number = input("Enter a number between 1 and 100: ")
# user_number = int(user_number)
# print(f"Random number between 1 and 100: {random_number}")

# if user_number == random_number:
#     print("You guessed it!")
# elif user_number < random_number:
#     print("Your guess is too low.")
# else:
#     print("Your guess is too high.")

# import random

# random_number = random.randint(1, 100)
# user_number = input("Enter a number between 1 and 100: ")
# user_number = int(user_number)
# while user_number != random_number:
#     if user_number < random_number:
#         print("Your guess is too low.")
#     else:
#         print("Your guess is too high.")
#     user_number = int(input("Enter a number between 1 and 100: "))
# print(f"Congratulations! You guessed the correct number: {user_number}")

# import random

# random_number = random.randint(1, 100)

# if random_number <50:
#     print("The random number is less than 50.")
# elif random_number == 50:
#     print("The random number is exactly 50.")
# else:
#     print("The random number is greater than 50.")
# print(f"The random number is: {random_number}")

# def area(a, b):
#     return a * b

# a = input("Enter the length of the rectangle: ")
# a = int(a)
# b = input("Enter the width of the rectangle: ")
# b = int(b)

# print(f"The area of the rectangle is: {area(a, b)}")

# def rect_area(length: int, width: int):
#     return length * width
# length = input("Enter the length of the rectangle: ")
# length = int(length)
# width = input("Enter the width of the rectangle: ")
# width = int(width)

# print(f"The area of the rectangle is: {rect_area(length, width)}")



# from operator import add


# def tip(amount: float, percentage: float):
#     return amount * (percentage / 100)

# user_amount = input("Enter the bill amount: ")
# user_amount = float(user_amount)
# user_percentage = input("Enter the tip percentage: ")
# user_percentage = float(user_percentage)
# print(f"The tip amount is: {tip(user_amount, user_percentage)}")

# print(f"The sum of the bill amount is: {add(user_amount, tip(user_amount, user_percentage))}")

# a = input("Enter a first string for comparison: ")
# b = input("Enter a second string for comparison: ")
# has_more_characters = str(a) or str(b)

# print(f"Do the strings have more characters? {len(a) > len(b)}")

# print(f"Do the strings have the same number of characters? {len(a) == len(b)}")

# string1 = input("Enter a first string for comparison: ")
# string2 = input("Enter a second string for comparison: ")

# def has_more_characters(string1: str, string2: str) -> bool:
#     length1 = len(string1)
#     length2 = len(string2)
#     if length1 > length2:
#         return string1
#     elif length2 > length1:
#         return string2
#     else:
#         return "They are equal"
    
# print(f"The string with more characters is: {has_more_characters(string1, string2)}")

# user_input = float(input("Enter current temperature: "))
# if user_input < 40:
#         print("Bring a jacket.")
# elif user_input >= 40 and user_input <= 65:  
#         print("Enjoy the weather.")
# else:
#         print("It's hot outside.")

# for number in range(1, 31):
#     if number % 3 == 0 and number % 5 == 0:
#         print("FizzBuzz")
#     elif number % 3 == 0:
#         print("Fizz")
#     elif number % 5 == 0:
#         print("Buzz")
#     else:
#         print(number)

from tracemalloc import start
from wsgiref import validate


# a = input("Enter a start of funtion: ")
# a = int(a)
# b = input("Enter a end of function: ")
# b = int(b)

# def fizzbuzz(a: int, b: int) -> int:
#     fizzbuzzes = 0
#     for number in range(a, b + 1):
#         if number % 3 == 0 and number % 5 == 0:
#             print("FizzBuzz")
#             fizzbuzzes += 1 
#         elif number % 3 == 0:
#             print("Fizz")
#         elif number % 5 == 0:
#             print("Buzz")
#         else:
#             print(number)
#     return fizzbuzzes

# amount = fizzbuzz(a, b)

# fizzbuzz(a, b)

# print(f"There are {amount} of fizzbuzzes in between and included.")

# def password_checker(password: str) -> str:
#     password_length = len(password)
#     if password_length < 8:
#         return "Password is weak."
#     elif password_length >= 8 and password_length <= 12:
#         return "Password is moderate."
#     else:
#         return "Password is strong."
    
# def score grade(Score: str) -> str:
#     if score_grade >= 90:
#         return "A"
#     elif score_grade >= "80":
#         return "B"
#     elif score_grade >= "70":
#         return "C"
#     elif score_grade >= "60":
#         return "D"
#     elif score_grade <= "59:
#         return "F"
#     else:
#         return "Invalid grade"

# students = int(input("How many grades are there to enter? "))
# for student in range(1, students+1):
#     score_grade = int(input(f"Enter student {student} score: "))
#     print(f"Student #{student} got a letter grade {letter_grade(score)}")

# print(f"The class average was {total_score/students}, this is a {letter_grade(total_score/students)}")

# my_list = ['c','a','t']
# my_string = "cat"

# # 1. Loop over both
# for item in my_list:
#     print(item)

# # 2. Loop over the string
# for char in my_string:
#     print(char)

# #indexing and slicing
# print(my_list[0],)
# print(my_string[0])

# print(my_list[0:2])
# print(my_string[0:2])

# validate_username("coder_42")
# validate_username("2cool")
# validate_username("hi")
# validate_username("python_dev_")
# validate_username("justletters")

import validate
import string

def validate_username(username: str) -> str:
    if not username:
        return "Username cannot be empty."
    if not username[0].isalpha():
        return "Username must start with a letter."
    if not all(char.isalnum() or char == "_" for char in username):
        return "Username can only contain letters, numbers, and underscores."
    if len(username) < 5:
        return "Username is too short."
    if len(username) > 15:
        return "Username is too long."
    return "Username is valid."