# Experiment 11: Reverse File Lines

def reverse_file_lines(filename):
    try:
        # Read the file
        with open(filename, 'r') as file:
            lines = file.readlines()
        
        print("Original lines:")
        for line in lines:
            print(line.strip())
        
        print("\nReversed lines:")
        for line in reversed(lines):
            print(line.strip())
            
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found")
    except Exception as e:
        print(f"An error occurred: {str(e)}")

def main():
    filename = input("Enter the filename to read: ")
    reverse_file_lines(filename)

main() 