# Experiment 9: Inheritance

class Animal:
    def __init__(self, name, species):
        self.name = name
        self.species = species
    
    def make_sound(self):
        print("Some generic animal sound")
    
    def get_info(self):
        return f"Name: {self.name}, Species: {self.species}"

class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name, species="Dog")
        self.breed = breed
    
    def make_sound(self):
        print("Woof! Woof!")
    
    def get_info(self):
        return f"{super().get_info()}, Breed: {self.breed}"

class Cat(Animal):
    def __init__(self, name, color):
        super().__init__(name, species="Cat")
        self.color = color
    
    def make_sound(self):
        print("Meow!")
    
    def get_info(self):
        return f"{super().get_info()}, Color: {self.color}"

def main():
    dog = Dog("Buddy", "Golden Retriever")
    cat = Cat("Whiskers", "Orange")
    
    print("=== Dog Info ===")
    print(dog.get_info())
    dog.make_sound()
    
    print("\n=== Cat Info ===")
    print(cat.get_info())
    cat.make_sound()

if __name__ == "__main__":
    main() 