# Experiment No 2

## Aim

Literals, Constants, Data Types & I/O Program

## Objective

Demonstrate numeric, string, and boolean data types with user input and formatted output.

## Process Flow

1. Define variables of different data types: int, float, str, bool.
2. Use `input()` function to take input from the user.
3. Use `print()` function with f-strings to display the value and type of each variable.

## Code

```python
num = 10
pi = 3.14
name = "Python"
is_fun = True

user_input = input("Enter something: ")
print(f"Integer: {num}, Type: {type(num)}")
print(f"Float: {pi}, Type: {type(pi)}")
print(f"String: {name}, Type: {type(name)}")
print(f"Boolean: {is_fun}, Type: {type(is_fun)}")
print(f"You entered: {user_input}")
```

---

## Output

```bash
Integer: 10, Type: <class 'int'>
Float: 3.14, Type: <class 'float'>
String: Python, Type: <class 'str'>
Boolean: True, Type: <class 'bool'>
You entered: Sample Input
```
