"""
Lesson 16: Dates and Times
The datetime module provides classes for working with dates and times.
Essential for time-based calculations and formatting.
"""

from datetime import datetime, date, time, timedelta

print("=== EXAMPLE 1: Getting Current Date and Time ===\n")

# Get the current date and time
now = datetime.now()
print(f"Current date and time: {now}")

# Get just the date
today = date.today()
print(f"Today's date: {today}")

# Get individual components
print(f"Year: {now.year}")
print(f"Month: {now.month}")
print(f"Day: {now.day}")
print(f"Hour: {now.hour}")
print(f"Minute: {now.minute}")
print(f"Second: {now.second}")

print("\n=== EXAMPLE 2: Formatting Dates ===\n")

# Format the date and time as strings
formatted1 = now.strftime("%Y-%m-%d %H:%M:%S")
print(f"Format 1: {formatted1}")

formatted2 = now.strftime("%B %d, %Y")
print(f"Format 2: {formatted2}")

formatted3 = now.strftime("%m/%d/%y %I:%M %p")
print(f"Format 3: {formatted3}")

formatted4 = now.strftime("%A, %B %d, %Y at %I:%M %p")
print(f"Format 4: {formatted4}")

print("\n=== EXAMPLE 3: Parsing Date Strings ===\n")

# Parse a date string into a datetime object
date_string = "2025-10-24"
parsed = datetime.strptime(date_string, "%Y-%m-%d")
print(f"Parsed date: {parsed}")

# Parse a more complex string
date_string2 = "October 24, 2025 3:30 PM"
parsed2 = datetime.strptime(date_string2, "%B %d, %Y %I:%M %p")
print(f"Parsed datetime: {parsed2}")

print("\n=== EXAMPLE 4: Date Arithmetic with timedelta ===\n")

# Add days to a date
future = now + timedelta(days=7)
print(f"One week from now: {future}")

# Subtract days
past = now - timedelta(days=30)
print(f"30 days ago: {past}")

# Add hours and minutes
later = now + timedelta(hours=5, minutes=30)
print(f"5 hours 30 minutes from now: {later}")

# Multiple units
complex_delta = now + timedelta(days=10, hours=3, minutes=45, seconds=30)
print(f"Complex delta: {complex_delta}")

print("\n=== EXAMPLE 5: Calculating Time Differences ===\n")

# Calculate difference between two dates
date1 = datetime(2025, 1, 1)
date2 = datetime(2025, 12, 31)
difference = date2 - date1

print(f"Date 1: {date1.strftime('%B %d, %Y')}")
print(f"Date 2: {date2.strftime('%B %d, %Y')}")
print(f"Days between: {difference.days} days")
print(f"Total seconds: {difference.total_seconds()} seconds")

# How many days until a future event
birthday = datetime(2026, 6, 15)
days_until = (birthday - now).days
print(f"\nDays until June 15, 2026: {days_until} days")

print("\n=== EXAMPLE 6: Creating Specific Dates ===\n")

# Create specific date and time objects
specific_date = date(2025, 12, 25)
print(f"Christmas 2025: {specific_date}")

specific_time = time(14, 30, 0)  # 2:30 PM
print(f"Specific time: {specific_time}")

specific_datetime = datetime(2025, 7, 4, 18, 30)
print(f"July 4th, 2025 at 6:30 PM: {specific_datetime}")

print("\n=== EXAMPLE 7: Weekdays and Calendar Info ===\n")

# Get day of week (0=Monday, 6=Sunday)
weekday_num = now.weekday()
weekday_name = now.strftime("%A")
print(f"Today is {weekday_name} (day {weekday_num})")

# Check if it's a weekend
if weekday_num >= 5:
    print("It's the weekend!")
else:
    print("It's a weekday.")

print("\n=== EXAMPLE 8: Practical Example - Age Calculator ===\n")

def calculate_age(birth_date):
    """Calculate age from birth date."""
    today = date.today()
    age = today.year - birth_date.year
    # Adjust if birthday hasn't occurred this year
    if (today.month, today.day) < (birth_date.month, birth_date.day):
        age -= 1
    return age

birth = date(2000, 5, 15)
age = calculate_age(birth)
print(f"Birth date: {birth.strftime('%B %d, %Y')}")
print(f"Age: {age} years old")
