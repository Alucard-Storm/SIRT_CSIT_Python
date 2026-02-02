# Experiment 6: Square Root Calculation Using the Math Module

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
if __name__ == "__main__":
    main()