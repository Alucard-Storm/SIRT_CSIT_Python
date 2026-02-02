# Experiment 10: Demonstrating Polymorphism using Shapes

# Base class defining an interface
class Shape:
    def area(self):
        """Abstract method to be implemented by shapes."""
        pass
    
    def perimeter(self):
        """Abstract method to be implemented by shapes."""
        pass

# Rectangle implementation of the Shape interface
class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width
    
    def area(self):
        # Area = L * W
        return self.length * self.width
    
    def perimeter(self):
        # Perimeter = 2 * (L + W)
        return 2 * (self.length + self.width)

# Circle implementation of the Shape interface
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    
    def area(self):
        # Area = PI * R^2
        return 3.14159 * self.radius * self.radius
    
    def perimeter(self):
        # Perimeter = 2 * PI * R
        return 2 * 3.14159 * self.radius

def calculate_area(shape):
    """
    Polymorphic function: It doesn't care what kind of shape it receives,
    as long as the object has an area() method.
    """
    return shape.area()

def main():
    # Instantiate specific shapes
    rectangle = Rectangle(5, 3)
    circle = Circle(4)
    
    # Store them in a list (polymorphic collection)
    shapes = [rectangle, circle]
    
    for shape in shapes:
        # Each object knows how to report its own class name and calculate its own data
        print(f"\nShape Type: {shape.__class__.__name__}")
        print(f"Calculated Area: {calculate_area(shape)}")
        print(f"Calculated Perimeter: {shape.perimeter()}")

# Main guard
if __name__ == "__main__":
    main()