"""
===========================================
PYTHON TUTORIAL: Variables, Data Types & Operators
===========================================
This file covers the fundamentals of Python programming.
Run this file with: python3 01_variables_data_types_operators.py
"""

print("=" * 60)
print("PART 1: VARIABLES")
print("=" * 60)

# ==========================================
# WHAT IS A VARIABLE?
# ==========================================
# A variable is like a labeled box that stores information.
# You give it a name and put a value inside it.
# Think of it like a container with a label on it.

# Creating a variable (also called "assigning" a value)
# Syntax: variable_name = value

# Example: Store the number 10 in a variable called 'age'
age = 10
print(f"Age variable contains: {age}")

# You can change the value of a variable anytime
age = 25  # Now age is 25 instead of 10
print(f"Age variable now contains: {age}")

# ==========================================
# VARIABLE NAMING RULES
# ==========================================
# 1. Must start with a letter (a-z, A-Z) or underscore (_)
# 2. Can contain letters, numbers, and underscores
# 3. Cannot use spaces or special characters (except _)
# 4. Case-sensitive (age, Age, and AGE are different)
# 5. Cannot use Python keywords (like 'print', 'if', 'for', etc.)

# ✅ GOOD variable names:
my_name = "Kamram"
user_age = 29
total_count = 100
_is_active = True
student1 = "Alice"

# ❌ BAD variable names (uncomment to see errors):
# 2name = "John"        # Can't start with number
# my name = "John"      # Can't have spaces
# my-name = "John"      # Can't use hyphens
# if = 10               # Can't use Python keywords

# ==========================================
# NAMING CONVENTIONS (Best Practices)
# ==========================================
# Python uses snake_case (lowercase with underscores)
# This makes code more readable

# Good examples:
first_name = "Kamram"
last_name = "Latif"
phone_number = "123-456-7890"
is_student = True

print(f"\nName: {first_name} {last_name}")
print(f"Phone: {phone_number}")
print(f"Is Student: {is_student}")

print("\n" + "=" * 60)
print("PART 2: DATA TYPES")
print("=" * 60)

# ==========================================
# DATA TYPE 1: INTEGER (int)
# ==========================================
# Integers are whole numbers (positive, negative, or zero)
# No decimal points

number_of_students = 50
temperature = -10
zero = 0
big_number = 1000000

print(f"\nInteger examples:")
print(f"Number of students: {number_of_students} (type: {type(number_of_students)})")
print(f"Temperature: {temperature} (type: {type(temperature)})")

# ==========================================
# DATA TYPE 2: FLOAT (float)
# ==========================================
# Floats are decimal numbers (numbers with decimal points)

price = 19.99
pi = 3.14159
percentage = 85.5
negative_float = -3.14

print(f"\nFloat examples:")
print(f"Price: ${price} (type: {type(price)})")
print(f"Pi: {pi} (type: {type(pi)})")

# ==========================================
# DATA TYPE 3: STRING (str)
# ==========================================
# Strings are text - anything inside quotes (single or double)

name = "Kamram"
greeting = "Hello"
sentence = "Python is awesome!"
empty_string = ""

# You can use single or double quotes
message1 = "She said 'Hello'"
message2 = 'He said "Hi there"'

print(f"\nString examples:")
print(f"Name: {name} (type: {type(name)})")
print(f"Greeting: {greeting}")
print(f"Message: {message1}")

# String concatenation (joining strings)
full_greeting = greeting + " " + name
print(f"Full greeting: {full_greeting}")

# ==========================================
# DATA TYPE 4: LIST (list)
# ==========================================
# Lists are ordered collections of items
# Items are enclosed in square brackets []
# Items can be of different types
# Lists are MUTABLE (can be changed)

# Creating a list
fruits = ["apple", "banana", "orange"]
numbers = [1, 2, 3, 4, 5]
mixed_list = [1, "hello", 3.14, True]  # Can mix types
empty_list = []

