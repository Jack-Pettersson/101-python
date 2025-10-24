# Demonstration of error handling in Python

print("=== Example 1: Handling ValueError ===")
try:
    number = int(input("Enter a number: "))
    print(f"You entered: {number}")
except ValueError:
    print("That was not a valid integer!")
finally:
    print("This always runs, no matter what.\n")

print("=== Example 2: Handling ZeroDivisionError ===")
try:
    numerator = 10
    denominator = int(input("Enter a denominator: "))
    result = numerator / denominator
    print(f"Result: {numerator} / {denominator} = {result}")
except ZeroDivisionError:
    print("Error: Cannot divide by zero!")
except ValueError:
    print("Error: Please enter a valid number!")
print()

print("=== Example 3: Handling Multiple Exceptions ===")
try:
    numbers = [1, 2, 3]
    index = int(input("Enter an index (0-2): "))
    print(f"Value at index {index}: {numbers[index]}")
except ValueError:
    print("Error: Please enter a valid integer!")
except IndexError:
    print("Error: Index out of range!")
except Exception as e:
    print(f"An unexpected error occurred: {e}")
finally:
    print("Exception handling demonstration complete.")
