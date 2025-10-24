"""
Lesson 08: User Input
The input() function allows your program to get information from the user.
All input is received as a string, so you may need to convert it.
"""

print("=== EXAMPLE 1: String Input ===\n")

# Get a string input from the user
name = input("What is your name? ")
print(f"Hello, {name}! Nice to meet you.")

print("\n=== EXAMPLE 2: Integer Input with Conversion ===\n")

# Get a number input from the user and convert it to int
age = int(input("How old are you? "))
print(f"You are {age} years old.")

# Calculate birth year
from datetime import date
current_year = date.today().year
birth_year = current_year - age
print(f"You were born in approximately {birth_year}.")

print("\n=== EXAMPLE 3: Float Input with Calculations ===\n")

# Use input in a calculation
number = float(input("Enter a number to double: "))
doubled = number * 2
print(f"Twice your number is {doubled}")

print("\n=== EXAMPLE 4: Multiple Inputs ===\n")

# Get multiple pieces of information
favorite_color = input("What's your favorite color? ")
favorite_food = input("What's your favorite food? ")

print(f"\nGreat! Your favorite color is {favorite_color} and you love {favorite_food}.")

print("\n=== EXAMPLE 5: Yes/No Input ===\n")

# Get yes/no response and make a decision
answer = input("Do you like Python? (yes/no): ").lower()

if answer == "yes" or answer == "y":
    print("That's awesome! Python is a great language!")
elif answer == "no" or answer == "n":
    print("That's okay. Maybe you'll like it more as you learn!")
else:
    print("I didn't understand your response.")

print("\n=== EXAMPLE 6: Building a Simple Calculator ===\n")

num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
operation = input("Choose operation (+, -, *, /): ")

if operation == "+":
    result = num1 + num2
    print(f"{num1} + {num2} = {result}")
elif operation == "-":
    result = num1 - num2
    print(f"{num1} - {num2} = {result}")
elif operation == "*":
    result = num1 * num2
    print(f"{num1} * {num2} = {result}")
elif operation == "/":
    if num2 != 0:
        result = num1 / num2
        print(f"{num1} / {num2} = {result}")
    else:
        print("Error: Cannot divide by zero!")
else:
    print("Invalid operation!")
