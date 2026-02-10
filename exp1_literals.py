"""
Experiment 1: Literals, Constants, Data Types, and I/O

This experiment demonstrates the fundamental building blocks of Python programming.
It covers:
1.  **Literals**: Fixed values like integers, floating-point numbers, strings, and booleans.
2.  **Constants**: Variables whose values are intended to remain unchanged (conventionally named in UPPERCASE).
3.  **Data Types**: The classification of data items (int, float, str, bool, complex, list).
4.  **Input/Output (I/O)**: Using `input()` to receive user data and `print()` to display results.
"""


# Constants (variables in UPPERCASE that don't change)
PI = 3.14159

# Different types of literals
integer_num = 42
float_num = 3.14
string_text = "Hello, Python!"
boolean_val = True
list_example = [1, 2, 3, 4, 5]

# Main program
print("=== Data Types and I/O Demo ===")

# Take input from user
name = input("Enter your name: ")
age = int(input("Enter your age: "))

# Display output
print(f"\nName (string): {name}")
print(f"Age (integer): {age}")
print(f"PI (float): {PI}")
print(f"Boolean value: {boolean_val}")
print(f"List: {list_example}")