"""
Experiment 5: Checking for Even and Odd Numbers

This experiment demonstrates basic conditional logic and the modulo operator.
It covers:
1.  **Modulo Operator (%)**: Used to find the remainder of a division operation.
2.  **Even Numbers**: Numbers divisible by 2 (remainder is 0).
3.  **Odd Numbers**: Numbers not divisible by 2 (remainder is not 0).
4.  **Conditional Statements**: Using `if-else` blocks to handle different logic paths.
"""


def is_even(number):
    """Returns True if the number is even, False otherwise."""
    # Modulo operator % returns the remainder of division
    return number % 2 == 0

def main():
    try:
        # Prompt user for input
        number = int(input("Enter a number to check if it's even: "))
        
        # Decision logic using the is_even function
        if is_even(number):
            print(f"{number} is an even number.")
        else:
            print(f"{number} is an odd number.")
            
    except ValueError:
        # Handle cases where input is not a valid integer
        print("Error: Please enter a valid integer.")

# Execution starts here
main()