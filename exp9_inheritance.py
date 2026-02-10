"""
Experiment 9: Demonstrating Class Inheritance in Python

This experiment explores Object-Oriented Programming (OOP) concepts, specifically Inheritance.
It covers:
1.  **Inheritance**: Creating new classes (Child/Derived) based on existing ones (Parent/Base).
2.  **Code Reusability**: Using common attributes and methods from the Parent class.
3.  **Method Overriding**: Modifying the behavior of inherited methods in Child classes.
4.  **`super()` Function**: Accessing methods and properties of the Parent class.
"""


# Parent Class (Base Class)
class Animal:
    def __init__(self, name, species):
        self.name = name
        self.species = species
    
    def get_info(self):
        return f"Name: {self.name}, Species: {self.species}"

# Child Class - Dog inherits from Animal
class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name, "Dog")
        self.breed = breed
    
    def make_sound(self):
        print("Woof! Woof!")
    
    def get_info(self):
        return f"{super().get_info()}, Breed: {self.breed}"

# Child Class - Cat inherits from Animal
class Cat(Animal):
    def __init__(self, name, color):
        super().__init__(name, "Cat")
        self.color = color
    
    def make_sound(self):
        print("Meow!")
    
    def get_info(self):
        return f"{super().get_info()}, Color: {self.color}"

# Create objects and test
dog = Dog("Buddy", "Golden Retriever")
cat = Cat("Whiskers", "Orange")

print("=== Dog ===")
print(dog.get_info())
dog.make_sound()

print("\n=== Cat ===")
print(cat.get_info())
cat.make_sound()