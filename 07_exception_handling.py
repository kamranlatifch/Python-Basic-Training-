"""
===========================================
PYTHON TUTORIAL: Exception Handling
===========================================
This file covers exception handling in Python.
Run this file with: python3 07_exception_handling.py
"""

print("=" * 60)
print("PART 1: WHAT ARE EXCEPTIONS?")
print("=" * 60)

print("\nExceptions are runtime errors that can crash your program.")
print("Examples: dividing by zero, accessing non-existent files, invalid input")

print("\n" + "=" * 60)
print("PART 2: TRY-EXCEPT BLOCKS")
print("=" * 60)

# Basic try-except
print("\nExample 1: Handling division by zero")
try:
    result = 10 / 0
except ZeroDivisionError:
    print("Error: Cannot divide by zero!")

# Multiple exception types
print("\nExample 2: Handling multiple exceptions")
try:
    value = int("abc")
except ValueError:
    print("Error: Invalid input!")
except ZeroDivisionError:
    print("Error: Cannot divide by zero!")

# Catching multiple in one block
print("\nExample 3: Catching multiple exceptions")
try:
    num = int("42")
    result = 100 / num
except (ValueError, ZeroDivisionError) as e:
    print(f"Error: {e}")
else:
    print(f"Success! Result: {result}")

# Generic exception handling
print("\nExample 4: Generic exception")
try:
    data = [1, 2, 3]
    print(data[10])
except IndexError as e:
    print(f"IndexError: {e}")

print("\n" + "=" * 60)
print("PART 3: COMMON EXCEPTION TYPES")
print("=" * 60)

print("\n1. ValueError:")
try:
    int("not a number")
except ValueError as e:
    print(f"  {e}")

print("\n2. TypeError:")
try:
    "hello" + 5
except TypeError as e:
    print(f"  {e}")

print("\n3. IndexError:")
try:
    my_list = [1, 2, 3]
    print(my_list[10])
except IndexError as e:
    print(f"  {e}")

print("\n4. KeyError:")
try:
    my_dict = {"name": "Alice"}
    print(my_dict["age"])
except KeyError as e:
    print(f"  {e}")

print("\n5. FileNotFoundError:")
try:
    with open("nonexistent.txt", "r", encoding="utf-8") as f:
        content = f.read()
except FileNotFoundError as e:
    print(f"  {e}")

print("\n6. ZeroDivisionError:")
try:
    result = 10 / 0
except ZeroDivisionError as e:
    print(f"  {e}")

print("\n" + "=" * 60)
print("PART 4: ELSE AND FINALLY BLOCKS")
print("=" * 60)

# else: runs only if no exception
print("\nExample with else:")
try:
    num = int("42")
    result = 100 / num
except (ValueError, ZeroDivisionError) as e:
    print(f"Error: {e}")
else:
    print(f"Success! Result: {result}")

# finally: always runs
print("\nExample with finally:")
test_file = None
try:
    test_file = open("test.txt", "w", encoding="utf-8")
    test_file.write("Hello")
    result = 10 / 0
except ZeroDivisionError:
    print("Division error occurred")
finally:
    print("Finally: This always runs")
    if test_file:
        test_file.close()

print("\n" + "=" * 60)
print("PART 5: RAISING EXCEPTIONS")
print("=" * 60)


def check_age(age):
    if age < 0:
        raise ValueError("Age cannot be negative")
    if age < 18:
        raise ValueError("Must be 18 or older")
    return f"Age {age} is valid"


print("\nRaising exceptions:")
for age in [-5, 15, 25]:
    try:
        result = check_age(age)
        print(f"Success: {result}")
    except ValueError as e:
        print(f"Error: {e}")

print("\n" + "=" * 60)
print("PART 6: BEST PRACTICES")
print("=" * 60)

print("\n1. Be specific with exception types:")
print("   ❌ Bad: except Exception:")
print("   ✅ Good: except ValueError:")

print("\n2. Don't ignore exceptions silently:")
print("   ❌ Bad: except: pass")
print("   ✅ Good: except ValueError as e: print(f'Error: {e}')")

print("\n3. Use else for code that runs only if no exception:")
try:
    data = {"name": "Alice"}
    name = data["name"]
except KeyError:
    print("Key not found")
else:
    print(f"Found: {name}")

print("\n4. Use finally for cleanup (files, connections):")
print("   - Always closes files/resources")
print("   - Always runs, even if exception occurs")

print("\n5. Provide meaningful error messages:")


def divide(a, b):
    if b == 0:
        raise ValueError(f"Cannot divide {a} by zero")
    return a / b


try:
    divide(10, 0)
except ValueError as e:
    print(f"Meaningful error: {e}")

print("\n6. Handle exceptions at the right level:")


def read_file(filename):
    try:
        with open(filename, "r", encoding="utf-8") as f:
            return f.read()
    except FileNotFoundError:
        return None


content = read_file("nonexistent.txt")
if content is None:
    print("File not found, using default")

print("\n" + "=" * 60)
print("PART 7: PRACTICAL EXAMPLE")
print("=" * 60)


def safe_divide(a, b):
    """Safely divide two numbers"""
    try:
        return a / b
    except ZeroDivisionError:
        print(f"Error: Cannot divide {a} by zero")
        return None
    except TypeError:
        print("Error: Both arguments must be numbers")
        return None


print("\nSafe division:")
print(f"10 / 2 = {safe_divide(10, 2)}")
print(f"10 / 0 = {safe_divide(10, 0)}")
print(f"'10' / 2 = {safe_divide('10', 2)}")

print("\n" + "=" * 60)
print("END OF TUTORIAL")
print("=" * 60)
print("\nKey Takeaways:")
print("- Use try-except to handle errors gracefully")
print("- Be specific with exception types")
print("- Use else for code that runs only if no error")
print("- Use finally for cleanup that always runs")
print("- Raise exceptions with meaningful messages")
print("- Don't ignore exceptions silently")
print("\nException handling makes programs more robust!")
