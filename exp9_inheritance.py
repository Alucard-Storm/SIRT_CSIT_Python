# Experiment 9: Demonstrating Class Inheritance in Python

# Base Class (Parent Class)
class Animal:
    def __init__(self, name, species):
        """Initialize the animal with a name and species."""
        self.name = name
        self.species = species
    
    def make_sound(self):
        """A generic method meant to be overridden by subclasses."""
        print("Some generic animal sound")
    
    def get_info(self):
        """Return basic information about the animal."""
        return f"Name: {self.name}, Species: {self.species}"

# Derived Class (Child Class) - Inherits from Animal
class Dog(Animal):
    def __init__(self, name, breed):
        # super() calls the parent class constructor
        super().__init__(name, species="Dog")
        self.breed = breed
    
    def make_sound(self):
        # Overriding the parent class method
        print("Woof! Woof!")
    
    def get_info(self):
        # Extending the parent class information
        return f"{super().get_info()}, Breed: {self.breed}"

# Another Derived Class
class Cat(Animal):
    def __init__(self, name, color):
        super().__init__(name, species="Cat")
        self.color = color
    
    def make_sound(self):
        # Overriding the parent class method
        print("Meow!")
    
    def get_info(self):
        return f"{super().get_info()}, Color: {self.color}"

def main():
    # Creating instances (objects) of derived classes
    dog = Dog("Buddy", "Golden Retriever")
    cat = Cat("Whiskers", "Orange")
    
    print("=== Dog Information ===")
    print(dog.get_info())
    dog.make_sound()
    
    print("\n=== Cat Information ===")
    print(cat.get_info())
    cat.make_sound()

# Execution logic
if __name__ == "__main__":
    main()