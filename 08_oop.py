"""
===========================================
PYTHON TUTORIAL: Object-Oriented Programming (OOP)
===========================================
This file covers classes, objects, inheritance, and polymorphism.
Run this file with: python3 08_oop.py
"""

print("=" * 60)
print("PART 1: CLASSES AND OBJECTS")
print("=" * 60)


# Class: blueprint for creating objects
class Dog:
    species = "Canis familiaris"  # Class attribute

    def __init__(self, name, age):  # Constructor
        self.name = name  # Instance attributes
        self.age = age

    def bark(self):  # Method
        return f"{self.name} says Woof!"


# Creating objects (instances)
dog1 = Dog("Buddy", 3)
dog2 = Dog("Max", 5)
print(f"\ndog1: {dog1.name}, {dog1.bark()}")
print(f"dog2: {dog2.name}, Species: {dog2.species}")

print("\n" + "=" * 60)
print("PART 2: ENCAPSULATION")
print("=" * 60)


# Encapsulation: hiding internal details (use _ prefix for private)
class BankAccount:
    def __init__(self, balance):
        self._balance = balance  # Private attribute

    def deposit(self, amount):
        if amount > 0:
            self._balance += amount
            return f"Balance: ${self._balance}"
        return "Invalid amount"

    def get_balance(self):
        return self._balance


account = BankAccount(100)
print(f"\nBalance: ${account.get_balance()}")
print(account.deposit(50))

print("\n" + "=" * 60)
print("PART 3: INHERITANCE")
print("=" * 60)


# Base class
class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def speak(self):
        return "Some generic sound"


# Child class inherits from parent
class Cat(Animal):
    def speak(self):
        return f"{self.name} says Meow!"


class Bird(Animal):
    def __init__(self, name, age, can_fly):
        super().__init__(name, age)  # Call parent constructor
        self.can_fly = can_fly

    def speak(self):
        return f"{self.name} says Tweet!"


cat = Cat("Whiskers", 2)
bird = Bird("Tweety", 1, True)
print(f"\n{cat.speak()}")
print(f"{bird.speak()}")

print("\n" + "=" * 60)
print("PART 4: POLYMORPHISM")
print("=" * 60)


# Polymorphism: same interface, different behavior
class Rectangle:
    def __init__(self, width, height):
        self.width, self.height = width, height

    def area(self):
        return self.width * self.height


class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14159 * self.radius**2


def print_area(shape):  # Polymorphic function
    print(f"Area: {shape.area()}")


print("\nPolymorphism:")
print_area(Rectangle(5, 3))
print_area(Circle(4))

print("\n" + "=" * 60)
print("PART 5: METHOD OVERRIDING")
print("=" * 60)


# Overriding: child class redefines parent method
class Vehicle:
    def start(self):
        return "Vehicle is starting"


class Car(Vehicle):
    def start(self):  # Override
        return "Car engine is starting"


class ElectricCar(Car):
    def start(self):  # Override again
        return "Electric car starts silently"


print("\nOverriding examples:")
print(f"Vehicle: {Vehicle().start()}")
print(f"Car: {Car().start()}")
print(f"ElectricCar: {ElectricCar().start()}")


# Using super() to call parent method
class Animal:
    def make_sound(self):
        return "Generic sound"


class Dog(Animal):
    def make_sound(self):
        return f"{super().make_sound()}, but this dog says Woof!"


print(f"\nUsing super(): {Dog().make_sound()}")

print("\n" + "=" * 60)
print("PART 6: METHOD OVERLOADING CONSTRAINTS")
print("=" * 60)


# Python doesn't support traditional method overloading
# Use default arguments or *args, **kwargs instead
class Calculator:
    def add(self, a, b=0, c=0):  # Default arguments
        return a + b + c

    def multiply(self, *args):  # *args for variable arguments
        result = 1
        for num in args:
            result *= num
        return result


calc = Calculator()
print(f"\nOverloading workaround:")
print(
    f"add(5)={calc.add(5)}, add(5,3)={calc.add(5, 3)}, add(1,2,3)={calc.add(1, 2, 3)}"
)
print(f"multiply(2,3)={calc.multiply(2, 3)}, multiply(2,3,4)={calc.multiply(2, 3, 4)}")
print("\nNote: Python doesn't support traditional overloading.")
print("Use default args or *args/**kwargs instead.")

print("\n" + "=" * 60)
print("PART 7: PRACTICAL EXAMPLE")
print("=" * 60)


class Employee:
    def __init__(self, name, employee_id, salary):
        self.name, self.employee_id, self.salary = name, employee_id, salary

    def calculate_bonus(self):
        return self.salary * 0.1

    def display_info(self):
        return f"Employee: {self.name} (ID: {self.employee_id})"


class Manager(Employee):
    def __init__(self, name, employee_id, salary, department):
        super().__init__(name, employee_id, salary)
        self.department = department

    def calculate_bonus(self):  # Override
        return self.salary * 0.2

    def display_info(self):  # Override
        return f"{super().display_info()}, Manager of {self.department}"


employees = [
    Employee("Alice", "E001", 50000),
    Manager("Bob", "M001", 80000, "Engineering"),
]
print("\nEmployee system:")
for emp in employees:
    print(f"{emp.display_info()}, Bonus: ${emp.calculate_bonus():.2f}")

print("\n" + "=" * 60)
print("END OF TUTORIAL")
print("=" * 60)
print("\nKey Takeaways:")
print("- Class: blueprint, Object: instance of class")
print("- Encapsulation: hide internal details")
print("- Inheritance: child classes inherit from parent")
print("- Polymorphism: same interface, different behavior")
print("- Overriding: child redefines parent method")
print("- Python doesn't support traditional overloading")
print("- Use default args or *args/**kwargs for flexibility")
print("\nOOP helps organize code into reusable components!")
