# Experiment No 5

## Aim

Exponentiation (Power of a Number)

## Objective

Calculate the power of a number using operators and built-in functions.

## Process Flow

1. Read the base and exponent values from the user.
2. Calculate the power using the `**` operator or `pow()` function.
3. Display the result.

## Code

```python
base = float(input("Enter base: "))
exp = float(input("Enter exponent: "))
result = base ** exp
print(f"{base} raised to {exp} is {result}")
```

---

## Output

```bash
Enter base: 2
Enter exponent: 3
2.0 raised to 3.0 is 8.0
```
