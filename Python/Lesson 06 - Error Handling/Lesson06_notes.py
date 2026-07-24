import random

with open("computer_choices.txt", "w") as file:
    for _ in range(100):
        random_number = random.randint(0, 1000)
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
       number = line.strip()
       number = int(number)
       print(f"Read number: {number}")
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