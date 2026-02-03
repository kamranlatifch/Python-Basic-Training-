# file name: map_filter_reduce.py
"""
1: Map:
    - A function that applies a function to each item in an iterable and returns a new iterable
    - Syntax: map(function, iterable)
    - Example: map(lambda x: x*2, [1,2,3,4,5])
    - Example: map(lambda x: x*2, {1,2,3,4,5})
    - Example: map(lambda x: x*2, (1,2,3,4,5))
    - Example: map(lambda x: x*2, "12345")
    - Example: map(lambda x: x*2, {"a":1,"b":2,"c":3})
    - Example: map(lambda x: x*2, {"a":1,"b":2,"c":3})

2: Filter:
    - A function that filters out items from an iterable based on a condition
    - Syntax: filter(function, iterable)
    - Example: filter(lambda x: x%2==0, [1,2,3,4,5])
    - Example: filter(lambda x: x%2==0, {1,2,3,4,5})
    - Example: filter(lambda x: x%2==0, (1,2,3,4,5))
    - Example: filter(lambda x: x%2==0, "12345")
    - Example: filter(lambda x: x%2==0, {"a":1,"b":2,"c":3})
    - Example: filter(lambda x: x%2==0, {"a":1,"b":2,"c":3})
    - Example: filter(lambda x: x%2==0, {"a":1,"b":2,"c":3})

3: Reduce:
    - A function that reduces an iterable to a single value
    - Syntax: reduce(function, iterable)
    - Example: reduce(lambda x,y: x+y, [1,2,3,4,5])
    - Example: reduce(lambda x,y: x+y, {1,2,3,4,5})
    - Example: reduce(lambda x,y: x+y, (1,2,3,4,5))
    - Example: reduce(lambda x,y: x+y, "12345")
    - Example: reduce(lambda x,y: x+y, {"a":1,"b":2,"c":3})
    - Example: reduce(lambda x,y: x+y, {"a":1,"b":2,"c":3})

"""
# 1: Map:
h1 = [1, 2, 4, 5, 7]
sq = []
for item in h1:
    sq.append(item**2)
print(sq)


# WITH map:
print("WITH map:")


def square(x):
    return x**2


sq2 = map(square, h1)
print(sq2)
# WITH list comprehension:
print("WITH list comprehension:")
sq3 = [x**2 for x in h1]
print(sq3)
print("--------------------------------")


# 2: Filter:
def grater_than_2(x):
    if x > 2:
        return True
    else:
        return False


print("WITH filter:")
greater_th_2 = list(filter(grater_than_2, h1))
print(greater_th_2)
