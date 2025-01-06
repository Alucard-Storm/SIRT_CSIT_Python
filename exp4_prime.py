# Experiment 4: First N Prime Numbers

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def get_n_primes(n):
    primes = []
    num = 2
    while len(primes) < n:
        if is_prime(num):
            primes.append(num)
        num += 1
    return primes

def main():
    n = int(input("Enter how many prime numbers you want: "))
    prime_numbers = get_n_primes(n)
    print(f"First {n} prime numbers are: {prime_numbers}")

if __name__ == "__main__":
    main() 