# file name: comprehension.py
"""
1: List Comprehension:
    - A concise way to create lists
    - Syntax: [expression for item in iterable if condition]
    - Example: [x**2 for x in range(5)]
    - Example: [x for x in range(5) if x % 2 == 0]
    - Example: [x for x in range(5) if x % 2 != 0]
    - Example: [x for x in range(5) if x % 2 == 0]
2: Dictionary Comprehension:
    - A concise way to create dictionaries
    - Syntax: {key: value for item in iterable if condition}
    - Example: {x: x**2 for x in range(5)}
    - Example: {x: x**2 for x in range(5) if x % 2 == 0}
3: Set Comprehension:
    - A concise way to create sets
    - Syntax: {expression for item in iterable if condition}
    - Example: {x**2 for x in range(5)}
    - Example: {x**2 for x in range(5) if x % 2 == 0}
    - Example: {x**2 for x in range(5) if x % 2 != 0}
    - Example: {x**2 for x in range(5) if x % 2 == 0}
4: Generator Comprehension:
    - A concise way to create generators
    - Syntax: (expression for item in iterable if condition)
    - Example: (x**2 for x in range(5))
    - Example: (x**2 for x in range(5) if x % 2 == 0)
    - Example: (x**2 for x in range(5) if x % 2 != 0)
    - Example: (x**2 for x in range(5) if x % 2 == 0)

"""

# List Comprehension:

list_1 = [1, 2, 4, 8, 9, 12, 14, 15, 17, 18, 20, 21, 24, 25, 26, 28, 30]
divide_by_3_list = []
print("WITHOUT list comprehension:")
for item in list_1:
    if item % 3 == 0:
        divide_by_3_list.append(item)
print(divide_by_3_list)

# WITH list comprehension: we can do it in one line
print("WITH list comprehension:")
divide_by_3_list_2 = [item for item in list_1 if item % 3 == 0]
print(divide_by_3_list_2)

print("--------------------------------")
# Dictionary Comprehension:
print("WITH dictionary comprehension:")
dict_1 = {"a": 45, "b": 65, "A": 5}
print(
    {
        k.lower(): dict_1.get(k.lower(), 0) + dict_1.get(k.upper(), 0)
        for k in dict_1.keys()
    }
)

# 3: Set Comprehension:
print("WITH set comprehension:")
squared = {
    x**2 for x in [1, 2, 2, 2, 3, 3, 4, 5]
}  # set will remove the duplicate values
print(squared)

print("--------------------------------")
# Generator Comprehension:
print("WITH generator comprehension:")
gen = (i for i in range(56) if i % 3 == 0)
for item in gen:
    print(item)
