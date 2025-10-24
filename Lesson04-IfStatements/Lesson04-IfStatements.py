"""
Lesson 04: If Statements
Conditional statements allow your program to make decisions and execute
different code based on whether conditions are true or false.
"""

print("=== EXAMPLE 1: Basic If-Elif-Else ===\n")

# Check if a number is positive, negative, or zero
number = 10

if number > 0:
    print(f"{number} is positive.")
elif number == 0:
    print(f"{number} is zero.")
else:
    print(f"{number} is negative.")

# Try changing the value of 'number' to see different outputs
print("\n=== EXAMPLE 2: Comparison Operators ===\n")

age = 18

if age >= 18:
    print(f"Age {age}: You are an adult.")
else:
    print(f"Age {age}: You are a minor.")

print("\n=== EXAMPLE 3: Multiple Conditions ===\n")

temperature = 75

if temperature > 85:
    print("It's hot outside!")
elif temperature > 65:
    print("The weather is nice.")
elif temperature > 45:
    print("It's a bit chilly.")
else:
    print("It's cold outside!")

print("\n=== EXAMPLE 4: Logical Operators (and, or, not) ===\n")

has_ticket = True
has_id = True

if has_ticket and has_id:
    print("You can enter the venue.")
elif has_ticket and not has_id:
    print("You have a ticket but need to show ID.")
elif not has_ticket and has_id:
    print("You have ID but need a ticket.")
else:
    print("You need both a ticket and ID.")

print("\n=== EXAMPLE 5: Nested If Statements ===\n")

score = 85

if score >= 60:
    print("You passed!")
    if score >= 90:
        print("Grade: A")
    elif score >= 80:
        print("Grade: B")
    elif score >= 70:
        print("Grade: C")
    else:
        print("Grade: D")
else:
    print("You failed. Grade: F")
