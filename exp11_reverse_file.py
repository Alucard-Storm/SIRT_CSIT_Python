"""
Experiment 11: File Reading and Reversing Line Order

This experiment demonstrates File Input/Output (I/O) operations and string manipulation.
It covers:
1.  **File Handling**: safely opening and reading files using the `with` statement.
2.  **Reading Data**: Using `readlines()` to capture file content into a list.
3.  **Data Processing**: Iterating through the list of lines in reverse order using `reversed()`.
4.  **Error Handling**: Managing missing files and other exceptions using `try-except` blocks.
"""


def reverse_file_lines(filename):
    """Reads lines from a file and prints them in original and reversed order."""
    try:
        # 'with' statement ensures the file is automatically closed
        with open(filename, 'r') as file:
            # readlines() returns a list of all lines in the file
            lines = file.readlines()
        
        if not lines:
            print(f"The file '{filename}' is empty.")
            return

        print(f"--- Original content of '{filename}' ---")
        for line in lines:
            # strip() removes leading/trailing whitespace including newlines
            print(line.strip())
        
        print(f"\n--- Content in Reversed Order ---")
        # reversed() returns an iterator that traverses the list backwards
        for line in reversed(lines):
            print(line.strip())
            
    except FileNotFoundError:
        print(f"Error: The file '{filename}' was not found.")
    except Exception as e:
        print(f"An unexpected error occurred: {str(e)}")

def main():
    # Prompt user for the file to process
    filename = input("Enter the filename (e.g., sample.txt): ")
    reverse_file_lines(filename)

# Entry point
main()