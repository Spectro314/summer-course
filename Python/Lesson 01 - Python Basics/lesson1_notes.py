pi = 3.14
diameter_pizza = input("Enter the diameter of the pizza: ")
radius_pizza = float(diameter_pizza) / 2
area_pizza = pi * radius_pizza ** 2
print("The area of the pizza is:", area_pizza)
price_pizza = input("Enter the price of the pizza: ")
print("The price of the pizza is:", price_pizza)

price_pizza = float(price_pizza)
price_per_square_inch = price_pizza / area_pizza
print("The price per square inch of the pizza is:", price_per_square_inch)  cd

