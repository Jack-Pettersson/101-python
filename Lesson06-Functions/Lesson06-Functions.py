"""
Lesson 06: Functions
Functions are reusable blocks of code that perform specific tasks.
They help organize code and avoid repetition.
"""

print("=== EXAMPLE 1: Simple Function ===\n")

def greet(name):
    """Prints a greeting to the user."""
    print(f"Hello, {name}!")

# Call the function
greet("Alice")
greet("Bob")

print("\n=== EXAMPLE 2: Function with Return Value ===\n")

def add(a, b):
    """Returns the sum of a and b."""
    return a + b

# Store the returned value in a variable
result = add(3, 5)
print(f"3 + 5 = {result}")

result2 = add(10, 20)
print(f"10 + 20 = {result2}")

print("\n=== EXAMPLE 3: Function with Default Parameters ===\n")

def greet_with_title(name, title="Mr."):
    """Greets a person with an optional title."""
    print(f"Hello, {title} {name}!")

greet_with_title("Smith")  # Uses default title "Mr."
greet_with_title("Johnson", "Dr.")  # Uses custom title "Dr."
greet_with_title("Davis", "Ms.")

print("\n=== EXAMPLE 4: Function with Multiple Return Values ===\n")

def calculate(a, b):
    """Returns multiple calculations at once."""
    sum_result = a + b
    diff_result = a - b
    prod_result = a * b
    return sum_result, diff_result, prod_result

# Unpack multiple return values
sum_val, diff_val, prod_val = calculate(10, 3)
print(f"10 + 3 = {sum_val}")
print(f"10 - 3 = {diff_val}")
print(f"10 * 3 = {prod_val}")

print("\n=== EXAMPLE 5: Function That Calls Another Function ===\n")

def square(x):
    """Returns the square of x."""
    return x * x

def sum_of_squares(a, b):
    """Returns the sum of the squares of a and b."""
    return square(a) + square(b)

result = sum_of_squares(3, 4)
print(f"3² + 4² = {result}")

print("\n=== EXAMPLE 6: Function with Variable Number of Arguments ===\n")

def print_all(*args):
    """Prints all arguments passed to the function."""
    print("Arguments received:")
    for arg in args:
        print(f"  - {arg}")

print_all("apple", "banana", "cherry")
print()
print_all(1, 2, 3, 4, 5)
