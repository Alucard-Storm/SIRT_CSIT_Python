# Experiment No 15

## Aim

Case Study: Mathematical Utility Toolkit

## Objective

Develop a unified program combining various mathematical operations (Prime, Fibonacci, Factorial, Power) into a functional utility.

## Process Flow

1. **Define Helper Functions:**
    * `is_prime(n)`: Returns True if n is prime.
    * `factorial(n)`: Returns factorial of n.
    * `fibonacci(n)`: Returns Fibonacci series up to n terms.
    * `power(base, exp)`: Calculates base raised to exponent.
2. **Main Interface:** Create a menu to allow users to select an operation repeatedly.

## Code

```python
def is_prime(n):
    if n < 2: return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0: return False
    return True

def factorial(n):
    if n == 0 or n == 1: return 1
    return n * factorial(n - 1)

def fibonacci(n):
    series = [0, 1]
    while len(series) < n:
        series.append(series[-1] + series[-2])
    return series[:n]

def power(base, exp):
    return base ** exp

while True:
    print("\n--- Math Toolkit ---")
    print("1. Check Prime")
    print("2. Calculate Factorial")
    print("3. Generate Fibonacci Series")
    print("4. Calculate Power")
    print("5. Exit")
    
    choice = input("Select Operation: ")
    
    if choice == '1':
        num = int(input("Enter number: "))
        print(f"{num} is {'Prime' if is_prime(num) else 'Not Prime'}")
    elif choice == '2':
        num = int(input("Enter number: "))
        print(f"Factorial of {num} is {factorial(num)}")
    elif choice == '3':
        num = int(input("Enter number of terms: "))
        print(f"Fibonacci Series: {fibonacci(num)}")
    elif choice == '4':
        b = float(input("Enter base: "))
        e = float(input("Enter exponent: "))
        print(f"Result: {power(b, e)}")
    elif choice == '5':
        print("Goodbye!")
        break
    else:
        print("Invalid selection.")
```

---

## Output

```bash
--- Math Toolkit ---
1. Check Prime
2. Calculate Factorial
3. Generate Fibonacci Series
4. Calculate Power
5. Exit
Select Operation: 1
Enter number: 17
17 is Prime

Select Operation: 3
Enter number of terms: 6
Fibonacci Series: [0, 1, 1, 2, 3, 5]

Select Operation: 5
Goodbye!
```