print(f"\nList examples:")
print(f"Fruits: {fruits} (type: {type(fruits)})")
print(f"Numbers: {numbers}")
print(f"Mixed list: {mixed_list}")

# Accessing list items (indexing starts at 0)
print(f"First fruit: {fruits[0]}")  # apple
print(f"Second fruit: {fruits[1]}")  # banana

# Modifying lists (they are mutable)
fruits.append("grape")  # Add item to end
print(f"After adding grape: {fruits}")

fruits[0] = "mango"  # Change first item
print(f"After changing first item: {fruits}")

# ==========================================
# DATA TYPE 5: TUPLE (tuple)
# ==========================================
# Tuples are ordered collections like lists
# Items are enclosed in parentheses ()
# Tuples are IMMUTABLE (cannot be changed)

# Creating a tuple
coordinates = (10, 20)
colors = ("red", "green", "blue")
single_item_tuple = (42,)  # Note the comma!

print(f"\nTuple examples:")
print(f"Coordinates: {coordinates} (type: {type(coordinates)})")
print(f"Colors: {colors}")

# Accessing tuple items (same as lists)
print(f"X coordinate: {coordinates[0]}")
print(f"Y coordinate: {coordinates[1]}")

# Tuples cannot be modified (uncomment to see error):
# coordinates[0] = 15  # This will cause an error!

# ==========================================
# DATA TYPE 6: DICTIONARY (dict)
# ==========================================
# Dictionaries store key-value pairs
# Like a real dictionary: word (key) -> definition (value)
# Items are enclosed in curly braces {}
# Format: {key: value, key: value}

# Creating a dictionary
student = {"name": "Kamram", "age": 25, "grade": "A", "city": "New York"}

# Another example
phonebook = {"Alice": "555-1234", "Bob": "555-5678", "Charlie": "555-9012"}

print(f"\nDictionary examples:")
print(f"Student info: {student} (type: {type(student)})")  # type: dict
print(f"Phonebook: {phonebook}")

# Accessing dictionary values using keys
print(f"Student name: {student['name']}")
print(f"Student age: {student['age']}")
print(f"Alice's phone: {phonebook['Alice']}")

# Modifying dictionaries
student["age"] = 26  # Update existing key
student["email"] = "kamram@example.com"  # Add new key-value pair
print(f"Updated student: {student}")

# ==========================================
# CHECKING DATA TYPES
# ==========================================
# Use type() function to check what type something is

print(f"\n" + "=" * 60)
print("Checking Data Types:")
print("=" * 60)

example_int = 42
example_float = 3.14
example_string = "Hello"
example_list = [1, 2, 3]
example_tuple = (1, 2, 3)
example_dict = {"key": "value"}

print(f"42 is: {type(example_int)}")
print(f"3.14 is: {type(example_float)}")
print(f"'Hello' is: {type(example_string)}")
print(f"[1,2,3] is: {type(example_list)}")
print(f"(1,2,3) is: {type(example_tuple)}")
print(f"{{'key':'value'}} is: {type(example_dict)}")

print("\n" + "=" * 60)
print("PART 3: OPERATORS")
print("=" * 60)

# ==========================================
# ARITHMETIC OPERATORS
# ==========================================
# Used for mathematical operations

a = 10
b = 3

print(f"\nArithmetic Operators (a = {a}, b = {b}):")
print(f"Addition (a + b): {a} + {b} = {a + b}")
print(f"Subtraction (a - b): {a} - {b} = {a - b}")
print(f"Multiplication (a * b): {a} * {b} = {a * b}")
print(f"Division (a / b): {a} / {b} = {a / b}")
print(f"Floor Division (a // b): {a} // {b} = {a // b}")  # Rounds down to whole number
print(f"Modulus (a % b): {a} % {b} = {a % b}")  # Remainder after division
print(f"Exponentiation (a ** b): {a} ** {b} = {a ** b}")  # Power (a to the power of b)

# ==========================================
# COMPARISON OPERATORS
# ==========================================
# Used to compare values
# Returns True or False (Boolean values)

