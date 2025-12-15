"""
===========================================
PYTHON TUTORIAL: Lists, Tuples and Named Tuples
===========================================
This file covers lists, tuples, and named tuples.
Run this file with: python3 05_lists_tuples.py
"""

print("=" * 60)
print("PART 1: LISTS")
print("=" * 60)

# Creating lists
fruits = ["apple", "banana", "orange"]
numbers = [1, 2, 3, 4, 5]
mixed = [1, "hello", 3.14, True]
empty = []
print(f"\nLists: {fruits}, {numbers}, {mixed}")

# Indexing and slicing (same as strings)
print(f"\nIndexing: fruits[0]={fruits[0]}, fruits[-1]={fruits[-1]}")
print(f"Slicing: fruits[0:2]={fruits[0:2]}, fruits[1:]={fruits[1:]}")

# Appending elements
fruits.append("grape")
print(f"After append('grape'): {fruits}")

# Modifying elements
fruits[0] = "mango"
print(f"After fruits[0]='mango': {fruits}")

# Inserting elements
fruits.insert(1, "kiwi")
print(f"After insert(1, 'kiwi'): {fruits}")

# Deleting elements
fruits.remove("banana")  # Remove by value
print(f"After remove('banana'): {fruits}")

del fruits[0]  # Remove by index
print(f"After del fruits[0]: {fruits}")

popped = fruits.pop()  # Remove and return last element
print(f"After pop(): {fruits}, popped: {popped}")

# Common list methods
numbers = [3, 1, 4, 1, 5, 9, 2, 6]
print(f"\nList: {numbers}")
print(
    f"len(numbers)={len(numbers)}, max(numbers)={max(numbers)}, min(numbers)={min(numbers)}"
)
print(f"numbers.count(1)={numbers.count(1)}")
print(f"numbers.index(4)={numbers.index(4)}")

# Sorting
numbers.sort()
print(f"After sort(): {numbers}")
numbers.reverse()
print(f"After reverse(): {numbers}")

# Extending lists
list1 = [1, 2, 3]
list2 = [4, 5]
list1.extend(list2)
print(f"\nExtend: {list1}")

# List comprehension (concise way to create lists)
print("\nList comprehensions:")
squares = [x**2 for x in range(1, 6)]
print(f"Squares: {squares}")

even_squares = [x**2 for x in range(1, 11) if x % 2 == 0]
print(f"Even squares: {even_squares}")

words = ["hello", "world", "python"]
uppercase = [word.upper() for word in words]
print(f"Uppercase: {uppercase}")

print("\n" + "=" * 60)
print("PART 2: TUPLES")
print("=" * 60)

# Creating tuples (use parentheses or just commas)
coordinates = (10, 20)
colors = "red", "green", "blue"
single = (42,)  # Note: comma required for single element
print(f"\nTuples: {coordinates}, {colors}, {single}")

# Tuples are IMMUTABLE (cannot be changed)
print(f"\nIndexing: coordinates[0]={coordinates[0]}, colors[-1]={colors[-1]}")
print(f"Slicing: colors[0:2]={colors[0:2]}")

# Tuples cannot be modified (uncomment to see error):
# coordinates[0] = 15  # This will cause an error!

# When to use tuples vs lists?
# - Tuples: fixed data, faster, can be dictionary keys
# - Lists: mutable data, need to change

# Tuple methods
numbers_tuple = (3, 1, 4, 1, 5)
print(f"\nTuple: {numbers_tuple}")
print(f"numbers_tuple.count(1)={numbers_tuple.count(1)}")
print(f"numbers_tuple.index(4)={numbers_tuple.index(4)}")

# Unpacking tuples
x, y = coordinates
print(f"\nUnpacking: x={x}, y={y}")


# Tuple unpacking in functions (returning multiple values)
def get_name_age():
    return "Alice", 25


name, age = get_name_age()
print(f"Function returns: name={name}, age={age}")

# Converting between lists and tuples
my_list = [1, 2, 3]
my_tuple = tuple(my_list)
back_to_list = list(my_tuple)
print(f"\nConvert: list={my_list}, tuple={my_tuple}, back to list={back_to_list}")

print("\n" + "=" * 60)
print("PART 3: NAMED TUPLES")
print("=" * 60)

# Named tuples: tuples with named fields (like a simple class)
from collections import namedtuple

# Define a named tuple type
Point = namedtuple("Point", ["x", "y"])
Person = namedtuple("Person", ["name", "age", "city"])

# Create instances
p1 = Point(10, 20)
p2 = Point(x=30, y=40)
person1 = Person("Alice", 25, "New York")

print(f"\nNamed tuples:")
print(f"Point: {p1}, x={p1.x}, y={p1.y}")
print(f"Point: {p2}, x={p2.x}, y={p2.y}")
print(f"Person: {person1}, name={person1.name}, age={person1.age}")

# Named tuples are still tuples (immutable, can be indexed)
print(f"\nStill tuples: p1[0]={p1[0]}, person1[1]={person1[1]}")

# But also have named attributes (more readable)
distance = ((p2.x - p1.x) ** 2 + (p2.y - p1.y) ** 2) ** 0.5
print(f"Distance between points: {distance:.2f}")

# Converting to dictionary
person_dict = person1._asdict()
print(f"\nAs dictionary: {person_dict}")

# Creating from iterable
person2 = Person._make(["Bob", 30, "Boston"])
print(f"Created from list: {person2}")

print("\n" + "=" * 60)
print("PART 4: PRACTICAL EXAMPLES")
print("=" * 60)

# Example 1: Student grades using lists
students = ["Alice", "Bob", "Charlie"]
grades = [[85, 90, 78], [92, 88, 95], [75, 82, 80]]

for i, student in enumerate(students):
    avg = sum(grades[i]) / len(grades[i])
    print(f"{student}: grades={grades[i]}, average={avg:.1f}")

# Example 2: Using tuples for coordinates
Rectangle = namedtuple("Rectangle", ["width", "height"])


def area(rect):
    return rect.width * rect.height


rect = Rectangle(10, 5)
print(f"\nRectangle {rect}: area={area(rect)}")

# Example 3: List comprehension with filtering
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
evens = [n for n in numbers if n % 2 == 0]
print(f"\nNumbers: {numbers}")
print(f"Even numbers: {evens}")

print("\n" + "=" * 60)
print("END OF TUTORIAL")
print("=" * 60)
print("\nKey Takeaways:")
print("- Lists: mutable, use [] or list()")
print("- Tuples: immutable, use () or just commas")
print("- Named tuples: readable tuples with named fields")
print("- List comprehension: concise way to create lists")
print("- Use lists when you need to modify")
print("- Use tuples for fixed, unchangeable data")
