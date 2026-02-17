# Experiment No 8

## Aim

First n Prime Numbers

## Objective

Write a program to find the first `n` prime numbers using nested loops.

## Process Flow

1. Read `n` from the user.
2. Initialize a counter and a number variable.
3. Use a while loop to find `n` primes.
4. Inside, use a for loop to check if the current number is prime.
5. If prime, print it and increment the counter.

## Code

```python
n = int(input("Enter value of n: "))
count = 0
num = 2
print(f"First {n} prime numbers:")
while count < n:
    is_prime = True
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            is_prime = False
            break
    if is_prime:
        print(num, end=" ")
        count += 1
    num += 1
print()
```

---

## Output

```bash
Enter value of n: 5
First 5 prime numbers:
2 3 5 7 11 
```
