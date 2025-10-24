"""
Lesson 02: Variables
Variables are containers for storing data values.
Python is dynamically typed - you don't need to declare variable types.
"""

# String variable - stores text
message = "This is a string variable!"
print(message)

# You can change the value of a variable
message = "The message has changed!"
print(message)

# Different types of variables
name = "Alice"          # String
age = 25                # Integer
height = 5.6            # Float
is_student = True       # Boolean

# Print all variables
print(f"\nName: {name}")
print(f"Age: {age}")
print(f"Height: {height} feet")
print(f"Is student: {is_student}")

# Variables can be used in calculations
birth_year = 2024 - age
print(f"\n{name} was born in {birth_year}")
