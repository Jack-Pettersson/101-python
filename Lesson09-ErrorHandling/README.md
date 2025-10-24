````markdown
# Lesson09-ErrorHandling

This lesson introduces error handling in Python. It explains how to use try, except, and finally blocks to handle exceptions and make your programs more robust and user-friendly.

## Key Concepts

- Using `try` blocks to wrap code that might raise an exception
- Catching specific exceptions with `except` blocks
- Handling multiple exception types
- Using `finally` blocks for cleanup code that always runs
- The general `Exception` class as a catch-all

## Code Explanation

The script demonstrates:
- **Example 1**: Handling `ValueError` when converting user input to an integer.
- **Example 2**: Handling `ZeroDivisionError` and `ValueError` in division operations.
- **Example 3**: Handling `IndexError` when accessing list elements and catching multiple exception types.
- How to use a `finally` block to execute code whether an error occurred or not.
- Why error handling is important for creating user-friendly programs.

## Expected Output

The program will prompt you for input multiple times. Try entering:
- Valid numbers
- Invalid text (like "abc")
- Zero for the denominator
- Out-of-range indices

Each example demonstrates different exception handling scenarios.

## How to Run

1. Open a terminal and navigate to the `Lesson09-ErrorHandling` directory.
2. Run the script with:

   ```sh
   python3 Lesson09-ErrorHandling.py
   ```

Follow the prompts and try entering various types of input to see error handling in action.

````
   ```

Follow the prompts and try entering invalid input to see error handling in action.
