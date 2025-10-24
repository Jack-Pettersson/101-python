# Lesson14-Inheritance

This lesson introduces inheritance in Python. It explains how to create subclasses, inherit attributes and methods from a parent class, override methods, and use the `super()` function, which are key concepts in object-oriented programming.

## Key Concepts

- Creating parent (base) and child (derived) classes
- Inheriting attributes and methods from parent classes
- Method overriding in child classes
- Using `super()` to call parent class methods
- Code reuse through inheritance
- The "is-a" relationship in OOP

## Code Explanation

The script demonstrates:
- How to define a parent class and a child class.
- How the child class inherits attributes and methods from the parent class.
- How to override a method in the child class.
- How to use `super()` to call the parent class's methods.
- Child classes can add new methods or override existing ones.

## Expected Output

```
=== EXAMPLE 1: Basic Inheritance ===

Generic Animal makes a sound.
Rex barks.
Whiskers meows.

=== EXAMPLE 2: Using super() ===

Tweety makes a sound.
Tweety also chirps.

=== EXAMPLE 3: Extending __init__() ===

Employee: John, Salary: $50000

Employee: Sarah, Salary: $80000
Department: Engineering

=== EXAMPLE 4: Multiple Levels of Inheritance ===

Tesla vehicle is starting...
Tesla Model 3 goes beep beep!
Charging Tesla Model 3 with 75 kWh battery...

=== EXAMPLE 5: Adding New Methods ===

Rectangle area: 15
Square area: 16
Square perimeter: 16

=== EXAMPLE 6: isinstance() and issubclass() ===

Is dog an Animal? True
Is dog a Dog? True
Is dog a Cat? False
Is Dog a subclass of Animal? True
Is Cat a subclass of Animal? True
Is Animal a subclass of Dog? False
```

## How to Run

1. Open a terminal and navigate to the `Lesson14-Inheritance` directory.
2. Run the script with:

   ```sh
   python3 Lesson14-Inheritance.py
   ```

Observe the output to see how inheritance works in Python.
