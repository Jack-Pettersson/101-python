"""
Lesson 14: Inheritance
Inheritance allows classes to inherit attributes and methods from other classes.
This promotes code reuse and creates hierarchical relationships.
"""

print("=== EXAMPLE 1: Basic Inheritance ===\n")

# Parent class (also called base class or superclass)
class Animal:
    def __init__(self, name):
        self.name = name
    
    def speak(self):
        print(f"{self.name} makes a sound.")

# Child class (also called derived class or subclass)
class Dog(Animal):
    def speak(self):
        """Override the parent's speak method."""
        print(f"{self.name} barks.")

class Cat(Animal):
    def speak(self):
        """Override the parent's speak method."""
        print(f"{self.name} meows.")

# Create objects
animal = Animal("Generic Animal")
dog = Dog("Rex")
cat = Cat("Whiskers")

# Call methods
animal.speak()  # Uses Animal's method
dog.speak()     # Uses Dog's method (overridden)
cat.speak()     # Uses Cat's method (overridden)

print("\n=== EXAMPLE 2: Using super() ===\n")

class Bird(Animal):
    def speak(self):
        """Call parent method first, then add own behavior."""
        super().speak()  # Call parent class's speak()
        print(f"{self.name} also chirps.")

bird = Bird("Tweety")
bird.speak()

print("\n=== EXAMPLE 3: Extending __init__() ===\n")

class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
    
    def display_info(self):
        print(f"Employee: {self.name}, Salary: ${self.salary}")

class Manager(Employee):
    def __init__(self, name, salary, department):
        """Initialize parent attributes plus new ones."""
        super().__init__(name, salary)  # Call parent constructor
        self.department = department    # Add new attribute
    
    def display_info(self):
        """Override to show additional information."""
        super().display_info()  # Call parent method
        print(f"Department: {self.department}")

emp = Employee("John", 50000)
emp.display_info()

print()

mgr = Manager("Sarah", 80000, "Engineering")
mgr.display_info()

print("\n=== EXAMPLE 4: Multiple Levels of Inheritance ===\n")

class Vehicle:
    def __init__(self, brand):
        self.brand = brand
    
    def start(self):
        print(f"{self.brand} vehicle is starting...")

class Car(Vehicle):
    def __init__(self, brand, model):
        super().__init__(brand)
        self.model = model
    
    def honk(self):
        print(f"{self.brand} {self.model} goes beep beep!")

class ElectricCar(Car):
    def __init__(self, brand, model, battery_size):
        super().__init__(brand, model)
        self.battery_size = battery_size
    
    def charge(self):
        print(f"Charging {self.brand} {self.model} with {self.battery_size} kWh battery...")

# Create an electric car (inherits from Car, which inherits from Vehicle)
tesla = ElectricCar("Tesla", "Model 3", 75)
tesla.start()   # From Vehicle
tesla.honk()    # From Car
tesla.charge()  # From ElectricCar

print("\n=== EXAMPLE 5: Adding New Methods ===\n")

class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height
    
    def area(self):
        return self.width * self.height

class Square(Rectangle):
    def __init__(self, side):
        """A square is a rectangle with equal sides."""
        super().__init__(side, side)
        self.side = side
    
    def perimeter(self):
        """New method not in parent class."""
        return 4 * self.side

rect = Rectangle(5, 3)
print(f"Rectangle area: {rect.area()}")

square = Square(4)
print(f"Square area: {square.area()}")  # Inherited method
print(f"Square perimeter: {square.perimeter()}")  # New method

print("\n=== EXAMPLE 6: isinstance() and issubclass() ===\n")

# Check if object is instance of a class
print(f"Is dog an Animal? {isinstance(dog, Animal)}")
print(f"Is dog a Dog? {isinstance(dog, Dog)}")
print(f"Is dog a Cat? {isinstance(dog, Cat)}")

# Check if class is a subclass of another
print(f"Is Dog a subclass of Animal? {issubclass(Dog, Animal)}")
print(f"Is Cat a subclass of Animal? {issubclass(Cat, Animal)}")
print(f"Is Animal a subclass of Dog? {issubclass(Animal, Dog)}")
