"""
Lesson 13: Classes and Objects
Classes are blueprints for creating objects.
Objects bundle data (attributes) and functionality (methods) together.
"""

print("=== EXAMPLE 1: Basic Class Definition ===\n")

# Define a class
class Person:
    def __init__(self, name, age):
        """Constructor method - called when creating a new object."""
        self.name = name  # Instance attribute
        self.age = age    # Instance attribute
    
    def greet(self):
        """Instance method - can access instance attributes."""
        print(f"Hello, my name is {self.name} and I am {self.age} years old.")

# Create an object (instance) of the class
person1 = Person("Alice", 30)

# Access attributes
print(f"Name: {person1.name}")
print(f"Age: {person1.age}")

# Call a method
person1.greet()

print("\n=== EXAMPLE 2: Multiple Objects ===\n")

# Create multiple objects from the same class
person2 = Person("Bob", 25)
person3 = Person("Carol", 28)

# Each object has its own data
person2.greet()
person3.greet()

print("\n=== EXAMPLE 3: Class with More Methods ===\n")

class BankAccount:
    def __init__(self, owner, balance=0):
        """Create a bank account with optional starting balance."""
        self.owner = owner
        self.balance = balance
    
    def deposit(self, amount):
        """Add money to the account."""
        self.balance += amount
        print(f"Deposited ${amount}. New balance: ${self.balance}")
    
    def withdraw(self, amount):
        """Remove money from the account."""
        if amount > self.balance:
            print(f"Insufficient funds! Balance: ${self.balance}")
        else:
            self.balance -= amount
            print(f"Withdrew ${amount}. New balance: ${self.balance}")
    
    def get_balance(self):
        """Return the current balance."""
        return self.balance

# Create a bank account
account = BankAccount("Alice", 1000)
print(f"{account.owner}'s account created with ${account.balance}")

# Use the methods
account.deposit(500)
account.withdraw(200)
account.withdraw(2000)  # This will fail
print(f"Final balance: ${account.get_balance()}")

print("\n=== EXAMPLE 4: Class Attributes ===\n")

class Dog:
    # Class attribute (shared by all instances)
    species = "Canis familiaris"
    
    def __init__(self, name, breed):
        # Instance attributes (unique to each instance)
        self.name = name
        self.breed = breed
    
    def description(self):
        return f"{self.name} is a {self.breed}"
    
    def speak(self, sound):
        return f"{self.name} says {sound}"

# Create dog objects
dog1 = Dog("Buddy", "Golden Retriever")
dog2 = Dog("Lucy", "Beagle")

# Class attribute is the same for all instances
print(f"Dog 1 species: {dog1.species}")
print(f"Dog 2 species: {dog2.species}")

# Instance attributes are unique
print(dog1.description())
print(dog2.description())

# Methods can use instance data
print(dog1.speak("Woof!"))
print(dog2.speak("Arf!"))

print("\n=== EXAMPLE 5: String Representation ===\n")

class Book:
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages
    
    def __str__(self):
        """String representation for print()."""
        return f"'{self.title}' by {self.author}"
    
    def __repr__(self):
        """Detailed representation for debugging."""
        return f"Book(title='{self.title}', author='{self.author}', pages={self.pages})"

book = Book("Python Crash Course", "Eric Matthes", 544)

# __str__ is used by print()
print(f"Book: {book}")

# __repr__ shows more detail
print(f"Detailed: {repr(book)}")

print("\n=== EXAMPLE 6: Object Comparison ===\n")

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __eq__(self, other):
        """Define equality for Point objects."""
        return self.x == other.x and self.y == other.y
    
    def __str__(self):
        return f"Point({self.x}, {self.y})"

p1 = Point(3, 4)
p2 = Point(3, 4)
p3 = Point(5, 6)

print(f"p1: {p1}")
print(f"p2: {p2}")
print(f"p3: {p3}")
print(f"p1 == p2: {p1 == p2}")  # True because coordinates match
print(f"p1 == p3: {p1 == p3}")  # False because coordinates differ
