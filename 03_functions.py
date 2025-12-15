"""
===========================================
PYTHON TUTORIAL: Functions
===========================================
This file covers functions, parameters, return values, scope, and lambda functions.
Run this file with: python3 03_functions.py
"""

print("=" * 60)
print("PART 1: DEFINING AND CALLING FUNCTIONS")
print("=" * 60)


# Functions are reusable blocks of code
# Syntax: def function_name():
def greet():
    """Simple function that prints a greeting"""
    print("Hello, World!")


print("\nCalling the greet() function:")
greet()

# Function naming: use snake_case, descriptive names
# ✅ Good: calculate_total(), get_user_name()
# ❌ Bad: 2calculate(), calculate total(), def()


print("\n" + "=" * 60)
print("PART 2: PARAMETERS AND ARGUMENTS")
print("=" * 60)


# Parameters allow functions to receive data
def greet_person(name):
    """Function with one parameter"""
    print(f"Hello, {name}!")


print("\nFunctions with parameters:")
greet_person("Alice")
greet_person("Bob")


# Multiple parameters
def introduce(name, age):
    print(f"My name is {name} and I'm {age} years old.")


introduce("Alice", 25)


# Default parameters
def greet_with_time(name, time="morning"):
    print(f"Good {time}, {name}!")


greet_with_time("Alice")  # Uses default
greet_with_time("Bob", "evening")  # Overrides default


# Keyword arguments (order doesn't matter)
def create_profile(name, age, city):
    print(f"{name}, {age}, from {city}")


create_profile(age=30, name="Bob", city="Toronto")


print("\n" + "=" * 60)
print("PART 3: RETURN VALUES")
print("=" * 60)


# Functions can return values using 'return'
def add_numbers(a, b):
    return a + b


print(f"\n5 + 3 = {add_numbers(5, 3)}")
result = add_numbers(10, 20)
print(f"10 + 20 = {result}")


# Multiple return values (returns a tuple)
def calculate(x, y):
    return x + y, x - y, x * y, x / y


add, subtract, multiply, divide = calculate(10, 5)
print(f"10 + 5 = {add}, 10 - 5 = {subtract}")


# Functions without return return None
def print_message(msg):
    print(msg)


print(f"Return value: {print_message('Hello')}")


print("\n" + "=" * 60)
print("PART 4: FUNCTION SCOPE - LOCAL AND GLOBAL VARIABLES")
print("=" * 60)

# Global variables: defined outside functions, accessible anywhere
global_var = "I am global"


def show_global():
    print(f"Inside function: {global_var}")


print(f"\nOutside function: {global_var}")
show_global()


# Local variables: defined inside functions, only exist within that function
def create_local():
    local_var = "I am local"
    print(f"Inside function: {local_var}")


create_local()
# print(local_var)  # Error: local_var doesn't exist outside!

# Variable shadowing: local variable hides global one with same name
x = "global x"


def show_shadowing():
    x = "local x"  # New local variable
    print(f"Inside function: {x}")


print(f"\nOutside: {x}")
show_shadowing()
print(f"Outside (still): {x}")  # Global unchanged

# Modifying global variables: use 'global' keyword
counter = 0


def increment_counter():
    global counter
    counter += 1
    print(f"Counter: {counter}")


print(f"\nBefore: {counter}")
increment_counter()
increment_counter()
print(f"After: {counter}")


# Best practice: pass values as parameters and return results
def increment_value(value):
    return value + 1


my_number = increment_value(5)
print(f"My number: {my_number}")


print("\n" + "=" * 60)
print("PART 5: LAMBDA FUNCTIONS")
print("=" * 60)


# Lambda functions: small, anonymous functions
# Syntax: lambda parameters: expression
def add_regular(x, y):
    return x + y


add_lambda = lambda x, y: x + y

print(f"\nRegular: {add_regular(5, 3)}")
print(f"Lambda: {add_lambda(5, 3)}")

# Common use: with map(), filter(), sorted()
numbers = [1, 2, 3, 4, 5]
squared = list(map(lambda x: x**2, numbers))
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print(f"Squared: {squared}")
print(f"Even: {even_numbers}")

# Lambda with sorted()
students = [{"name": "Alice", "age": 25}, {"name": "Bob", "age": 20}]
sorted_students = sorted(students, key=lambda s: s["age"])
print(f"Sorted by age: {[s['name'] for s in sorted_students]}")


print("\n" + "=" * 60)
print("PART 6: PRACTICAL EXAMPLES")
print("=" * 60)


def celsius_to_fahrenheit(celsius):
    return (celsius * 9 / 5) + 32


def calculate_grade(score):
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    else:
        return "F"


print(f"\n25°C = {celsius_to_fahrenheit(25)}°F")
print(f"Score 85 = Grade {calculate_grade(85)}")

# Lambda example
temps = [0, 20, 30, 40]
fahrenheit = list(map(lambda c: (c * 9 / 5) + 32, temps))
print(f"Temps in °F: {fahrenheit}")


print("\n" + "=" * 60)
print("END OF TUTORIAL")
print("=" * 60)
print("\nKey Takeaways:")
print("- Functions make code reusable")
print("- Parameters receive data, return sends data back")
print("- Local variables exist only in functions")
print("- Global variables accessible everywhere (use carefully!)")
print("- Lambda: short anonymous functions")
print("\nPractice creating your own functions!")
