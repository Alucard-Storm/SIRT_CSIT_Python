"""
Experiment 4: Generating the First N Prime Numbers

This experiment focuses on algorithm implementation for prime number generation.
It covers:
1.  **Prime Number**: A natural number greater than 1 that has no positive divisors other than 1 and itself.
2.  **Validation Function**: Implementing `is_prime(n)` to check for primality logic efficiently.
3.  **Loop Control**: Using a while loop to generate a specific count (N) of prime numbers.
"""


# Function to check if a number is prime
def is_prime(num):
    # Numbers less than 2 are not prime
    if num < 2:
        return False
    # Check if any number divides evenly
    for i in range(2, num):
        if num % i == 0:
            return False
    return True

# Get user input
n = int(input("Enter how many prime numbers you want: "))

if n <= 0:
    print("Please enter a positive number.")
else:
    # Generate first n prime numbers
    primes = []
    number = 2
    
    while len(primes) < n:
        if is_prime(number):
            primes.append(number)
        number += 1
    
    print(f"First {n} prime numbers are: {primes}")