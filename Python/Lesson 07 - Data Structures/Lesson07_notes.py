# import random

# with open('preclass_problem1_data.txt', 'r') as input_file:  
#     lines = input_file.readlines()
   
#     count = 0
#     min = 100
#     max = 0
#     sum = 0
#     for line in lines:
#         amount = int(line)
#         sum += amount
#         count += 1
#         if amount > max:
#             max = amount
#         if amount < min:
#             min = amount
#     average = sum/ count
#     print("Count:", count)
#     print("Min:", min)
#     print("Max:", max)
#     print("Sum:", sum)
#     print("Average:", average)

# signal = []
# with open("preclass_problem1_data.txt", "r") as input_file:
#     for line in input_file:
#         value = int(line)
#         signal.append(value)
# signal_sorted = sorted(signal, reverse=True)
# high_5 = signal_sorted[:5]
# coordinate = sum(high_5) / 10
# print("High 5:", high_5)
# print(f"The Coordinate is: {coordinate}")

# with open("preclass_problem1_data.txt", "r") as in_file:
#     print(f"The coordinate is: {sum(sorted(int(x) for x in in_file) [-5:]) / 10}")
    