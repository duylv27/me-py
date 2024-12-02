# Function with positional and keyword arguments
def greet(name, age=18):
    print(f"Hello {name}, you are {age} years old.")

# Positional arguments
greet("Alice", 25)  # Output: Hello Alice, you are 25 years old.

# Keyword arguments
greet(age=30, name="Bob")  # Output: Hello Bob, you are 30 years old.

# Default argument
greet("Charlie")  # Output: Hello Charlie, you are 18 years old.
