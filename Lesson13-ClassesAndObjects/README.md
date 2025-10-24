# Lesson13-ClassesAndObjects

This lesson introduces classes and objects in Python. It explains how to define classes, create objects, use attributes and methods, and understand the concept of `self`, which are fundamental concepts in object-oriented programming (OOP).

## Key Concepts

- Defining classes with the `class` keyword
- Creating objects (instances) of a class
- The `__init__()` method (constructor) for initialization
- Instance attributes and methods
- The `self` parameter and why it's needed
- Object-oriented programming basics

## Code Explanation

The script demonstrates:
- How to define a class using the `class` keyword.
- How to create an object (instance) of a class.
- How to define and use attributes and methods.
- The role of `self` in class methods (it refers to the instance of the class).
- The `__init__()` method is called automatically when creating a new object.

## Expected Output

```
=== EXAMPLE 1: Basic Class Definition ===

Name: Alice
Age: 30
Hello, my name is Alice and I am 30 years old.

=== EXAMPLE 2: Multiple Objects ===

Hello, my name is Bob and I am 25 years old.
Hello, my name is Carol and I am 28 years old.

=== EXAMPLE 3: Class with More Methods ===

Alice's account created with $1000
Deposited $500. New balance: $1500
Withdrew $200. New balance: $1300
Insufficient funds! Balance: $1300
Final balance: $1300

=== EXAMPLE 4: Class Attributes ===

Dog 1 species: Canis familiaris
Dog 2 species: Canis familiaris
Buddy is a Golden Retriever
Lucy is a Beagle
Buddy says Woof!
Lucy says Arf!

=== EXAMPLE 5: String Representation ===

Book: 'Python Crash Course' by Eric Matthes
Detailed: Book(title='Python Crash Course', author='Eric Matthes', pages=544)

=== EXAMPLE 6: Object Comparison ===

p1: Point(3, 4)
p2: Point(3, 4)
p3: Point(5, 6)
p1 == p2: True
p1 == p3: False
```

## How to Run

1. Open a terminal and navigate to the `Lesson13-ClassesAndObjects` directory.
2. Run the script with:

   ```sh
   python3 Lesson13-ClassesAndObjects.py
   ```

Observe the output to see how classes and objects work.
