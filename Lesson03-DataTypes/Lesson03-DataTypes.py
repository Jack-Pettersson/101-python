"""
Lesson 03: Data Types
Python has several built-in data types for storing different kinds of information.
This lesson demonstrates the most common ones.
"""

print("=== BASIC DATA TYPES ===\n")

# String: Text data
string_var = "Hello, Python!"
print(f"String: {string_var}")
print(f"Type: {type(string_var)}\n")

# Integer: Whole numbers
integer_var = 42
print(f"Integer: {integer_var}")
print(f"Type: {type(integer_var)}\n")

# Float: Decimal numbers
float_var = 3.14
print(f"Float: {float_var}")
print(f"Type: {type(float_var)}\n")

# Boolean: True or False values
bool_var = True
print(f"Boolean: {bool_var}")
print(f"Type: {type(bool_var)}\n")

print("=== COLLECTION DATA TYPES ===\n")

# List: Ordered, mutable collection. Allows duplicates.
list_var = [1, 2, 3, 2]  # Notice the duplicate 2
print(f"List: {list_var}")
print(f"Type: {type(list_var)}")
print(f"Can be modified: list_var[0] = 10 would change the first element\n")

# Tuple: Ordered, immutable collection. Allows duplicates.
tuple_var = (4, 5, 6, 5)  # Notice the duplicate 5
print(f"Tuple: {tuple_var}")
print(f"Type: {type(tuple_var)}")
print(f"Cannot be modified after creation\n")

# Set: Unordered collection of unique elements. No duplicates allowed.
set_var = {7, 8, 9, 9}  # Duplicate 9 will be automatically removed
print(f"Set: {set_var}")
print(f"Type: {type(set_var)}")
print(f"Notice: duplicates are automatically removed\n")

# Dictionary: Unordered collection of key-value pairs. Keys must be unique.
dict_var = {"name": "Alice", "age": 30, "city": "NYC"}
print(f"Dictionary: {dict_var}")
print(f"Type: {type(dict_var)}")
print(f"Access values by key: dict_var['name'] = {dict_var['name']}\n")

print("=== TYPE CONVERSION ===\n")

# You can convert between types
num_string = "123"
num_int = int(num_string)  # Convert string to integer
print(f"String '{num_string}' converted to integer: {num_int}")
print(f"Type: {type(num_int)}")
