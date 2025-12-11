"""
===========================================
PYTHON TUTORIAL: Control Flow and Loops
===========================================
This file covers conditional statements, loops, list comprehensions, and generators.
Run this file with: python3 02_control_flow_loops.py
"""

print("=" * 60)
print("PART 1: CONDITIONAL STATEMENTS (if, else, elif)")
print("=" * 60)

# ==========================================
# IF STATEMENT
# ==========================================
# Used to make decisions in your code
# Syntax: if condition:
#            code to execute

age = 20
if age >= 18:
    print(f"Age {age}: You are an adult!")

# ==========================================
# IF-ELSE STATEMENT
# ==========================================
# Executes one block if condition is True, another if False

temperature = 25
if temperature > 30:
    print("It's hot outside!")
else:
    print("It's not too hot.")

# ==========================================
# IF-ELIF-ELSE STATEMENT
# ==========================================
# Used when you have multiple conditions to check
# elif = "else if" - checks another condition if previous ones are False

score = 85

if score >= 90:
    grade = "A"
    print(f"Score {score}: Grade {grade} - Excellent!")
elif score >= 80:
    grade = "B"
    print(f"Score {score}: Grade {grade} - Good!")
elif score >= 70:
    grade = "C"
    print(f"Score {score}: Grade {grade} - Average")
elif score >= 60:
    grade = "D"
    print(f"Score {score}: Grade {grade} - Below Average")
else:
    grade = "F"
    print(f"Score {score}: Grade {grade} - Failed")

# ==========================================
# NESTED IF STATEMENTS
# ==========================================
# You can put if statements inside other if statements

age = 20
has_license = True

if age >= 18:
    print("You are old enough to drive.")
    if has_license:
        print("You have a license. You can drive!")
    else:
        print("But you need a license first.")
else:
    print("You are too young to drive.")

# ==========================================
# MULTIPLE CONDITIONS
# ==========================================
# Using 'and', 'or', 'not' with if statements

username = "admin"
password = "12345"

if username == "admin" and password == "12345":
    print("Login successful!")
else:
    print("Invalid credentials.")

# Example with 'or'
day = "Saturday"
if day == "Saturday" or day == "Sunday":
    print("It's the weekend!")
else:
    print("It's a weekday.")

print("\n" + "=" * 60)
print("PART 2: LOOPS")
print("=" * 60)

# ==========================================
# WHILE LOOP
# ==========================================
# Repeats code as long as condition is True
# Be careful: make sure condition becomes False, or loop runs forever!

print("\nWhile Loop Example 1: Counting")
count = 1
while count <= 5:
    print(f"Count: {count}")
    count += 1  # Important: increment count, otherwise infinite loop!

print("\nWhile Loop Example 2: User Input Simulation")
# Simulating user input (normally you'd use input() function)
attempts = 0
max_attempts = 3
correct_password = "python123"

while attempts < max_attempts:
    attempts += 1
    entered_password = "wrong"  # Simulating wrong password
    if entered_password == correct_password:
        print("Access granted!")
        break  # Exit loop immediately
    else:
        print(f"Wrong password. Attempt {attempts}/{max_attempts}")
else:
    print("Too many failed attempts. Access denied.")

# ==========================================
# FOR LOOP
# ==========================================
# Used to iterate over a sequence (list, string, tuple, etc.)

print("\nFor Loop Example 1: Iterating over a list")
fruits = ["apple", "banana", "orange"]
for fruit in fruits:
    print(f"I like {fruit}")

print("\nFor Loop Example 2: Iterating over a string")
word = "Python"
for letter in word:
    print(letter, end=" ")  # end=" " prints on same line with space
print()  # New line

print("\nFor Loop Example 3: Iterating over a dictionary")
student = {"name": "Alice", "age": 20, "grade": "A"}
for key in student:
    print(f"{key}: {student[key]}")

# Iterating over both keys and values
for key, value in student.items():
    print(f"{key} = {value}")

