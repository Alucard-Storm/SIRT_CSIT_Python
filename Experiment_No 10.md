# Experiment No 10

## Aim
File Handling: Reverse Each Line of a File

## Objective
Read a text file and print each line in reverse order.

## Process Flow
1. Create/Identify a text file named `@sample.txt`.
2. Open the file in read mode.
3. Iterate through each line.
4. Remove trailing newline using `.strip()`.
5. Reverse the string using slicing `[::-1]`.
6. Print the reversed line.

## Code
```python
# Using @sample.txt
filename = "sample.txt"
try:
    with open(filename, 'r') as file:
        for line in file:
            # We strip the newline character before reversing
            print(line.strip()[::-1])
except FileNotFoundError:
    print(f"{filename} not found.")
```
---

## Outcome

```bash
reif eht fo enil tsriF
reif eht fo enil dnoceS
reif eht fo enil drihT
reif eht fo enil htruoF
 elif eht fo enil htfiF
```
