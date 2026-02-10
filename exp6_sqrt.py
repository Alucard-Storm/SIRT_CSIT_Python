"""
Experiment 6: Square Root Calculation Using the Math Module

This experiment introduces Python's standard library modules.
It covers:
1.  **Importing Modules**: Using the `import` statement to access the `math` library.
2.  **Math Functions**: Utilizing `math.sqrt()` for efficient mathematical computations.
3.  **Input Validation**: Checking for non-negative inputs since square roots of negative numbers are undefined in real numbers.
"""


import math

# Get input from user
number = float(input("Enter a number to find its square root: "))

# Check for negative numbers
if number < 0:
    print("Error: Cannot find square root of a negative number.")
else:
    # Calculate and display square root
    result = math.sqrt(number)
    print(f"The square root of {number} is: {result}")