# Experiment 6: Square Root Calculation

import math

def calculate_square_root(number):
    # Using built-in math function
    return math.sqrt(number)

def newton_sqrt(number, precision=0.0001):
    # Newton's method for square root
    guess = number / 2
    while abs(guess * guess - number) > precision:
        guess = (guess + number / guess) / 2
    return guess

def main():
    try:
        number = float(input("Enter a number to find its square root: "))
        if number < 0:
            print("Cannot calculate square root of negative number")
            return
            
        math_sqrt = calculate_square_root(number)
        newton_method_sqrt = newton_sqrt(number)
        
        print(f"Square root using math.sqrt: {math_sqrt}")
        print(f"Square root using Newton's method: {newton_method_sqrt}")
    
    except ValueError:
        print("Please enter a valid number")

if __name__ == "__main__":
    main() 