# Lesson19-CustomExceptions

This lesson introduces custom exceptions in Python. It explains how to define your own exception classes, raise them, and handle them to make your programs more robust and descriptive with application-specific error handling.

## Key Concepts

- Defining custom exception classes by inheriting from `Exception`
- Raising exceptions with the `raise` keyword
- Catching custom exceptions with try/except blocks
- Providing meaningful error messages
- When and why to create custom exceptions
- Exception hierarchy in Python

## Code Explanation

The script demonstrates:
- How to define a custom exception class by inheriting from `Exception`.
- How to raise a custom exception using `raise`.
- How to catch and handle custom exceptions with `try` and `except` blocks.
- Why custom exceptions are useful for specific error handling in your programs (they make code more readable and maintainable).

## Expected Output

```
=== EXAMPLE 1: Basic Custom Exception ===

5 is non-negative.
Custom exception caught: Number must be non-negative! Got: -3

=== EXAMPLE 2: Exception with Additional Data ===

Withdrew $50. New balance: $50
Current balance: $50
Transaction failed: Cannot withdraw $75. Current balance: $50
  Attempted: $75
  Available: $50

=== EXAMPLE 3: Multiple Custom Exceptions ===

Testing valid inputs:
✓ Email is valid: alice@example.com
✓ Age is valid: 25
✓ Username is valid: alice123
All validations passed!

Testing invalid inputs:
✗ Email validation failed: Invalid email format: invalid-email
✗ Age validation failed: Age must be between 0 and 120, got 150
✗ Username validation failed: Username must be at least 3 characters, got 'ab'

=== EXAMPLE 4: Exception Hierarchy ===

Player X placed at (0, 0)
Player O placed at (0, 1)
Invalid move: Position (0, 0) is already occupied!

=== EXAMPLE 5: Re-raising Exceptions ===

Processing: valid data
Data saved: valid data

Processing: 
Database error occurred: Cannot save empty data!
Final error handler: Failed to process '': Cannot save empty data!
Original cause: Cannot save empty data!

=== EXAMPLE 6: Exception with Cleanup ===

Opening file: data.txt
Processing data.txt...
File processed successfully!
Closing file: <File: data.txt>

Opening file: invalid_file.txt
Error occurred while processing invalid_file.txt
Closing file: <File: invalid_file.txt>

Caught exception: Cannot process file: invalid_file.txt

=== EXAMPLE 7: Interactive Exception Demo ===

✓ Temperature 25°C is within safe range (0°C - 100°C)
⚠ WARNING: Temperature 105°C exceeds safe limit of 100°C
⚠ WARNING: Temperature -10°C is below safe limit of 0°C
✓ Temperature 50°C is within safe range (0°C - 100°C)

✅ All custom exception examples completed!
```

## How to Run

1. Open a terminal and navigate to the `Lesson19-CustomExceptions` directory.
2. Run the script with:

   ```sh
   python3 Lesson19-CustomExceptions.py
   ```

````
   ```

Observe the output to see how custom exceptions work in Python.
