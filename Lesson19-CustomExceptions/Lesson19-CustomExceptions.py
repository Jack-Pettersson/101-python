"""
Lesson 19: Custom Exceptions
Custom exceptions make your code more readable and maintainable.
They allow you to create specific error types for your application.
"""

print("=== EXAMPLE 1: Basic Custom Exception ===\n")

# Define a custom exception class
class NegativeNumberError(Exception):
    """Raised when a negative number is provided where not allowed."""
    pass

def check_positive(number):
    """Check if number is positive, raise exception if negative."""
    if number < 0:
        raise NegativeNumberError(f"Number must be non-negative! Got: {number}")
    print(f"{number} is non-negative.")

# Test the function
try:
    check_positive(5)
    check_positive(-3)  # This will raise an exception
except NegativeNumberError as e:
    print(f"Custom exception caught: {e}")

print("\n=== EXAMPLE 2: Exception with Additional Data ===\n")

class InsufficientFundsError(Exception):
    """Raised when attempting to withdraw more money than available."""
    
    def __init__(self, balance, amount):
        self.balance = balance
        self.amount = amount
        self.message = f"Cannot withdraw ${amount}. Current balance: ${balance}"
        super().__init__(self.message)

class BankAccount:
    def __init__(self, balance=0):
        self.balance = balance
    
    def withdraw(self, amount):
        if amount > self.balance:
            raise InsufficientFundsError(self.balance, amount)
        self.balance -= amount
        print(f"Withdrew ${amount}. New balance: ${self.balance}")

# Test the bank account
account = BankAccount(100)
try:
    account.withdraw(50)
    print(f"Current balance: ${account.balance}")
    account.withdraw(75)  # This will fail
except InsufficientFundsError as e:
    print(f"Transaction failed: {e.message}")
    print(f"  Attempted: ${e.amount}")
    print(f"  Available: ${e.balance}")

print("\n=== EXAMPLE 3: Multiple Custom Exceptions ===\n")

class ValidationError(Exception):
    """Base class for validation errors."""
    pass

class InvalidEmailError(ValidationError):
    """Raised when email format is invalid."""
    pass

class InvalidAgeError(ValidationError):
    """Raised when age is invalid."""
    pass

class InvalidUsernameError(ValidationError):
    """Raised when username is invalid."""
    pass

def validate_email(email):
    """Validate email contains @ and ."""
    if "@" not in email or "." not in email:
        raise InvalidEmailError(f"Invalid email format: {email}")
    print(f"✓ Email is valid: {email}")

def validate_age(age):
    """Validate age is between 0 and 120."""
    if not 0 <= age <= 120:
        raise InvalidAgeError(f"Age must be between 0 and 120, got {age}")
    print(f"✓ Age is valid: {age}")

def validate_username(username):
    """Validate username is at least 3 characters."""
    if len(username) < 3:
        raise InvalidUsernameError(f"Username must be at least 3 characters, got '{username}'")
    print(f"✓ Username is valid: {username}")

# Test validations
print("Testing valid inputs:")
try:
    validate_email("alice@example.com")
    validate_age(25)
    validate_username("alice123")
    print("All validations passed!\n")
except ValidationError as e:
    print(f"Validation error: {e}\n")

print("Testing invalid inputs:")
validations = [
    (lambda: validate_email("invalid-email"), "email"),
    (lambda: validate_age(150), "age"),
    (lambda: validate_username("ab"), "username")
]

for validator, field in validations:
    try:
        validator()
    except ValidationError as e:
        print(f"✗ {field.capitalize()} validation failed: {e}")

print("\n=== EXAMPLE 4: Exception Hierarchy ===\n")

class GameError(Exception):
    """Base class for game-related errors."""
    pass

class InvalidMoveError(GameError):
    """Raised when a move is not allowed."""
    pass

class GameOverError(GameError):
    """Raised when trying to play after game is over."""
    pass

