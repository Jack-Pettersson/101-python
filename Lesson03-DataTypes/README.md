````markdown
# Lesson03-DataTypes

This lesson demonstrates the basic data types in Python. For each data type, a variable is declared, its value is printed, and its type is displayed using the `type()` function.

## Key Concepts

- Understanding Python's fundamental data types
- Using the `type()` function to inspect data types
- Differences between mutable and immutable data structures
- Collection types: Lists, Tuples, Sets, and Dictionaries

## Code Explanation

The script covers:

- **Integer** (`int`): Whole numbers
- **Float** (`float`): Decimal numbers
- **String** (`str`): Text data
- **Boolean** (`bool`): True/False values
- **List**: Ordered and mutable (can be changed). Allows duplicates.
- **Tuple**: Ordered and immutable (cannot be changed). Allows duplicates.
- **Set**: Unordered collection of unique elements (no duplicates).
- **Dictionary**: Unordered collection of key-value pairs. Keys must be unique.

### Differences Between Collection Types

- **List**: Ordered and mutable (can be changed after creation). Allows duplicate elements. Defined with square brackets `[ ]`.
- **Tuple**: Ordered and immutable (cannot be changed after creation). Allows duplicate elements. Defined with parentheses `( )`.
- **Set**: Unordered collection of unique elements (no duplicates). Defined with curly braces `{ }`.
- **Dictionary**: Unordered collection of key-value pairs. Keys must be unique. Defined with curly braces `{ }` and colons `:` to separate keys and values.

## Expected Output

## Expected Output

```
=== BASIC DATA TYPES ===

String: Hello, Python!
Type: <class 'str'>

Integer: 42
Type: <class 'int'>

Float: 3.14
Type: <class 'float'>

Boolean: True
Type: <class 'bool'>

=== COLLECTION DATA TYPES ===

List: [1, 2, 3, 2]
Type: <class 'list'>
Can be modified: list_var[0] = 10 would change the first element

Tuple: (4, 5, 6, 5)
Type: <class 'tuple'>
Cannot be modified after creation

Set: {8, 9, 7}
Type: <class 'set'>
Notice: duplicates are automatically removed

Dictionary: {'name': 'Alice', 'age': 30, 'city': 'NYC'}
Type: <class 'dict'>
Access values by key: dict_var['name'] = Alice

=== TYPE CONVERSION ===

String '123' converted to integer: 123
Type: <class 'int'>
```

Note: Set elements may appear in a different order since sets are unordered.

## How to Run

1. Open a terminal and navigate to the `Lesson03-DataTypes` directory.
2. Run the script with:

   ```sh
   python3 Lesson03-DataTypes.py
   ```

````
   ```

You will see the value and type of each variable printed to the console.
