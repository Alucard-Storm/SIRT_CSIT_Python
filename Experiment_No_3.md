# Experiment No 3

## Aim

Even or Odd Number Checker

## Objective

Use conditional statements (`if–else`) to check whether a number is even or odd.

## Process Flow

1. Read an integer input from the user.
2. Use the modulo operator `%` to check if the number is divisible by 2.
3. If the remainder is 0, print 'Even'.
4. Otherwise, print 'Odd'.

## Code

```python
num = int(input("Enter a number: "))
if num % 2 == 0:
    print(f"{num} is Even")
else:
    print(f"{num} is Odd")
```

---

## Output

```bash
Enter a number: 4
4 is Even
```
