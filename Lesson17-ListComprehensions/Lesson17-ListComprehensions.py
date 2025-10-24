"""
Lesson 17: List Comprehensions
List comprehensions provide a concise way to create lists.
They're more readable and often faster than traditional loops.
"""

print("=== EXAMPLE 1: Basic List Comprehension ===\n")

# Traditional way with for loop
squares_loop = []
for x in range(1, 6):
    squares_loop.append(x**2)
print(f"Squares (loop): {squares_loop}")

# List comprehension way (more Pythonic)
squares = [x**2 for x in range(1, 6)]
print(f"Squares (comprehension): {squares}")

print("\n=== EXAMPLE 2: List Comprehension with Condition ===\n")

# Get only even numbers squared
even_squares = [x**2 for x in range(1, 11) if x % 2 == 0]
print(f"Even squares from 1-10: {even_squares}")

# Traditional equivalent
even_squares_loop = []
for x in range(1, 11):
    if x % 2 == 0:
        even_squares_loop.append(x**2)
print(f"Even squares (loop): {even_squares_loop}")

print("\n=== EXAMPLE 3: Transforming Strings ===\n")

words = ["hello", "world", "python", "programming"]

# Convert all to uppercase
upper_words = [word.upper() for word in words]
print(f"Uppercase: {upper_words}")

# Get word lengths
word_lengths = [len(word) for word in words]
print(f"Lengths: {word_lengths}")

# Get first letter of each word
first_letters = [word[0] for word in words]
print(f"First letters: {first_letters}")

print("\n=== EXAMPLE 4: Filtering Lists ===\n")

numbers = [1, -2, 3, -4, 5, -6, 7, -8, 9, -10]

# Get only positive numbers
positives = [num for num in numbers if num > 0]
print(f"Positive numbers: {positives}")

# Get only negative numbers
negatives = [num for num in numbers if num < 0]
print(f"Negative numbers: {negatives}")

print("\n=== EXAMPLE 5: Mathematical Operations ===\n")

# Create Fahrenheit temperatures
celsius = [0, 10, 20, 30, 40]
fahrenheit = [(temp * 9/5) + 32 for temp in celsius]
print(f"Celsius: {celsius}")
print(f"Fahrenheit: {fahrenheit}")

# Create a multiplication table
row = 5
table = [row * i for i in range(1, 11)]
print(f"\nMultiplication table for {row}: {table}")

print("\n=== EXAMPLE 6: Nested List Comprehension ===\n")

# Create a 3x3 matrix
matrix = [[i * j for j in range(1, 4)] for i in range(1, 4)]
print("3x3 multiplication matrix:")
for row in matrix:
    print(row)

# Flatten a nested list
nested = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
flattened = [num for sublist in nested for num in sublist]
print(f"\nNested list: {nested}")
print(f"Flattened: {flattened}")

print("\n=== EXAMPLE 7: Conditional Expression (Ternary) ===\n")

# Use if-else in comprehension
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
labels = ["even" if num % 2 == 0 else "odd" for num in numbers]
print(f"Numbers: {numbers}")
print(f"Labels: {labels}")

# Replace negative numbers with zero
values = [5, -3, 8, -1, 2, -7]
non_negative = [val if val >= 0 else 0 for val in values]
print(f"\nOriginal: {values}")
print(f"Non-negative: {non_negative}")

print("\n=== EXAMPLE 8: Working with Strings ===\n")

sentence = "The quick brown fox jumps over the lazy dog"

# Get words longer than 3 characters
long_words = [word for word in sentence.split() if len(word) > 3]
print(f"Words longer than 3 chars: {long_words}")

# Get words that start with a vowel
vowels = "aeiouAEIOU"
vowel_words = [word for word in sentence.split() if word[0] in vowels]
print(f"Words starting with vowel: {vowel_words}")

print("\n=== EXAMPLE 9: Set and Dictionary Comprehensions ===\n")

# Set comprehension (unique values only)
numbers = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4]
unique_squares = {x**2 for x in numbers}
print(f"Original: {numbers}")
print(f"Unique squares (set): {unique_squares}")

# Dictionary comprehension
words = ["apple", "banana", "cherry"]
word_lengths_dict = {word: len(word) for word in words}
print(f"\nWord lengths (dict): {word_lengths_dict}")

# Create a dictionary from two lists
keys = ["name", "age", "city"]
values = ["Alice", 30, "New York"]
person_dict = {k: v for k, v in zip(keys, values)}
print(f"Person dictionary: {person_dict}")

print("\n=== EXAMPLE 10: Performance Comparison ===\n")

import time

# Measure time for loop
start = time.time()
loop_result = []
for i in range(100000):
    loop_result.append(i**2)
loop_time = time.time() - start

# Measure time for comprehension
start = time.time()
comp_result = [i**2 for i in range(100000)]
comp_time = time.time() - start

print(f"Loop time: {loop_time:.6f} seconds")
print(f"Comprehension time: {comp_time:.6f} seconds")
print(f"Comprehension is {loop_time/comp_time:.2f}x faster!")
