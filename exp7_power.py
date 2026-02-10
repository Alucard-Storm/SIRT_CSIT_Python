"""
Experiment 7: Exponentiation (Calculating Base raised to Power)

This experiment demonstrates mathematical operations for calculating powers.
It covers:
1.  **Exponentiation Operator (**)**: Python's dedicated operator for calculating powers efficiently.
2.  **Type Conversion**: Handling different numeric inputs (float for base, integer for exponent).
3.  **Function Definition**: Encapsulating logic within reusable functions with clear parameters.
"""


# Get input from user
base = float(input("Enter the base number: "))
exponent = int(input("Enter the exponent: "))

# Calculate power using ** operator
result = base ** exponent

# Display the result
print(f"{base} raised to the power of {exponent} is: {result}")