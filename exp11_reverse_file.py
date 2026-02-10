"""
Experiment 11: File Reading and Reversing Line Order

This experiment demonstrates File Input/Output (I/O) operations and string manipulation.
It covers:
1.  **File Handling**: safely opening and reading files using the `with` statement.
2.  **Reading Data**: Using `readlines()` to capture file content into a list.
3.  **Data Processing**: Iterating through the list of lines in reverse order using `reversed()`.
4.  **Error Handling**: Managing missing files and other exceptions using `try-except` blocks.
"""


# Get filename from user
filename = input("Enter the filename (e.g., sample.txt): ")

try:
    # Open and read file
    with open(filename, 'r') as file:
        lines = file.readlines()
    
    # Display original content
    print(f"\n--- Original content of '{filename}' ---")
    for line in lines:
        print(line.strip())
    
    # Display reversed content
    print(f"\n--- Content in Reversed Order ---")
    for line in reversed(lines):
        print(line.strip())
        
except FileNotFoundError:
    print(f"Error: File '{filename}' not found.")
except Exception as e:
    print(f"Error: {e}")