class TicTacToe:
    def __init__(self):
        self.board = [[" " for _ in range(3)] for _ in range(3)]
        self.game_over = False
        self.current_player = "X"
    
    def make_move(self, row, col):
        if self.game_over:
            raise GameOverError("The game has already ended!")
        
        if not (0 <= row < 3 and 0 <= col < 3):
            raise InvalidMoveError(f"Position ({row}, {col}) is out of bounds!")
        
        if self.board[row][col] != " ":
            raise InvalidMoveError(f"Position ({row}, {col}) is already occupied!")
        
        self.board[row][col] = self.current_player
        print(f"Player {self.current_player} placed at ({row}, {col})")
        self.current_player = "O" if self.current_player == "X" else "X"

# Test the game
game = TicTacToe()

try:
    game.make_move(0, 0)  # Valid
    game.make_move(0, 1)  # Valid
    game.make_move(0, 0)  # Invalid - already occupied
except InvalidMoveError as e:
    print(f"Invalid move: {e}")
except GameError as e:
    print(f"Game error: {e}")

print("\n=== EXAMPLE 5: Re-raising Exceptions ===\n")

class DatabaseError(Exception):
    """Raised for database-related errors."""
    pass

def save_to_database(data):
    """Simulate saving data to database."""
    if not data:
        raise DatabaseError("Cannot save empty data!")
    print(f"Data saved: {data}")

def process_and_save(data):
    """Process data and save it, with error handling."""
    try:
        print(f"Processing: {data}")
        save_to_database(data)
    except DatabaseError as e:
        print(f"Database error occurred: {e}")
        # Log the error and re-raise with more context
        raise DatabaseError(f"Failed to process '{data}': {e}") from e

# Test re-raising
try:
    process_and_save("valid data")
    print()
    process_and_save("")  # This will cause an error
except DatabaseError as e:
    print(f"Final error handler: {e}")
    if e.__cause__:
        print(f"Original cause: {e.__cause__}")

print("\n=== EXAMPLE 6: Exception with Cleanup ===\n")

class FileProcessingError(Exception):
    """Raised when file processing fails."""
    pass

def process_file(filename):
    """Simulate file processing with proper cleanup."""
    print(f"Opening file: {filename}")
    file_handle = f"<File: {filename}>"
    
    try:
        if "invalid" in filename:
            raise FileProcessingError(f"Cannot process file: {filename}")
        print(f"Processing {filename}...")
        print(f"File processed successfully!")
    except FileProcessingError:
        print(f"Error occurred while processing {filename}")
        raise  # Re-raise the exception
    finally:
        print(f"Closing file: {file_handle}")
        print()

# Test with valid and invalid files
try:
    process_file("data.txt")
    process_file("invalid_file.txt")
except FileProcessingError as e:
    print(f"Caught exception: {e}")

print("\n=== EXAMPLE 7: Interactive Exception Demo ===\n")

class TemperatureError(Exception):
    """Base class for temperature-related errors."""
    pass

class TemperatureTooHighError(TemperatureError):
    """Raised when temperature exceeds safe limit."""
    def __init__(self, temp, limit):
        self.temp = temp
        self.limit = limit
        super().__init__(f"Temperature {temp}°C exceeds safe limit of {limit}°C")

class TemperatureTooLowError(TemperatureError):
    """Raised when temperature is below safe limit."""
    def __init__(self, temp, limit):
        self.temp = temp
        self.limit = limit
        super().__init__(f"Temperature {temp}°C is below safe limit of {limit}°C")

def check_temperature(temp, min_temp=0, max_temp=100):
    """Check if temperature is within safe range."""
    if temp > max_temp:
        raise TemperatureTooHighError(temp, max_temp)
    elif temp < min_temp:
        raise TemperatureTooLowError(temp, min_temp)
    else:
        print(f"✓ Temperature {temp}°C is within safe range ({min_temp}°C - {max_temp}°C)")

# Test different temperatures
temperatures = [25, 105, -10, 50]

for temp in temperatures:
    try:
        check_temperature(temp)
    except TemperatureTooHighError as e:
        print(f"⚠ WARNING: {e}")
    except TemperatureTooLowError as e:
        print(f"⚠ WARNING: {e}")
    except TemperatureError as e:
        print(f"Temperature error: {e}")

print("\n✅ All custom exception examples completed!")
