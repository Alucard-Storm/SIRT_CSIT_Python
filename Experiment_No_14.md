# Experiment No 14

## Aim

Case Study: Student Record Management System

## Objective

Develop a menu-driven program using list of dictionaries and functions to manage student records (Create, Read, Delete, Search).

## Process Flow

1. **Initialize:** Create a list `students` to store student records (dictionaries).
2. **Define Functions:**
    * `add_student(roll, name, marks)`: Adds a new record.
    * `view_students()`: Displays all records in a tabular format.
    * `search_student(roll)`: Finds and displays a student by Roll No.
    * `delete_student(roll)`: Removes a student by Roll No.
3. **Main Loop:** valid inputs and call respective functions until exit.

## Code

```python
students = []

def add_student(roll, name, marks):
    students.append({"roll": roll, "name": name, "marks": marks})
    print(f"Student {name} added successfully.")

def view_students():
    print("\n--- Student Records ---")
    print(f"{'Roll No':<10} {'Name':<20} {'Marks':<10}")
    print("-" * 40)
    for s in students:
        print(f"{s['roll']:<10} {s['name']:<20} {s['marks']:<10}")
    print("-" * 40)

def search_student(roll):
    for s in students:
        if s['roll'] == roll:
            return s
    return None

def delete_student(roll):
    global students
    original_len = len(students)
    students = [s for s in students if s['roll'] != roll]
    if len(students) < original_len:
        print(f"Student with Roll No {roll} deleted.")
    else:
        print("Student not found.")

# Simulation of User Interaction
while True:
    print("\n1. Add Student\n2. View Students\n3. Search Student\n4. Delete Student\n5. Exit")
    choice = input("Enter choice: ")

    if choice == '1':
        r = input("Enter Roll No: ")
        n = input("Enter Name: ")
        m = input("Enter Marks: ")
        add_student(r, n, m)
    elif choice == '2':
        view_students()
    elif choice == '3':
        r = input("Enter Roll No to search: ")
        s = search_student(r)
        if s:
            print(f"Found: {s}")
        else:
            print("Not Found.")
    elif choice == '4':
        r = input("Enter Roll No to delete: ")
        delete_student(r)
    elif choice == '5':
        print("Exiting...")
        break
    else:
        print("Invalid choice!")
```

---

## Outcome

```bash
1. Add Student
2. View Students
3. Search Student
4. Delete Student
5. Exit
Enter choice: 1
Enter Roll No: 101
Enter Name: Alice
Enter Marks: 85
Student Alice added successfully.

Enter choice: 2
--- Student Records ---
Roll No    Name                 Marks     
----------------------------------------
101        Alice                85        
----------------------------------------

Enter choice: 5
Exiting...
```
