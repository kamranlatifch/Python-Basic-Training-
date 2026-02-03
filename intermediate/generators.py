# Iterable is an object that can be iterated over[__getitem__ is defined inside it ]-> Means its an object that can give you iterator
# 2: Iterator is an object that has next method inside it -> Means its an object that can give you next item in the iterable
# 3: Iteration is the process of iterating over an iterable

# Genrators: Generators are iterators that can be used to iterate over a sequence of values [Generate values only one time]

for i in range(10000):
    print(i)
# This will take a lot of memory to store all the values in the list
# So we use generators to generate values on the fly[Generate values on the fly, and all the ram gets back to the system]


def generate_numbers(n):
    for i in range(n):
        yield i


# print(generate_numbers(10000))
# for i in generate_numbers(1000):
#     print(i)
obj1 = generate_numbers(2)
print(next(obj1))
print(next(obj1))
# error will be raised because there are no more values to generate
# print(next(obj1))
# print(next(obj1))
# int [num = 345] is not iterable vs string [num = "345"] is iterable
num = "345"
for i in num:
    print(i)
print("--------------------------------")
name = "Kamran"
iter1 = iter(name)
print(next(iter1))
print(next(iter1))
print(next(iter1))
# It will print the first character of the string 'Kam'
