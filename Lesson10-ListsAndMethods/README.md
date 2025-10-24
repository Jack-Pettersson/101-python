# Lesson10-ListsAndMethods

This lesson introduces lists and common list methods in Python. It explains how to create lists, access elements, and use methods to modify and work with lists effectively.

## Key Concepts

- Creating and accessing list elements by index
- Common list methods: `append()`, `remove()`, `sort()`, `pop()`, `insert()`, `extend()`, `clear()`, `copy()`
- List slicing syntax `[start:end:step]`
- Using the `in` operator to check membership
- Built-in functions: `len()`, `sum()`, `max()`, `min()`, `count()`, `index()`
- Lists are mutable (can be modified after creation)
- Negative indices count from the end
- List copying vs. reference

## Code Explanation

The script demonstrates:
- How to create a list and access its elements by index.
- How to use methods like `append()`, `insert()`, `remove()`, and `pop()` to modify lists.
- How to use `sort()` and `reverse()` to reorder lists.
- How to use slicing to access parts of a list.
- How to check if an item is in a list with the `in` operator.
- How to use built-in functions like `len()`, `sum()`, `max()`, `min()`.
- How to copy lists properly.
- How to extend and concatenate lists.
- List indexing starts at 0 (first element is at index 0).

## Expected Output

```
=== CREATING AND ACCESSING LISTS ===

Original list: ['apple', 'banana', 'cherry']
First fruit: apple
Second fruit: banana
Last fruit: cherry

=== MODIFYING LISTS ===

After append('orange'): ['apple', 'banana', 'cherry', 'orange']
After insert(1, 'mango'): ['apple', 'mango', 'banana', 'cherry', 'orange']
After remove('banana'): ['apple', 'mango', 'cherry', 'orange']
Popped item: orange
After pop(): ['apple', 'mango', 'cherry']

=== LIST OPERATIONS ===

Number list: [3, 1, 4, 1, 5, 9, 2, 6]
After sort(): [1, 1, 2, 3, 4, 5, 6, 9]
After reverse(): [9, 6, 5, 4, 3, 2, 1, 1]
Count of 1: 2
Index of 5: 2

=== SLICING ===

Full list: ['a', 'b', 'c', 'd', 'e', 'f']
First three: ['a', 'b', 'c']
Last three: ['d', 'e', 'f']
Middle items: ['c', 'd', 'e']
Every second item: ['a', 'c', 'e']

=== LIST MEMBERSHIP ===

Is 'apple' in fruits? True
Is 'grape' in fruits? False

=== LIST LENGTH AND SUM ===

Scores: [85, 92, 78, 90, 88]
Number of scores: 5
Total of all scores: 433
Average score: 86.60
Highest score: 92
Lowest score: 78

=== COPYING LISTS ===

Original: [1, 2, 3]
Copy with append: [1, 2, 3, 4]

=== EXTENDING LISTS ===

List 1: [1, 2, 3]
List 2: [4, 5, 6]
After list1.extend(list2): [1, 2, 3, 4, 5, 6]
[7, 8] + [9, 10] = [7, 8, 9, 10]

=== CLEARING LISTS ===

Before clear: [1, 2, 3, 4, 5]
After clear(): []
```

## How to Run

1. Open a terminal and navigate to the `Lesson10-ListsAndMethods` directory.
2. Run the script with:

   ```sh
   python3 Lesson10-ListsAndMethods.py
   ```

````
   ```

Observe the output to see how lists and their methods work.
