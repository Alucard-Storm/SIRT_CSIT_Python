# Experiment 10: Functional Polymorphism

class Shape:
    def area(self):
        pass
    
    def perimeter(self):
        pass

class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width
    
    def area(self):
        return self.length * self.width
    
    def perimeter(self):
        return 2 * (self.length + self.width)

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    
    def area(self):
        return 3.14159 * self.radius * self.radius
    
    def perimeter(self):
        return 2 * 3.14159 * self.radius

def calculate_area(shape):
    return shape.area()

def main():
    # Creating different shapes
    rectangle = Rectangle(5, 3)
    circle = Circle(4)
    
    # Demonstrating polymorphism
    shapes = [rectangle, circle]
    
    for shape in shapes:
        print(f"\nShape: {shape.__class__.__name__}")
        print(f"Area: {calculate_area(shape)}")
        print(f"Perimeter: {shape.perimeter()}")

main() 