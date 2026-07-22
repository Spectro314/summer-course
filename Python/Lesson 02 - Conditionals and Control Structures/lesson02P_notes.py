# user_number = input("Enter a number: ")
# if int(user_number) >= 1:
#     print("Positive Number")
# elif int(user_number) == 0:
#     print("Zero")
# else:
#     print("Negative Number")

# user_number = input("Enter a number: ")
# if int(user_number) %2 == 0:
#     print("The Number is Even")
# elif int(user_number) == 0:
#     print("The Number is Zero")
# else:
#     print("The Number is Odd")

# user_age = input("Enter a age: ")
# if int(user_age) <= 13:
#     print("Child")
# elif int(user_age) <= 19:
#     print("Teenager")
# elif int(user_age) <= 64:
#     print("Adult")
# else:
#     print("Senior")

# number_a = input("Enter a number: ")
# number_a = int(number_a)
# number_b = input("Enter another number: ")
# number_b = int(number_b)
# if number_a > number_b:
#     print("Larger")
# elif number_a < number_b:
#     print("Smaller")
# else:
#     print("a is equal to b")

# user_grade = input("Enter a grade: ")
# if int(user_grade) >= 90:
#     print("A")
# elif int(user_grade) >= 80:
#     print("B")
# elif int(user_grade) >= 70:
#     print("C")
# elif int(user_grade) >= 60:
#     print("D")
# else:
#     print("F")

# user_text = input("Enter your input string:  ")
# if len(user_text) > 10:
#     print("Long string")
# else:
#     print("Short string")   

# user_number = input("Enter a number:  ")
# user_number = int(user_number)
# if user_number >= 10 and user_number <= 20:
#     print("Number is in range")
# else:
#     print("Out of range")

# user_letter = input("Enter a letter:  ")
# if user_letter == "a" or user_letter == "e" or user_letter == "i" or user_letter == "o" or user_letter == "u":
#     print("The letter is a Vowel")
# else:
#     print("The letter is a Consonant")

# Alternative solution using 'in'
# if user_letter in "aeiou":
#     print("The letter is a Vowel")
# else:
#     print("The letter is a Consonant")

# user_year = input("Enter a year:  ")
# user_year = int(user_year)
# if (user_year % 4 == 0 and user_year % 100 != 0) or (user_year % 400 == 0):
#     print("Leap year")
# else:
#     print("Not a leap year")

# user_weight = input("What is your weight (kg)?  ")
# user_weight = float(user_weight)
# user_height = input("What is your height (m)?  ")
# user_height = float(user_height)    

# bmi = user_weight / (user_height ** 2)

# if bmi < 18.5:
#     print("BMI:",bmi," - Underweight")
# elif bmi < 25:
#     print("BMI:",bmi," - Normal weight")
# elif bmi < 30:
#     print("BMI:",bmi, " - Overweight")
# else:
#     print("BMI:",bmi," - Obese")

# Alternative using fprints
# if bmi < 18.5:
#     print(f"BMI: {bmi} - Underweight")
# elif bmi < 25:
#     print(f"BMI: {bmi} - Normal weight")
# elif bmi < 30:
#     print(f"BMI: {bmi} - Overweight")
# else:
#     print(f"BMI: {bmi} - Obese")

# colors = ["red", "blue", "green"]

# for color in colors:
#     print(color)

# user_numbers = [5, 10, 15, 20, 25]

# print(f"The list has {len(user_numbers)} items")

# my_list = []
# my_list.append("Jose")
# my_list.append("J.")
# my_list.append("Walters")
# my_list.append("Del")
# my_list.append("Moral")
# my_list.append(52)
# my_list.append(True)
# print(my_list)
# print(f"My list has {len(my_list)} items")

# for j in range(1, 11):
#     print(j)

# numbers = [4, 7, 2, 9, 12]
# sum = 0
# for number in numbers:
#     sum += number
#     print(number)
# print(f"The Sum is: {sum}")

# available_fruits = ["apple", "banana", "orange", "mango"]
# fruit = "banana"

# if fruit in available_fruits:
#     print(f"{fruit} is in stock")
# else:
#     print(f"{fruit} is out of stock")

# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# count = 0
# for number in numbers:
#     if number % 2 == 0:
#         count += 1
# print(f"There are {count} even numbers")

# count = 10

# while count >= 1:
#     print(count)
#     count -= 1  

# number = 1
# while number <= 100:
#     print(number)
#     number *= 2

# even_numbers = []
# for j in range(0, 21, 2):
#     even_numbers.append(j)

# print(even_numbers)

# # Alternative using list()
# even_numbers = list(range(0, 21, 2))
# print(even_numbers)

# squares_numbers = []
# for j in range(1, 6):
#     squares_numbers.append(j ** 2)

# print(squares_numbers)

text = "Hello World"
vowels = "aeiouAEIOU"

# count = 0
# for char in text:
#     if char in vowels:
#         count += 1

# print(f"Number of vowels is: {count}")

# numbers = [23, 67, 12, 89, 45, 34]

# maximum_number = numbers[0]
# for number in numbers:
#     if number > maximum_number:
#         maximum_number = number

# print(f"The maximum is {maximum_number}")

# numbers = [2, 5, 7, 10, 15]

# for number in numbers:
#     if number == 7:
#         break
#     print(number)

# print("Operation Stopped")

# for j in range(1, 11):
#     if j % 3 == 0:
#         continue
#     print(j)

# for i in range(1, 4):
#     for j in range(1, 4):
#         print(f"{i} × {j} = {i * j}")
#     print()  # Empty line after each row

# # Alternative - compact format
# for i in range(1, 4):
#     for j in range(1, 4):
#         print(f"{i*j:3}", end=" ")
#     print()  # New line after each row

# numbers = [5, 10, 8, 15, 12, 7]

# result = []
# total = 0
# j = 0

# while total <= 50 and j < len(numbers):
#     result.append(numbers[j])
#     total += numbers[j]
#     j += 1

# print(f"Final list: {result}")
# print(f"Total sum: {total}")

# fruits = ["apple", "banana", "cherry", "date"]
# target = "cherry"

# for j in range(len(fruits)):
#     if fruits[j] == target:
#         print(f"{target} is at index {j}")
#         break
# else:
#     print(f"{target} is not in the list")

# original = [10, 20, 30, 40, 50]

# reversed_list = []
# for j in range(len(original) - 1, -1, -1):
#     reversed_list.append(original[j])

# print(reversed_list)

# # Alternative using while loop
# reversed_list = []
# j = len(original) - 1
# while j >= 0:
#     reversed_list.append(original[j])
#     j -= 1

# print(reversed_list)

# num_asterisks = 10
# total_printed = 0
# row = 1

# while total_printed < num_asterisks:
#     for col in range(row):
#         if total_printed >= num_asterisks:
#             break
#         print("*", end="")
#         total_printed += 1
#     print()  # New line after each row
#     row += 1

# # Alternative using flag variable
# num_asterisks = 10
# total_printed = 0
# stop = False

# for row in range(1, 100):  # Use a large range
#     if stop:
#         break
#     for col in range(row):
#         print("*", end="")
#         total_printed += 1
#         if total_printed >= num_asterisks:
#             stop = True
#             break
#     print()

for number in range(1, 101):