# ==========================================
# RANGE FUNCTION
# ==========================================
# range() generates a sequence of numbers
# Very useful with for loops!

print("\nRange Function Examples:")
print("range(5) generates: 0, 1, 2, 3, 4")
for i in range(5):
    print(f"Number: {i}")

print("\nrange(2, 6) generates: 2, 3, 4, 5")
for i in range(2, 6):
    print(f"Number: {i}")

print("\nrange(0, 10, 2) generates: 0, 2, 4, 6, 8 (step by 2)")
for i in range(0, 10, 2):
    print(f"Number: {i}")

# Converting range to list
numbers = list(range(1, 6))
print(f"\nrange(1, 6) as list: {numbers}")

# ==========================================
# LOOP CONTROL STATEMENTS
# ==========================================
# break: Exit the loop immediately
# continue: Skip to next iteration
# pass: Do nothing (placeholder)

print("\nBreak Example: Stop when finding 'banana'")
fruits = ["apple", "banana", "orange", "grape"]
for fruit in fruits:
    if fruit == "banana":
        print("Found banana! Stopping search.")
        break
    print(f"Checking {fruit}...")

print("\nContinue Example: Skip even numbers")
for num in range(1, 11):
    if num % 2 == 0:  # If number is even
        continue  # Skip to next iteration
    print(f"Odd number: {num}")

print("\n" + "=" * 60)
print("PART 3: LIST COMPREHENSION")
print("=" * 60)

# ==========================================
# LIST COMPREHENSION
# ==========================================
# A concise way to create lists
# Syntax: [expression for item in iterable if condition]

# Traditional way (without list comprehension)
print("\nTraditional way to create a list:")
squares_traditional = []
for num in range(1, 6):
    squares_traditional.append(num**2)
print(f"Squares: {squares_traditional}")

# List comprehension way (shorter and cleaner!)
print("\nList comprehension way:")
squares_comprehension = [num**2 for num in range(1, 6)]
print(f"Squares: {squares_comprehension}")

# More examples
print("\nList Comprehension Examples:")

# Example 1: Convert to uppercase
words = ["hello", "world", "python"]
uppercase_words = [word.upper() for word in words]
print(f"Uppercase: {uppercase_words}")

# Example 2: Filter even numbers
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_numbers = [num for num in numbers if num % 2 == 0]
print(f"Even numbers: {even_numbers}")

# Example 3: Conditional transformation
ages = [15, 20, 25, 30, 17]
adults = ["Adult" if age >= 18 else "Minor" for age in ages]
print(f"Age categories: {adults}")

# Example 4: Nested list comprehension (creating a matrix)
matrix = [[i * j for j in range(1, 4)] for i in range(1, 4)]
print(f"3x3 Matrix: {matrix}")

print("\n" + "=" * 60)
print("PART 4: GENERATORS")
print("=" * 60)

# ==========================================
# GENERATORS
# ==========================================
# Generators are like lists, but they generate values on-the-fly
# More memory efficient for large datasets
# Use 'yield' instead of 'return'


# Generator function (uses yield)
def count_up_to(max_count):
    """Generator that counts from 1 to max_count"""
    count = 1
    while count <= max_count:
        yield count  # yield produces a value and pauses
        count += 1


print("\nGenerator Function Example:")
counter = count_up_to(5)
print(f"Generator object: {counter}")
print("Values from generator:")
for num in counter:
    print(num, end=" ")
print()

# Generator expression (similar to list comprehension but with parentheses)
print("\nGenerator Expression Example:")
# List comprehension: creates entire list in memory
squares_list = [x**2 for x in range(5)]
print(f"List: {squares_list}")

# Generator expression: creates generator (lazy evaluation)
squares_gen = (x**2 for x in range(5))
print(f"Generator: {squares_gen}")
print("Values from generator:")
for square in squares_gen:
    print(square, end=" ")
print()

