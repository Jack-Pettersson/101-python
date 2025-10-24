"""
Lesson 12: File Input and Output
Files allow programs to save and retrieve data permanently.
The 'with' statement ensures files are properly closed.
"""

print("=== EXAMPLE 1: Writing to a File ===\n")

# Write to a file (creates new file or overwrites existing)
with open("example.txt", "w") as file:
    file.write("Hello, file!\n")
    file.write("This is a second line.\n")
    file.write("Python makes file handling easy!\n")

print("File 'example.txt' has been created and written to.")

print("\n=== EXAMPLE 2: Reading from a File ===\n")

# Read the entire file
with open("example.txt", "r") as file:
    content = file.read()
    print("File contents:")
    print(content)

print("=== EXAMPLE 3: Reading Line by Line ===\n")

# Read file line by line
with open("example.txt", "r") as file:
    print("Reading line by line:")
    for line_number, line in enumerate(file, 1):
        print(f"Line {line_number}: {line.strip()}")  # strip() removes newline

print("\n=== EXAMPLE 4: Reading Lines into a List ===\n")

# Read all lines into a list
with open("example.txt", "r") as file:
    lines = file.readlines()
    print(f"Number of lines: {len(lines)}")
    print(f"Lines as list: {lines}")

print("\n=== EXAMPLE 5: Appending to a File ===\n")

# Append to the file (adds to end without overwriting)
with open("example.txt", "a") as file:
    file.write("This line was appended.\n")
    file.write("And so was this one!\n")

print("New lines have been appended to 'example.txt'.")

# Show the updated file
with open("example.txt", "r") as file:
    print("\nUpdated file contents:")
    print(file.read())

print("=== EXAMPLE 6: Writing Multiple Lines at Once ===\n")

# Write multiple lines from a list
lines_to_write = [
    "First line from list\n",
    "Second line from list\n",
    "Third line from list\n"
]

with open("list_output.txt", "w") as file:
    file.writelines(lines_to_write)

print("File 'list_output.txt' created with multiple lines.")

# Read and display it
with open("list_output.txt", "r") as file:
    print("Contents of 'list_output.txt':")
    print(file.read())

print("=== EXAMPLE 7: Working with CSV-like Data ===\n")

# Write some structured data
with open("data.txt", "w") as file:
    file.write("Name,Age,City\n")
    file.write("Alice,30,New York\n")
    file.write("Bob,25,Boston\n")
    file.write("Carol,28,Chicago\n")

print("File 'data.txt' created with structured data.")

# Read and parse it
with open("data.txt", "r") as file:
    print("\nParsing structured data:")
    for line in file:
        parts = line.strip().split(",")
        if parts[0] != "Name":  # Skip header
            print(f"  {parts[0]} is {parts[1]} years old and lives in {parts[2]}")

print("\n=== EXAMPLE 8: Checking if File Exists ===\n")

import os

if os.path.exists("example.txt"):
    print("✓ 'example.txt' exists")
    file_size = os.path.getsize("example.txt")
    print(f"  File size: {file_size} bytes")
else:
    print("✗ 'example.txt' does not exist")

print("\nAll file operations completed successfully!")
