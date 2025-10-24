"""
Lesson 11: Dictionaries and Dictionary Methods
Dictionaries store data as key-value pairs.
They're perfect for organizing related information and fast lookups.
"""

print("=== CREATING AND ACCESSING DICTIONARIES ===\n")

# Create a dictionary
person = {"name": "Alice", "age": 30, "city": "New York"}
print(f"Original dictionary: {person}")

# Access a value by key
print(f"Name: {person['name']}")
print(f"Age: {person['age']}")

print("\n=== ADDING AND MODIFYING ===\n")

# Add a new key-value pair
person["email"] = "alice@example.com"
print(f"After adding email: {person}")

# Update a value
person["age"] = 31
print(f"After updating age: {person}")

# Update multiple values at once
person.update({"city": "Boston", "phone": "555-1234"})
print(f"After update(): {person}")

print("\n=== REMOVING ITEMS ===\n")

# Remove a key-value pair with pop()
removed_value = person.pop("phone")
print(f"Removed value: {removed_value}")
print(f"After removing phone: {person}")

# Delete a key with del
del person["city"]
print(f"After del person['city']: {person}")

print("\n=== DICTIONARY METHODS ===\n")

# Dictionary methods
print(f"Keys: {list(person.keys())}")
print(f"Values: {list(person.values())}")
print(f"Items (key-value pairs): {list(person.items())}")

print("\n=== SAFE ACCESS WITH get() ===\n")

# Get method (safe way to access - returns None if key doesn't exist)
print(f"Email (using get): {person.get('email')}")
print(f"Phone (using get): {person.get('phone')}")  # Returns None
print(f"Phone with default: {person.get('phone', 'N/A')}")  # Returns default

print("\n=== CHECKING FOR KEYS ===\n")

# Check if a key exists
print(f"Is 'age' a key? {'age' in person}")
print(f"Is 'phone' a key? {'phone' in person}")

print("\n=== ITERATING OVER DICTIONARIES ===\n")

print("Iterating over keys:")
for key in person.keys():
    print(f"  {key}")

print("\nIterating over values:")
for value in person.values():
    print(f"  {value}")

print("\nIterating over key-value pairs:")
for key, value in person.items():
    print(f"  {key}: {value}")

print("\n=== NESTED DICTIONARIES ===\n")

# Dictionary containing dictionaries
students = {
    "student1": {"name": "Bob", "grade": 85},
    "student2": {"name": "Carol", "grade": 92},
    "student3": {"name": "David", "grade": 78}
}

print("Students dictionary:")
for student_id, info in students.items():
    print(f"  {student_id}: {info['name']} - Grade: {info['grade']}")

print("\n=== DICTIONARY COMPREHENSION ===\n")

# Create dictionary from lists
numbers = [1, 2, 3, 4, 5]
squares_dict = {n: n**2 for n in numbers}
print(f"Squares dictionary: {squares_dict}")

print("\n=== COPYING DICTIONARIES ===\n")

original_dict = {"a": 1, "b": 2}
copied_dict = original_dict.copy()
copied_dict["c"] = 3

print(f"Original: {original_dict}")
print(f"Copy: {copied_dict}")

print("\n=== CLEARING DICTIONARIES ===\n")

temp_dict = {"x": 10, "y": 20}
print(f"Before clear: {temp_dict}")
temp_dict.clear()
print(f"After clear(): {temp_dict}")
