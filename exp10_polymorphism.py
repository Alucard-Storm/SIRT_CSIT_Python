"""
Experiment 10: Demonstrating Polymorphism using Shapes

This experiment explores the concept of Polymorphism in Object-Oriented Programming.
It covers:
1.  **Polymorphism**: The ability of different classes to be treated as instances of the same general class through a common interface.
2.  **Abstract Base Classes**: Defining a common `Shape` interface with methods that must be implemented by subclasses.
3.  **Method Implementation**: Creating specific implementations (`Rectangle`, `Circle`) for the abstract methods.
4.  **Unified Interface**: Using a single function to interact with different objects interchangeably.
"""


# Parent class (base class)
class Shape:
    def area(self):
        pass
    
    def perimeter(self):
        pass

# Rectangle class
class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width
    
    def area(self):
        return self.length * self.width
    
    def perimeter(self):
        return 2 * (self.length + self.width)

# Circle class
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    
    def area(self):
        return 3.14159 * self.radius * self.radius
    
    def perimeter(self):
        return 2 * 3.14159 * self.radius

# Create shapes
rectangle = Rectangle(5, 3)
circle = Circle(4)

# Store in a list
shapes = [rectangle, circle]

# Display information for each shape
for shape in shapes:
    print(f"\nShape: {shape.__class__.__name__}")
    print(f"Area: {shape.area()}")
    print(f"Perimeter: {shape.perimeter()}")