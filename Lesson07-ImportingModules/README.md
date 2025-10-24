# Lesson07-ImportingModules

This lesson introduces importing modules in Python. It explains how to use Python's standard library and third-party modules to extend your programs with additional functionality.

## Key Concepts

- Importing modules with the `import` statement
- Importing specific functions or classes from a module
- Using the `as` keyword to create aliases
- Difference between importing whole modules vs. specific items
- Python's standard library (built-in modules)

## Code Explanation

The script demonstrates:
- How to import a module using the `import` statement.
- How to import specific functions or classes from a module.
- How to use functions from imported modules (e.g., `math` and `random`).
- The difference between importing the whole module and importing specific items.
- Using the `as` keyword to create module aliases for convenience.

## Expected Output

```
=== EXAMPLE 1: Import Entire Module ===

Square root of 16: 4.0
Pi value: 3.141592653589793
2 to the power of 3: 8.0

=== EXAMPLE 2: Import Specific Functions ===

Random integer between 1 and 10: 7
Random integer between 1 and 10: 3
Random color from list: blue

=== EXAMPLE 3: Import Multiple Items ===

sin(0) = 0.0
cos(0) = 1.0
tan(pi/4) = 0.9999999999999999

=== EXAMPLE 4: Import with Alias ===

Random float between 0 and 1: 0.5234567
Random choice from 1-100: 42

=== EXAMPLE 5: Using the datetime Module ===

Current date and time: 2025-10-24 15:30:45.123456
Today's date: 2025-10-24
Year: 2025, Month: 10, Day: 24

=== EXAMPLE 6: Using the os Module ===

Current working directory: /Users/jack/playground/101-python/Lesson07-ImportingModules
Operating system: posix
```

Note: The random numbers and current date/time will be different each time you run the script.

## How to Run

1. Open a terminal and navigate to the `Lesson07-ImportingModules` directory.
2. Run the script with:

   ```sh
      python3 Lesson07-ImportingModules.py
   ```

````
   ```

Observe the output to see how modules are imported and used.