x = 10
y = 5
z = 10

print(f"\nComparison Operators (x = {x}, y = {y}, z = {z}):")
print(f"Equal (x == y): {x} == {y} = {x == y}")
print(f"Not Equal (x != y): {x} != {y} = {x != y}")
print(f"Greater Than (x > y): {x} > {y} = {x > y}")
print(f"Less Than (x < y): {x} < {y} = {x < y}")
print(f"Greater or Equal (x >= z): {x} >= {z} = {x >= z}")
print(f"Less or Equal (x <= y): {x} <= {y} = {x <= y}")

# ==========================================
# LOGICAL OPERATORS
# ==========================================
# Used to combine or modify Boolean values
# and, or, not

p = True
q = False

print(f"\nLogical Operators (p = {p}, q = {q}):")
print(f"AND (p and q): {p} and {q} = {p and q}")  # Both must be True
print(f"OR (p or q): {p} or {q} = {p or q}")  # At least one must be True
print(f"NOT (not p): not {p} = {not p}")  # Reverses the value

# Real-world example
age = 25
has_license = True

can_drive = age >= 18 and has_license
print(f"\nCan drive? (age >= 18 and has_license): {can_drive}")

# ==========================================
# ASSIGNMENT OPERATORS
# ==========================================
# Used to assign values to variables
# Can combine arithmetic with assignment

num = 10
print(f"\nAssignment Operators (starting with num = {num}):")

# Basic assignment
num = 10
print(f"num = 10: {num}")

# Add and assign
num += 5  # Same as: num = num + 5
print(f"num += 5: {num}")

# Subtract and assign
num -= 3  # Same as: num = num - 3
print(f"num -= 3: {num}")

# Multiply and assign
num *= 2  # Same as: num = num * 2
print(f"num *= 2: {num}")

# Divide and assign
num /= 4  # Same as: num = num / 4
print(f"num /= 4: {num}")

# Modulus and assign
num %= 3  # Same as: num = num % 3
print(f"num %= 3: {num}")

# Power and assign
num = 5
num **= 2  # Same as: num = num ** 2
print(f"num **= 2: {num}")

# Floor divide and assign
num = 10
num //= 3  # Same as: num = num // 3
print(f"num //= 3: {num}")

# ==========================================
# PRACTICE EXAMPLES
# ==========================================

print("\n" + "=" * 60)
print("PRACTICE EXAMPLES")
print("=" * 60)

# Example 1: Calculate total price
item_price = 29.99
quantity = 3
tax_rate = 0.08  # 8% tax

subtotal = item_price * quantity
tax = subtotal * tax_rate
total = subtotal + tax

print(f"\nExample 1: Shopping Cart")
print(f"Item Price: ${item_price}")
print(f"Quantity: {quantity}")
print(f"Subtotal: ${subtotal:.2f}")
print(f"Tax (8%): ${tax:.2f}")
print(f"Total: ${total:.2f}")

# Example 2: Student information
student_info = {"name": "Alice", "grades": [85, 90, 78, 92], "age": 20}

average_grade = sum(student_info["grades"]) / len(student_info["grades"])
is_passing = average_grade >= 70

print(f"\nExample 2: Student Report")
print(f"Name: {student_info['name']}")
print(f"Age: {student_info['age']}")
print(f"Grades: {student_info['grades']}")
print(f"Average: {average_grade:.1f}")
print(f"Passing: {is_passing}")

# Example 3: String operations
first_name = "Kamram"
last_name = "Latif"
full_name = first_name + " " + last_name
name_length = len(full_name)

print(f"\nExample 3: String Operations")
print(f"First Name: {first_name}")
print(f"Last Name: {last_name}")
print(f"Full Name: {full_name}")
print(f"Name Length: {name_length} characters")

print("\n" + "=" * 60)
print("END OF TUTORIAL")
print("=" * 60)
print("\nTry modifying the values and running the code again!")
print("Experiment with different operators and data types.")
