#  Ability to take different forms
# Example: A dog is an animal, but a dog can also be a dog
# Example: A cat is an animal, but a cat can also be a cat
# Example: A bird is an animal, but a bird can also be a bird
# Example: A fish is an animal, but a fish can also be a fish

# Example: A dog is an animal, but a dog can also be a dog
# Example: A cat is an animal, but a cat can also be a cat
# Example: A bird is an animal, but a bird can also be a bird
# Example: A fish is an animal, but a fish can also be a fish
# file name: 11_Polymorphism.py


class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        return f"{self.name} says Animal sound!"


class Dog(Animal):
    def speak(self):
        return f"{self.name} says Woof!"


class Cat(Animal):
    def speak(self):
        return f"{self.name} says Meow!"


class Bird(Animal):
    def speak(self):
        return f"{self.name} says Tweet!"


class Fish(Animal):
    def speak(self):
        return f"{self.name} says Blub!"


animal = Animal("Animal")
dog = Dog("Dog")
cat = Cat("Cat")
bird = Bird("Bird")
fish = Fish("Fish")

print(animal.speak())
print(dog.speak())
print(cat.speak())
print(bird.speak())
print(fish.speak())
