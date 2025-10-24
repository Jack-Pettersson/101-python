# Lesson11-DictionariesAndMethods

This lesson introduces dictionaries and common dictionary methods in Python. It explains how to create dictionaries, access and modify values, and use methods to work with key-value pairs efficiently.

## Key Concepts

- Creating dictionaries with key-value pairs
- Accessing values using keys
- Common dictionary methods: `keys()`, `values()`, `items()`, `get()`, `update()`, `pop()`
- Adding and modifying dictionary entries
- Checking for key existence with the `in` operator
- Dictionaries are mutable and unordered (before Python 3.7) / insertion-ordered (Python 3.7+)

## Code Explanation

The script demonstrates:
- How to create a dictionary and access values by key.
- How to add, update, and remove key-value pairs.
- How to use methods like `keys()`, `values()`, `items()`, `get()`, and `update()`.
- How to check if a key exists in a dictionary.
- The `get()` method provides a safe way to access values (returns `None` if key doesn't exist).

## Expected Output

```
=== CREATING AND ACCESSING DICTIONARIES ===

Original dictionary: {'name': 'Alice', 'age': 30, 'city': 'New York'}
Name: Alice
Age: 30

=== ADDING AND MODIFYING ===

After adding email: {'name': 'Alice', 'age': 30, 'city': 'New York', 'email': 'alice@example.com'}
After updating age: {'name': 'Alice', 'age': 31, 'city': 'New York', 'email': 'alice@example.com'}
After update(): {'name': 'Alice', 'age': 31, 'city': 'Boston', 'email': 'alice@example.com', 'phone': '555-1234'}

=== REMOVING ITEMS ===

Removed value: 555-1234
After removing phone: {'name': 'Alice', 'age': 31, 'city': 'Boston', 'email': 'alice@example.com'}
After del person['city']: {'name': 'Alice', 'age': 31, 'email': 'alice@example.com'}

=== DICTIONARY METHODS ===

Keys: ['name', 'age', 'email']
Values: ['Alice', 31, 'alice@example.com']
Items (key-value pairs): [('name', 'Alice'), ('age', 31), ('email', 'alice@example.com')]

=== SAFE ACCESS WITH get() ===

Email (using get): alice@example.com
Phone (using get): None
Phone with default: N/A

=== CHECKING FOR KEYS ===

Is 'age' a key? True
Is 'phone' a key? False

=== ITERATING OVER DICTIONARIES ===

Iterating over keys:
  name
  age
  email

Iterating over values:
  Alice
  31
  alice@example.com

Iterating over key-value pairs:
  name: Alice
  age: 31
  email: alice@example.com

=== NESTED DICTIONARIES ===

Students dictionary:
  student1: Bob - Grade: 85
  student2: Carol - Grade: 92
  student3: David - Grade: 78

=== DICTIONARY COMPREHENSION ===

Squares dictionary: {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}

=== COPYING DICTIONARIES ===

Original: {'a': 1, 'b': 2}
Copy: {'a': 1, 'b': 2, 'c': 3}

=== CLEARING DICTIONARIES ===

Before clear: {'x': 10, 'y': 20}
After clear(): {}
```

## How to Run

1. Open a terminal and navigate to the `Lesson11-DictionariesAndMethods` directory.
2. Run the script with:

   ```sh
      python3 Lesson11-DictionariesAndMethods.py
   ```

````
   ```

Observe the output to see how dictionaries and their methods work.
