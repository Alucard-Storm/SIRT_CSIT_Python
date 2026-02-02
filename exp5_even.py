# Experiment 5: Checking for Even and Odd Numbers

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
if __name__ == "__main__":
    main()