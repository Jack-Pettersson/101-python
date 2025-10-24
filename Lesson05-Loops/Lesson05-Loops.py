"""
Lesson 05: Loops
Loops allow you to repeat code multiple times.
Python has two main types of loops: for loops and while loops.
"""

print("=== EXAMPLE 1: For Loop with Range ===\n")
# For loop: Iterates over a sequence
print("Counting from 1 to 5:")
for i in range(1, 6):  # range(1, 6) generates numbers 1, 2, 3, 4, 5
    print(i)

print("\n=== EXAMPLE 2: For Loop with List ===\n")
# For loop: Iterates over a list
print("Iterating over a list of fruits:")
fruits = ["apple", "banana", "cherry", "orange"]
for fruit in fruits:
    print(f"I like {fruit}s")

print("\n=== EXAMPLE 3: For Loop with String ===\n")
# You can iterate over strings too
print("Spelling out PYTHON:")
for letter in "PYTHON":
    print(letter)

print("\n=== EXAMPLE 4: While Loop ===\n")
# While loop: Repeats as long as a condition is true
print("Counting down from 5:")
count = 5
while count > 0:
    print(count)
    count -= 1  # Decrease count by 1
print("Blast off!")

print("\n=== EXAMPLE 5: Loop with Break ===\n")
# Break: Exit the loop early
print("Searching for the number 7:")
for num in range(1, 11):
    print(f"Checking {num}...")
    if num == 7:
        print("Found it!")
        break  # Exit the loop

print("\n=== EXAMPLE 6: Loop with Continue ===\n")
# Continue: Skip the rest of the current iteration
print("Print only odd numbers from 1 to 10:")
for num in range(1, 11):
    if num % 2 == 0:  # If number is even
        continue  # Skip to next iteration
    print(num)

print("\n=== EXAMPLE 7: Nested Loops ===\n")
# Loops inside loops
print("Multiplication table (1-3):")
for i in range(1, 4):
    for j in range(1, 4):
        print(f"{i} x {j} = {i*j}")
    print()  # Empty line after each row
