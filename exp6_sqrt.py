"""
Experiment 6: Square Root Calculation Using the Math Module

This experiment introduces Python's standard library modules.
It covers:
1.  **Importing Modules**: Using the `import` statement to access the `math` library.
2.  **Math Functions**: Utilizing `math.sqrt()` for efficient mathematical computations.
3.  **Input Validation**: Checking for non-negative inputs since square roots of negative numbers are undefined in real numbers.
"""


import math

def calculate_square_root(number):
    """Calculates the square root of a non-negative number."""
    # math.sqrt is a built-in function from the math module
    return math.sqrt(number)

def main():
    try:
        # Input can be a floating point number
        number = float(input("Enter a number to find its square root: "))
        
        # Square root of a negative number is undefined in the real number system
        if number < 0:
            print("Error: Cannot calculate the square root of a negative number.")
            return
            
        # Call the calculation function
        math_sqrt = calculate_square_root(number)
        
        # Display the result
        print(f"The square root of {number} is: {math_sqrt}")
    
    except ValueError:
        # Handle non-numeric input
        print("Error: Please enter a valid numeric value.")

# Main guard to prevent execution on import
main()