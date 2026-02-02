# Experiment 8: Generating Fibonacci Series up to N terms

def fibonacci(n):
    """Generates the Fibonacci sequence up to n terms iteratively."""
    # Handle edge cases for non-positive input and single term
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    
    # Initialize the series with the first two terms
    fib = [0, 1]
    
    # Loop to generate subsequent terms by adding the last two
    for i in range(2, n):
        next_term = fib[i-1] + fib[i-2]
        fib.append(next_term)
        
    return fib

def main():
    try:
        # Ask user for the number of terms
        n = int(input("Enter the number of Fibonacci terms to generate: "))
        
        if n < 0:
            print("Please enter a non-negative integer.")
            return

        # Call the function and print the resulting list
        fib_series = fibonacci(n)
        print(f"Fibonacci series ({n} terms): {fib_series}")
            
    except ValueError:
        # Input validation
        print("Error: Please enter a valid integer.")

# Entry point of the script
if __name__ == "__main__":
    main()