# Experiment 6: Square Root Calculation

import math

def calculate_square_root(number):
    # Using built-in math function
    return math.sqrt(number)

def main():
    try:
        number = float(input("Enter a number to find its square root: "))
        if number < 0:
            print("Cannot calculate square root of negative number")
            return
            
        math_sqrt = calculate_square_root(number)
        
        print(f"Square root using math.sqrt: {math_sqrt}")
    
    except ValueError:
        print("Please enter a valid number")

main() 