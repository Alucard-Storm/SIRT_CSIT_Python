"""
Experiment 5: Checking for Even and Odd Numbers

This experiment demonstrates basic conditional logic and the modulo operator.
It covers:
1.  **Modulo Operator (%)**: Used to find the remainder of a division operation.
2.  **Even Numbers**: Numbers divisible by 2 (remainder is 0).
3.  **Odd Numbers**: Numbers not divisible by 2 (remainder is not 0).
4.  **Conditional Statements**: Using `if-else` blocks to handle different logic paths.
"""


# Get input from user
number = int(input("Enter a number to check: "))

# Check if number is even or odd using modulo operator
if number % 2 == 0:
    print(f"{number} is an even number.")
else:
    print(f"{number} is an odd number.")