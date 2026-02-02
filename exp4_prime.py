"""
Experiment 4: Generating the First N Prime Numbers

This experiment focuses on algorithm implementation for prime number generation.
It covers:
1.  **Prime Number**: A natural number greater than 1 that has no positive divisors other than 1 and itself.
2.  **Validation Function**: Implementing `is_prime(n)` to check for primality logic efficiently.
3.  **Loop Control**: Using a while loop to generate a specific count (N) of prime numbers.
"""


def is_prime(n):
    """Checks if a number is prime."""
    # Numbers less than 2 are not prime
    if n < 2:
        return False
    # Check for factors from 2 up to the square root of n
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def get_n_primes(n):
    """Generates a list containing the first n prime numbers."""
    primes = []
    num = 2  # Start checking from 2
    while len(primes) < n:
        if is_prime(num):
            primes.append(num)
        num += 1
    return primes

def main():
    # User input for the number of primes needed
    try:
        n = int(input("Enter how many prime numbers you want: "))
        if n <= 0:
            print("Please enter a positive integer.")
            return
            
        prime_numbers = get_n_primes(n)
        print(f"First {n} prime numbers are: {prime_numbers}")
    except ValueError:
        print("Invalid input. Please enter a valid integer.")

# Script entry point
main()