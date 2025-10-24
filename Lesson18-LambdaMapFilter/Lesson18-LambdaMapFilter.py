"""
Lesson 18: Lambda Functions, Map, and Filter
Lambda functions are small anonymous functions.
Map and filter are functional programming tools for processing sequences.
"""

print("=== EXAMPLE 1: Lambda Functions Basics ===\n")

# Regular function
def square_func(x):
    return x ** 2

# Lambda function (anonymous, inline)
square_lambda = lambda x: x ** 2

print(f"Regular function: square_func(5) = {square_func(5)}")
print(f"Lambda function: square_lambda(5) = {square_lambda(5)}")

# Lambda with multiple arguments
add = lambda x, y: x + y
print(f"Lambda add: add(3, 7) = {add(3, 7)}")

multiply = lambda x, y, z: x * y * z
print(f"Lambda multiply: multiply(2, 3, 4) = {multiply(2, 3, 4)}")

print("\n=== EXAMPLE 2: map() Function ===\n")

# map() applies a function to every item in an iterable
numbers = [1, 2, 3, 4, 5]

# Using map with lambda
squares = list(map(lambda x: x ** 2, numbers))
print(f"Numbers: {numbers}")
print(f"Squares (map + lambda): {squares}")

# Using map with regular function
cubes = list(map(lambda x: x ** 3, numbers))
print(f"Cubes (map + lambda): {cubes}")

# Map with multiple iterables
list1 = [1, 2, 3]
list2 = [10, 20, 30]
sums = list(map(lambda x, y: x + y, list1, list2))
print(f"\nList 1: {list1}")
print(f"List 2: {list2}")
print(f"Sums (map): {sums}")

print("\n=== EXAMPLE 3: filter() Function ===\n")

# filter() selects items that pass a condition
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Filter even numbers
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print(f"Numbers: {numbers}")
print(f"Even numbers (filter): {even_numbers}")

# Filter numbers greater than 5
greater_than_five = list(filter(lambda x: x > 5, numbers))
print(f"Numbers > 5 (filter): {greater_than_five}")

# Filter strings by length
words = ["apple", "banana", "cat", "dog", "elephant"]
long_words = list(filter(lambda word: len(word) > 4, words))
print(f"\nWords: {words}")
print(f"Words longer than 4 chars: {long_words}")

print("\n=== EXAMPLE 4: Combining map() and filter() ===\n")

# First filter, then transform
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Get squares of even numbers only
even_squares = list(map(lambda x: x ** 2, filter(lambda x: x % 2 == 0, numbers)))
print(f"Squares of even numbers: {even_squares}")

# Get doubled odd numbers
odd_doubled = list(map(lambda x: x * 2, filter(lambda x: x % 2 != 0, numbers)))
print(f"Doubled odd numbers: {odd_doubled}")

print("\n=== EXAMPLE 5: Lambda with Sorting ===\n")

# Sort by custom criteria
students = [
    {"name": "Alice", "age": 25, "grade": 85},
    {"name": "Bob", "age": 22, "grade": 92},
    {"name": "Carol", "age": 23, "grade": 78}
]

# Sort by grade (ascending)
by_grade = sorted(students, key=lambda s: s["grade"])
print("Sorted by grade:")
for student in by_grade:
    print(f"  {student['name']}: {student['grade']}")

# Sort by age (descending)
by_age = sorted(students, key=lambda s: s["age"], reverse=True)
print("\nSorted by age (descending):")
for student in by_age:
    print(f"  {student['name']}: {student['age']}")

print("\n=== EXAMPLE 6: reduce() Function ===\n")

from functools import reduce

# reduce() applies a function cumulatively to items
numbers = [1, 2, 3, 4, 5]

# Calculate product of all numbers
product = reduce(lambda x, y: x * y, numbers)
print(f"Numbers: {numbers}")
print(f"Product (reduce): {product}")

# Find maximum
maximum = reduce(lambda x, y: x if x > y else y, numbers)
print(f"Maximum (reduce): {maximum}")

print("\n=== EXAMPLE 7: Practical Examples ===\n")

# Convert temperatures from Celsius to Fahrenheit
celsius = [0, 10, 20, 30, 40]
fahrenheit = list(map(lambda c: (c * 9/5) + 32, celsius))
print(f"Celsius: {celsius}")
print(f"Fahrenheit: {fahrenheit}")

# Extract email domains
emails = ["alice@gmail.com", "bob@yahoo.com", "carol@hotmail.com"]
domains = list(map(lambda email: email.split("@")[1], emails))
print(f"\nEmails: {emails}")
print(f"Domains: {domains}")

# Filter and transform names
names = ["alice", "BOB", "Carol", "DAVID", "eve"]
capitalized = list(map(lambda n: n.capitalize(), 
                       filter(lambda n: len(n) > 3, names)))
print(f"\nNames: {names}")
print(f"Capitalized (>3 chars): {capitalized}")

print("\n=== EXAMPLE 8: When NOT to Use Lambda ===\n")

# Bad: Complex lambda (hard to read)
complex_bad = lambda x: x ** 2 if x > 0 else -x ** 2 if x < 0 else 0

# Good: Regular function (more readable)
def complex_good(x):
    if x > 0:
        return x ** 2
    elif x < 0:
        return -x ** 2
    else:
        return 0

test_value = -5
print(f"Complex lambda result: {complex_bad(test_value)}")
print(f"Regular function result: {complex_good(test_value)}")
print("\nRule: Use lambda for simple operations, regular functions for complex logic!")

print("\n=== EXAMPLE 9: List Comprehension vs Map/Filter ===\n")

numbers = [1, 2, 3, 4, 5]

# Same result, different approaches
map_result = list(map(lambda x: x ** 2, numbers))
comprehension_result = [x ** 2 for x in numbers]

print(f"Map approach: {map_result}")
print(f"Comprehension: {comprehension_result}")
print(f"Results are equal: {map_result == comprehension_result}")

# Filter comparison
filter_result = list(filter(lambda x: x % 2 == 0, numbers))
comp_filter = [x for x in numbers if x % 2 == 0]

print(f"\nFilter approach: {filter_result}")
print(f"Comprehension: {comp_filter}")
print(f"Results are equal: {filter_result == comp_filter}")
print("\nNote: List comprehensions are often preferred in Python for readability!")
