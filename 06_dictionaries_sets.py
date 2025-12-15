"""
===========================================
PYTHON TUTORIAL: Dictionaries and Sets
===========================================
This file covers dictionaries and sets.
Run this file with: python3 06_dictionaries_sets.py
"""

print("=" * 60)
print("PART 1: DICTIONARIES")
print("=" * 60)

# Creating dictionaries (key-value pairs)
student = {"name": "Alice", "age": 20, "grade": "A"}
phonebook = {"Alice": "555-1234", "Bob": "555-5678"}
empty_dict = {}
print(f"\nDictionaries: {student}, {phonebook}")

# Accessing values
print(f"\nAccessing: student['name']={student['name']}")
print(f"student.get('age')={student.get('age')}")
print(
    f"student.get('city', 'Unknown')={student.get('city', 'Unknown')}"
)  # Default value

# Modifying dictionaries
student["age"] = 21  # Update existing key
student["city"] = "New York"  # Add new key-value pair
print(f"\nAfter modifications: {student}")

# Deleting key-value pairs
del student["grade"]
print(f"After del student['grade']: {student}")

removed_value = student.pop("city")  # Remove and return value
print(f"After pop('city'): {student}, removed={removed_value}")

# Dictionary methods
print(f"\nDictionary methods:")
print(f"keys(): {list(student.keys())}")
print(f"values(): {list(student.values())}")
print(f"items(): {list(student.items())}")

# Iterating over dictionaries
print("\nIterating:")
for key in student:
    print(f"  {key}: {student[key]}")

for key, value in student.items():
    print(f"  {key} = {value}")

# Dictionary comprehension
print("\nDictionary comprehension:")
squares = {x: x**2 for x in range(1, 6)}
print(f"Squares: {squares}")

# Creating from lists
keys = ["a", "b", "c"]
values = [1, 2, 3]
dict_from_lists = dict(zip(keys, values))
print(f"From lists: {dict_from_lists}")

# Nested dictionaries
nested = {
    "person1": {"name": "Alice", "age": 25},
    "person2": {"name": "Bob", "age": 30},
}
print(f"\nNested dict: {nested}")
print(f"Access nested: {nested['person1']['name']}")

# Common dictionary methods
student_copy = student.copy()
print(f"\nCopy: {student_copy}")
student_copy.clear()
print(f"After clear(): {student_copy}")

student.update({"age": 22, "email": "alice@example.com"})
print(f"After update(): {student}")

print("\n" + "=" * 60)
print("PART 2: SETS")
print("=" * 60)

# Creating sets (unordered, unique elements)
fruits = {"apple", "banana", "orange"}
numbers = {1, 2, 3, 4, 5}
empty_set = set()  # Note: {} creates empty dict, not set!
print(f"\nSets: {fruits}, {numbers}")

# Sets automatically remove duplicates
duplicates = {1, 2, 2, 3, 3, 3}
print(f"Duplicates removed: {duplicates}")

# Adding and removing elements
fruits.add("grape")
print(f"After add('grape'): {fruits}")

fruits.remove("banana")  # Raises error if not found
print(f"After remove('banana'): {fruits}")

fruits.discard("mango")  # Doesn't raise error if not found
print(f"After discard('mango'): {fruits}")

# Set operations
set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}

print(f"\nSet operations:")
print(f"set1 = {set1}")
print(f"set2 = {set2}")

# Union: all elements from both sets
union = set1.union(set2)
print(f"Union (set1 | set2): {union}")

# Intersection: common elements
intersection = set1.intersection(set2)
print(f"Intersection (set1 & set2): {intersection}")

# Difference: elements in set1 but not in set2
difference = set1.difference(set2)
print(f"Difference (set1 - set2): {difference}")

# Symmetric difference: elements in either set, but not both
symmetric_diff = set1.symmetric_difference(set2)
print(f"Symmetric difference (set1 ^ set2): {symmetric_diff}")

# Subset and superset
set3 = {2, 3}
print(f"\nset3 = {set3}")
print(f"Is subset? set3.issubset(set1) = {set3.issubset(set1)}")
print(f"Is superset? set1.issuperset(set3) = {set1.issuperset(set3)}")
print(f"Are disjoint? set1.isdisjoint(set3) = {set1.isdisjoint(set3)}")

# Set methods
fruits = {"apple", "banana", "orange"}
print(f"\nSet methods:")
print(f"len(fruits) = {len(fruits)}")
print(f"'apple' in fruits = {'apple' in fruits}")

# Set comprehension
even_squares = {x**2 for x in range(1, 11) if x % 2 == 0}
print(f"\nSet comprehension: {even_squares}")

print("\n" + "=" * 60)
print("PART 3: PRACTICAL EXAMPLES")
print("=" * 60)

# Example 1: Word counter using dictionary
text = "hello world hello python"
words = text.split()
word_count = {}

for word in words:
    word_count[word] = word_count.get(word, 0) + 1

print(f"\nWord counter: {word_count}")

# Example 2: Finding common elements between lists using sets
list1 = [1, 2, 3, 4, 5]
list2 = [4, 5, 6, 7, 8]
common = set(list1) & set(list2)
print(f"\nCommon elements: {common}")

# Example 3: Removing duplicates from list using set
duplicate_list = [1, 2, 2, 3, 3, 3, 4, 5]
unique_list = list(set(duplicate_list))
print(f"Original: {duplicate_list}")
print(f"Unique: {unique_list}")

# Example 4: Student database
students = {
    "001": {"name": "Alice", "grades": [85, 90, 78]},
    "002": {"name": "Bob", "grades": [92, 88, 95]},
    "003": {"name": "Charlie", "grades": [75, 82, 80]},
}

print("\nStudent database:")
for student_id, info in students.items():
    avg = sum(info["grades"]) / len(info["grades"])
    print(f"  {info['name']} (ID: {student_id}): avg={avg:.1f}")

print("\n" + "=" * 60)
print("END OF TUTORIAL")
print("=" * 60)
print("\nKey Takeaways:")
print("- Dictionaries: key-value pairs, mutable, use {}")
print("- Sets: unique elements, unordered, use set() or {}")
print("- Dictionary: use .get() for safe access")
print("- Set operations: union (|), intersection (&), difference (-)")
print("- Sets are great for removing duplicates and fast lookups")
