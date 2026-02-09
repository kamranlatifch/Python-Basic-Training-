# file name: enumerate.py
"""
1: Enumerate:
    - A function that returns a tuple containing the index and the value of the item in the iterable
    - Syntax: enumerate(iterable)
    - Example: enumerate([1,2,3,4,5])
    - Example: enumerate(["apple","banana","cherry"])
    - Example: enumerate({"a":1,"b":2,"c":3})
    - Example: enumerate((1,2,3,4,5))
    - Example: enumerate("12345")
    - Example: enumerate({"a":1,"b":2,"c":3})
"""

a = [
    "apple",
    "banana",
    "cherry",
    "date",
    "elderberry",
    "fig",
    "grape",
    "honeydew",
    "kiwi",
    "lemon",
    "mango",
    "nectarine",
    "orange",
    "pear",
    "pineapple",
    "plum",
    "raspberry",
    "strawberry",
    "tangerine",
    "watermelon",
]

# WITHOUT enumerate: print the items with even index
i = 0
for item in a:
    i += 1
    if i % 2 == 0:
        print(i, item)

# WITH enumerate: print the items with even index
for i, item in enumerate(a):
    if (i + 1) % 2 == 0:
        print(i, item)
