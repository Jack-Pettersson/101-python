"""
Lesson 07: Importing Modules
Modules are Python files containing functions, classes, and variables.
Python has a large standard library of built-in modules you can use.
"""

print("=== EXAMPLE 1: Import Entire Module ===\n")

# Import the whole math module
import math

print(f"Square root of 16: {math.sqrt(16)}")
print(f"Pi value: {math.pi}")
print(f"2 to the power of 3: {math.pow(2, 3)}")

print("\n=== EXAMPLE 2: Import Specific Functions ===\n")

# Import a specific function from the random module
from random import randint, choice

print(f"Random integer between 1 and 10: {randint(1, 10)}")
print(f"Random integer between 1 and 10: {randint(1, 10)}")  # Different each time

colors = ["red", "blue", "green", "yellow"]
print(f"Random color from list: {choice(colors)}")

print("\n=== EXAMPLE 3: Import Multiple Items ===\n")

# Import multiple things from a module
from math import sin, cos, tan, pi

print(f"sin(0) = {sin(0)}")
print(f"cos(0) = {cos(0)}")
print(f"tan(pi/4) = {tan(pi/4)}")

print("\n=== EXAMPLE 4: Import with Alias ===\n")

# Use 'as' to rename an import (shorter name)
import random as rnd

print(f"Random float between 0 and 1: {rnd.random()}")
print(f"Random choice from 1-100: {rnd.randint(1, 100)}")

print("\n=== EXAMPLE 5: Using the datetime Module ===\n")

from datetime import datetime, date

now = datetime.now()
print(f"Current date and time: {now}")

today = date.today()
print(f"Today's date: {today}")
print(f"Year: {today.year}, Month: {today.month}, Day: {today.day}")

print("\n=== EXAMPLE 6: Using the os Module ===\n")

import os

print(f"Current working directory: {os.getcwd()}")
print(f"Operating system: {os.name}")
