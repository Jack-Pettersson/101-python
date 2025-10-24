# Lesson16-DatesAndTimes

This lesson introduces working with dates and times in Python using the `datetime` module. It explains how to get the current date and time, format dates, perform date arithmetic, and parse date strings, which is crucial for time-based applications.

## Key Concepts

- Using the `datetime` module for date/time operations
- Getting the current date and time with `datetime.now()`
- Formatting dates with `strftime()` (string format time)
- Parsing date strings with `strptime()` (string parse time)
- Date arithmetic with `timedelta`
- Common date format codes (`%Y`, `%m`, `%d`, `%H`, `%M`, `%S`)

## Code Explanation

The script demonstrates:
- How to get the current date and time.
- How to format dates and times as strings.
- How to parse strings into date objects.
- How to perform arithmetic with dates (e.g., adding days).
- `timedelta` represents a duration (difference between two dates/times).

## Expected Output

```
Current date and time: 2025-10-24 14:30:45.123456
Formatted date and time: 2025-10-24 14:30:45
Parsed date: 2025-10-24 00:00:00
Date one week from now: 2025-10-31 14:30:45.123456
```

Note: The actual dates and times will vary based on when you run the script.

## How to Run

1. Open a terminal and navigate to the `Lesson16-DatesAndTimes` directory.
2. Run the script with:

   ```sh
      python3 Lesson16-DatesAndTimes.py
   ```

````
   ```

Observe the output to see how dates and times are managed in Python.
