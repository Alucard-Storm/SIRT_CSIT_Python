# Experiment No 14

## Aim
Case Study: Student Record Management System

## Objective
Menu-driven program using functions, lists/dictionaries, and basic validation.

## Process Flow
1. Initialize an empty dictionary to store student records.
2. Display a menu loop.
3. If choice is 1, prompt for name and score, and add to dictionary.
4. If choice is 2, print the dictionary.
5. If choice is 3, break the loop.

## Code
```python
students = {}

while True:
    print("\n1. Add Student\n2. View Students\n3. Exit")
    choice = input("Enter choice: ")
    
    if choice == '1':
        name = input("Enter Name: ")
        score = input("Enter Score: ")
        students[name] = score
        print("Student added.")
    elif choice == '2':
        print(students)
    elif choice == '3':
        break
    else:
        print("Invalid choice!")
```
---

## Outcome

```bash
1. Add Student
2. View Students
3. Exit
Enter choice: 1
Enter Name: John
Enter Score: 90
Student added.

1. Add Student
2. View Students
3. Exit
Enter choice: 2
{'John': '90'}

1. Add Student
2. View Students
3. Exit
Enter choice: 3
```
