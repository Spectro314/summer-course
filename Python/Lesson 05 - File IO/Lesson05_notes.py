# import random
# number_games = input("Enter the number of games you want to play (between 1 and 9): ")
# number_games = int(number_games)    
# while number_games <= 1 or number_games >= 9:
#     number_games = input("Enter a number between 1 and 9: ")
#     number_games = int(number_games)
# for _ in range(number_games):
#     user = input("Enter a choice (rock, paper, scissors): ")
#     computer = random.choice(["rock", "paper", "scissors"])

#     if user == computer:
#         print("It's a tie!")
#     elif (user == "rock" and computer == "scissors"):
#         print("You win!")
#     elif (user == "paper" and computer == "rock"):
#         print("You win!")
#     elif (user == "scissors" and computer == "paper"):
#         print("You win!")
#     else:
#         print("You lose!")
#     print(f"Computer chose: {computer}") 


# games_list = [1, 3, 5, 7, 9]
# total_games = input("How many games would you like to play (1-9)? Odd number only: ")
# total_games = int(total_games)
# while total_games not in games_list:
#     total_games = input("Please enter a valid odd number between 1 and 9: ")
#     total_games = int(total_games)

# user_wins = 0
# computer_wins = 0
# wins_needed = (total_games // 2) + 1

# #Test
# print(f"Total games: {total_games}")
# print(f"Wins needed: {wins_needed}")
# print(f"User wins: {user_wins}")
# print(f"Computer wins: {computer_wins}")

# principal = input("Enter the principal amount: ")
# principal = float(principal)
# interest_rate = input("Enter the annual interest rate (as a decimal): ")
# interest_rate = float(interest_rate)

# n = input("Enter the number of times interest is compounded per year: ")
# n = int(n)

# years = input("Enter the number of years: ")
# years = int(years)

# Amount = principal * (1 + (interest_rate / n))**(n*years)

# print(f"Principal amount: {principal}")
# print(f"Annual interest rate: {interest_rate}")
# print(f"Times interest compounded per year: {n}")
# print(f"Amount after {years} years: {Amount}")

# def money(principal: float, interest_rate: float, n: int, years: int) -> float:
#     return principal * (1 + (interest_rate / n))**(n*years)

# print(money(principal, interest_rate, n, years))

# print(f"Amount after {years} years: {money(principal, interest_rate, n, years)}")

# import random

# for _ in range(50, 100):

#      computer = random.choice(list(range(50, 100)))

#      with open("computer_choices.txt", "w") as file:
#          file.write(f"{computer}\n")

#      print(f"Computer chose: {computer}")


import random

with open("computer_choices.txt", "w") as file:
    for _ in range(100):
        random_number = random.randint(50, 100)
        file.write(str(random_number) + "\n")
        # file.write(f"{random_number}\n")
        # print(f"Computer chose: {random_number}")

with open('computer_choices.txt', 'r') as file:
   line = file.readline()
   count = 0
   minimum = 1000
   maximum = 0
   sum = 0
   while line:
       number = int(line.strip())
       if number < minimum:
           minimum = number
       if number > maximum:
           maximum = number
       sum += number
       count += 1
       line = file.readline()

   print(f"Minimum: {minimum}")
   print(f"Maximum: {maximum}")
   print(f"Sum: {sum}")
   if count > 0:
       print(f"Average: {sum / count}")