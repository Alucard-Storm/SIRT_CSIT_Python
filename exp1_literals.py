# Experiment 1: Literals, Constants, Data Types, and I/O

# Defining Constants (conventionally written in UPPERCASE)
PI = 3.14159
MAX_VALUE = 100

# Demonstrating different types of literals and their corresponding data types
integer_num = 42         # Integer literal
float_num = 3.14          # Floating point literal
string_text = "Hello, Python!"  # String literal
boolean_val = True        # Boolean literal
complex_num = 3 + 4j      # Complex number literal (a + bj)
list_example = [1, 2, 3, 4, 5]  # List literal (mutable collection)

def main():
    # Input and Output demonstration
    print("=== Data Types and I/O Demo ===")
    
    # Taking input from the user (input() always returns a string)
    name = input("Enter your name: ")
    # Converting the input string to an integer
    age = int(input("Enter your age: "))
    
    # Displaying output using f-strings for formatting
    print(f"\nName (string): {name}")
    print(f"Age (integer): {age}")
    print(f"PI (float constant): {PI}")
    print(f"Complex number: {complex_num}")
    print(f"Boolean value: {boolean_val}")
    print(f"List: {list_example}")

# Entry point of the script
if __name__ == "__main__":
    main()