# Converting generator to list
squares_gen2 = (x**2 for x in range(5))
squares_list2 = list(squares_gen2)
print(f"Generator converted to list: {squares_list2}")

# ==========================================
# WHEN TO USE GENERATORS
# ==========================================
# Use generators when:
# - Working with large datasets (saves memory)
# - You don't need all values at once
# - You want lazy evaluation


def fibonacci_generator(n):
    """Generate first n Fibonacci numbers"""
    a, b = 0, 1
    count = 0
    while count < n:
        yield a
        a, b = b, a + b
        count += 1


print("\nFibonacci Generator Example:")
fib = fibonacci_generator(10)
print("First 10 Fibonacci numbers:")
for num in fib:
    print(num, end=" ")
print()

print("\n" + "=" * 60)
print("PART 5: PRACTICAL EXAMPLES")
print("=" * 60)

# ==========================================
# EXAMPLE 1: Grade Calculator with Control Flow
# ==========================================
print("\nExample 1: Grade Calculator")
scores = [85, 92, 78, 96, 88]

for score in scores:
    if score >= 90:
        grade = "A"
    elif score >= 80:
        grade = "B"
    elif score >= 70:
        grade = "C"
    else:
        grade = "F"
    print(f"Score {score}: Grade {grade}")

# ==========================================
# EXAMPLE 2: Shopping Cart with Loops
# ==========================================
print("\nExample 2: Shopping Cart Total")
cart = [
    {"item": "Apple", "price": 1.50, "quantity": 3},
    {"item": "Banana", "price": 0.75, "quantity": 5},
    {"item": "Orange", "price": 2.00, "quantity": 2},
]

total = 0
for product in cart:
    item_total = product["price"] * product["quantity"]
    total += item_total
    print(f"{product['item']}: ${item_total:.2f}")

print(f"Total: ${total:.2f}")

# ==========================================
# EXAMPLE 3: Finding Items with List Comprehension
# ==========================================
print("\nExample 3: Filtering Data")
students = [
    {"name": "Alice", "age": 20, "grade": 85},
    {"name": "Bob", "age": 19, "grade": 92},
    {"name": "Charlie", "age": 21, "grade": 78},
    {"name": "Diana", "age": 20, "grade": 95},
]

# Find students with grade >= 90 using list comprehension
top_students = [s["name"] for s in students if s["grade"] >= 90]
print(f"Top students (grade >= 90): {top_students}")

# Find average age
average_age = sum([s["age"] for s in students]) / len(students)
print(f"Average age: {average_age:.1f}")

# ==========================================
# EXAMPLE 4: Password Validator
# ==========================================
print("\nExample 4: Password Validator")


def validate_password(password):
    """Check if password meets requirements"""
    has_upper = any(char.isupper() for char in password)
    has_lower = any(char.islower() for char in password)
    has_digit = any(char.isdigit() for char in password)
    has_length = len(password) >= 8

    if has_upper and has_lower and has_digit and has_length:
        return True, "Password is valid!"
    else:
        issues = []
        if not has_upper:
            issues.append("needs uppercase letter")
        if not has_lower:
            issues.append("needs lowercase letter")
        if not has_digit:
            issues.append("needs a digit")
        if not has_length:
            issues.append("needs at least 8 characters")
        return False, ", ".join(issues)


test_passwords = ["Python123", "weak", "STRONG123", "python123"]
for pwd in test_passwords:
    is_valid, message = validate_password(pwd)
    status = "✓" if is_valid else "✗"
    print(f"{status} '{pwd}': {message}")

print("\n" + "=" * 60)
print("END OF TUTORIAL")
print("=" * 60)
print("\nKey Takeaways:")
print("- Use if/elif/else for decision-making")
print("- Use while loops when you don't know iterations in advance")
print("- Use for loops to iterate over collections")
print("- List comprehensions make code shorter and cleaner")
print("- Generators save memory for large datasets")
print("\nPractice by modifying these examples!")
