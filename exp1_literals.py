# Experiment 1: Literals, Constants, Data Types, and I/O

# Constants
PI = 3.14159
MAX_VALUE = 100

# Different types of literals and data types
integer_num = 42
float_num = 3.14
string_text = "Hello, Python!"
boolean_val = True
complex_num = 3 + 4j
list_example = [1, 2, 3, 4, 5]

def main():
    # Input/Output demonstration
    print("=== Data Types and I/O Demo ===")
    
    # Input
    name = input("Enter your name: ")
    age = int(input("Enter your age: "))
    
    # Output with different data types
    print(f"\nName (string): {name}")
    print(f"Age (integer): {age}")
    print(f"PI (float constant): {PI}")
    print(f"Complex number: {complex_num}")
    print(f"Boolean value: {boolean_val}")
    print(f"List: {list_example}")

if __name__ == "__main__":
    main() 