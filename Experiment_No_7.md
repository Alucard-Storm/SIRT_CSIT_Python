# Experiment No 7

## Aim

Fibonacci Series Using Loops

## Objective

Generate Fibonacci series using iterative logic and control flow.

## Process Flow

1. Read the number of terms `n`.
2. Initialize two variables `a=0` and `b=1`.
3. Use a loop to print `a` and update `a` and `b` as `b` and `a+b` respectively.
4. Repeat `n` times.

## Code

```python
n = int(input("Enter number of terms: "))
a, b = 0, 1
print("Fibonacci Series:")
for _ in range(n):
    print(a, end=" ")
    a, b = b, a + b
print()
```

---

## Outcome

```bash
Enter number of terms: 5
Fibonacci Series:
0 1 1 2 3 
```
