"""
Lesson 10: Lists and List Methods
Lists are ordered, mutable collections that can store multiple items.
Python provides many useful methods for working with lists.
"""

print("=== CREATING AND ACCESSING LISTS ===\n")

# Create a list
fruits = ["apple", "banana", "cherry"]
print(f"Original list: {fruits}")

# Access elements by index (starts at 0)
print(f"First fruit: {fruits[0]}")
print(f"Second fruit: {fruits[1]}")
print(f"Last fruit: {fruits[-1]}")  # Negative index counts from the end

print("\n=== MODIFYING LISTS ===\n")

# Append an item to the end
fruits.append("orange")
print(f"After append('orange'): {fruits}")

# Insert at a specific position
fruits.insert(1, "mango")  # Insert at index 1
print(f"After insert(1, 'mango'): {fruits}")

# Remove a specific item
fruits.remove("banana")
print(f"After remove('banana'): {fruits}")

# Pop removes and returns the last item (or item at index)
last_item = fruits.pop()
print(f"Popped item: {last_item}")
print(f"After pop(): {fruits}")

print("\n=== LIST OPERATIONS ===\n")

numbers = [3, 1, 4, 1, 5, 9, 2, 6]
print(f"Number list: {numbers}")

# Sort the list (modifies original)
numbers.sort()
print(f"After sort(): {numbers}")

# Reverse the list
numbers.reverse()
print(f"After reverse(): {numbers}")

# Count occurrences of an element
print(f"Count of 1: {numbers.count(1)}")

# Find index of an element
print(f"Index of 5: {numbers.index(5)}")

print("\n=== SLICING ===\n")

letters = ["a", "b", "c", "d", "e", "f"]
print(f"Full list: {letters}")
print(f"First three: {letters[:3]}")  # From start to index 3 (not included)
print(f"Last three: {letters[-3:]}")  # Last 3 elements
print(f"Middle items: {letters[2:5]}")  # Index 2 to 5 (not included)
print(f"Every second item: {letters[::2]}")  # Step of 2

print("\n=== LIST MEMBERSHIP ===\n")

# Check if an item is in the list
print(f"Is 'apple' in fruits? {'apple' in fruits}")
print(f"Is 'grape' in fruits? {'grape' in fruits}")

print("\n=== LIST LENGTH AND SUM ===\n")

scores = [85, 92, 78, 90, 88]
print(f"Scores: {scores}")
print(f"Number of scores: {len(scores)}")
print(f"Total of all scores: {sum(scores)}")
print(f"Average score: {sum(scores) / len(scores):.2f}")
print(f"Highest score: {max(scores)}")
print(f"Lowest score: {min(scores)}")

print("\n=== COPYING LISTS ===\n")

original = [1, 2, 3]
copy1 = original.copy()  # Create a copy
copy2 = original[:]  # Another way to copy

copy1.append(4)
print(f"Original: {original}")
print(f"Copy with append: {copy1}")

print("\n=== EXTENDING LISTS ===\n")

list1 = [1, 2, 3]
list2 = [4, 5, 6]
print(f"List 1: {list1}")
print(f"List 2: {list2}")

# Extend adds all elements from another list
list1.extend(list2)
print(f"After list1.extend(list2): {list1}")

# You can also use + operator
list3 = [7, 8] + [9, 10]
print(f"[7, 8] + [9, 10] = {list3}")

print("\n=== CLEARING LISTS ===\n")

temp_list = [1, 2, 3, 4, 5]
print(f"Before clear: {temp_list}")
temp_list.clear()
print(f"After clear(): {temp_list}")
