# Experiment No 15

## Aim
Case Study: Mathematical Utility Application

## Objective
A unified program combining prime, Fibonacci, power, and statistical operations.

## Process Flow
1. Define helper functions for operations.
2. Create a main loop displaying a menu.
3. Call appropriate functions based on user choice.
4. Exit on command.

## Code
```python
def check_even(n):
    return "Even" if n % 2 == 0 else "Odd"

def power(base, exp):
    return base ** exp

while True:
    print("\nMathematical Utility\n1. Check Even/Odd\n2. Power\n3. Exit")
    choice = input("Enter choice: ")
    
    if choice == '1':
        num = int(input("Enter number: "))
        print(check_even(num))
    elif choice == '2':
        b = float(input("Enter base: "))
        e = float(input("Enter exponent: "))
        print(power(b, e))
    elif choice == '3':
        break
    else:
        print("Invalid choice")
```
---

## Outcome

```bash
Mathematical Utility
1. Check Even/Odd
2. Power
3. Exit
Enter choice: 1
Enter number: 4
Even

Mathematical Utility
1. Check Even/Odd
2. Power
3. Exit
Enter choice: 3
```
