# user_number = input("Enter a number: ")
# if int(user_number) >= 1:
#     print("positive")
# elif int(user_number) == 0:
#     print("Zero")
# else:
#     print("negative")

# user_number = input("Enter a number: ")
# if int(user_number) >= 1:
#     print("The number is positive")
# else:
#     print("Not positive")

# user_number = input("Enter a number: ")
# if int(user_number) % 2 == 0:
#     print("The number is even")
# else:
#     print("The number is odd")

# user_number = input("Enter a number: ")
# if int(user_number) <= 13:
#     print("Child")
# elif int(user_number) <= 19:
#     print("Teenager")
# elif int(user_number) <= 64:
#     print("Adult")
# else:
#     print("Senior")

# a = 10
# b = 20
# if a > b:
#     print("Larger")
# elif a < b:
#     print("Smaller")
# else:
#     print("a is equal to b")

# user_grade = input("Enter your grade: ")
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

# user_number = int(input("Enter an even integer number: "))
# while user_number % 2 == 1:
#     user_number = int(input("Enter an even integer number: "))
    
# print(f"Good job! You entered an even number: {user_number}")

secret_number = 22

user_guess = int(input("Guess integer number: "))
count_guesses = 1
while user_guess != secret_number:
    if user_guess < secret_number:
        print("Your guess was too Low")
    else:
        print("Your guess was too high")
    user_guess = int(input("Guess an integer number: "))
    count_guesses += 1

print(f"Congratulations! You guessed the correct number: {user_guess}")
print(f"It took you {count_guesses} guesses.")
