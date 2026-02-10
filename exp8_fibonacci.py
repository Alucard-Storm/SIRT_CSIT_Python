"""
Experiment 8: Generating Fibonacci Series up to N terms

This experiment focuses on sequence generation and iterative logic.
It covers:
1.  **Fibonacci Sequence**: A series where each number is the sum of the two preceding ones (usually starting with 0 and 1).
2.  **Iterative Approach**: Using loops to generate terms dynamically based on user input.
3.  **List Manipulation**: Using `append()` to build the sequence incrementally.
"""


# Get number of terms from user
n = int(input("Enter the number of Fibonacci terms to generate: "))

if n <= 0:
    print("Please enter a positive number.")
elif n == 1:
    print("Fibonacci series (1 terms): [0]")
else:
    # Initialize the series with first two terms
    fib = [0, 1]
    
    # Generate remaining terms
    for i in range(2, n):
        next_term = fib[i-1] + fib[i-2]
        fib.append(next_term)
    
    print(f"Fibonacci series ({n} terms): {fib}")