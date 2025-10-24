# Lesson12-FileInputOutput

This lesson introduces file input and output (I/O) in Python. It explains how to read from and write to files using the `open()` function and context managers (`with` statement) for safe file handling.

## Key Concepts

- Opening files with the `open()` function
- File modes: `'r'` (read), `'w'` (write), `'a'` (append)
- Using `with` statements for automatic file closing
- Reading file contents with `read()`
- Writing data to files with `write()`
- The importance of proper file handling

## Code Explanation

The script demonstrates:
- How to write text to a file.
- How to read text from a file.
- The use of the `with` statement for safe file handling.
- The difference between write (`'w'`), append (`'a'`), and read (`'r'`) modes.
- The `with` statement ensures files are properly closed even if an error occurs.

## Expected Output

```
=== EXAMPLE 1: Writing to a File ===

File 'example.txt' has been created and written to.

=== EXAMPLE 2: Reading from a File ===

File contents:
Hello, file!
This is a second line.
Python makes file handling easy!

=== EXAMPLE 3: Reading Line by Line ===

Reading line by line:
Line 1: Hello, file!
Line 2: This is a second line.
Line 3: Python makes file handling easy!

=== EXAMPLE 4: Reading Lines into a List ===

Number of lines: 3
Lines as list: ['Hello, file!\n', 'This is a second line.\n', 'Python makes file handling easy!\n']

=== EXAMPLE 5: Appending to a File ===

New lines have been appended to 'example.txt'.

Updated file contents:
Hello, file!
This is a second line.
Python makes file handling easy!
This line was appended.
And so was this one!

=== EXAMPLE 6: Writing Multiple Lines at Once ===

File 'list_output.txt' created with multiple lines.
Contents of 'list_output.txt':
First line from list
Second line from list
Third line from list

=== EXAMPLE 7: Working with CSV-like Data ===

File 'data.txt' created with structured data.

Parsing structured data:
  Alice is 30 years old and lives in New York
  Bob is 25 years old and lives in Boston
  Carol is 28 years old and lives in Chicago

=== EXAMPLE 8: Checking if File Exists ===

✓ 'example.txt' exists
  File size: 117 bytes

All file operations completed successfully!
```

After running the script, you'll find several files created in the lesson directory:
- `example.txt` - Main demonstration file
- `list_output.txt` - File created from a list
- `data.txt` - Structured CSV-like data

## How to Run

1. Open a terminal and navigate to the `Lesson12-FileInputOutput` directory.
2. Run the script with:

   ```sh
      python3 Lesson12-FileInputOutput.py
   ```

````
   ```

Observe the output and check the created file to see how file I/O works.
