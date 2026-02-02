"""
Experiment 7: Exponentiation (Calculating Base raised to Power)

This experiment demonstrates mathematical operations for calculating powers.
It covers:
1.  **Exponentiation Operator (**)**: Python's dedicated operator for calculating powers efficiently.
2.  **Type Conversion**: Handling different numeric inputs (float for base, integer for exponent).
3.  **Function Definition**: Encapsulating logic within reusable functions with clear parameters.
"""


def calculate_power(base, exponent):
    """Returns the result of base raised to the power of exponent."""
    # The ** operator is used for exponentiation in Python
    return base ** exponent

def main():
    # Prompt user for base and exponent
    base = float(input("Enter the base number: "))
    exponent = int(input("Enter the exponent (integer): "))
    
    # Calculate the result
    result = calculate_power(base, exponent)
    
    # Output the formatted result
    print(f"{base} raised to the power of {exponent} is: {result}")

# Standard Python idiom for running the main function
main()