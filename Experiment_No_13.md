# Experiment No 13

## Aim
Functional Polymorphism

## Objective
Achieve polymorphism using default arguments or variable-length parameters.

## Process Flow
1. Define a function `area` with a default argument for breadth.
2. If breadth is not provided, calculate area of a square.
3. If breadth is provided, calculate area of a rectangle.
4. Call the function with one and two arguments.

## Code
```python
def area(l, b=None):
    if b is None:
        return l * l # Square
    else:
        return l * b # Rectangle

print("Area of square (side 5):", area(5))
print("Area of rectangle (5x10):", area(5, 10))
```
---

## Outcome

```bash
Area of square (side 5): 25
Area of rectangle (5x10): 50
```
