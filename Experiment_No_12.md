# Experiment No 12

## Aim

Inheritance in Python (Case Study: Employee Management System)

## Objective

Demonstrate single or multilevel inheritance using classes and objects by modeling an Employee Management System.

## Process Flow

1. **Define Base Class:** Create an `Employee` class with attributes for `name`, `id`, and `base_salary`, and a method `calculate_salary()`.
2. **Define Derived Class:** Create a `Manager` class that inherits from `Employee`.
3. **Extend Functionality:** Add a `bonus` attribute to the `Manager` class.
4. **Override Method:** Override the `calculate_salary()` method in `Manager` to include the bonus.
5. **Demonstrate:** Create instances of `Employee` and `Manager`, and display their details and calculated salaries.

## Code

```python
class Employee:
    def __init__(self, name, emp_id, base_salary):
        self.name = name
        self.emp_id = emp_id
        self.base_salary = base_salary

    def display_info(self):
        print(f"Employee ID: {self.emp_id}")
        print(f"Name: {self.name}")

    def calculate_salary(self):
        return self.base_salary

class Manager(Employee):
    def __init__(self, name, emp_id, base_salary, bonus):
        # Initialize the base class
        super().__init__(name, emp_id, base_salary)
        self.bonus = bonus

    def calculate_salary(self):
        # Override to include bonus
        return self.base_salary + self.bonus

# Case Study: Payroll Processing
print("--- Payroll System ---")

# Regular Employee
emp1 = Employee("Alice", "E001", 50000)
emp1.display_info()
print(f"Total Salary: ${emp1.calculate_salary()}")
print("-" * 20)

# Manager
mgr1 = Manager("Bob", "M001", 80000, 15000)
mgr1.display_info()
print(f"Total Salary: ${mgr1.calculate_salary()}")
```

---

## Outcome

```bash
--- Payroll System ---
Employee ID: E001
Name: Alice
Total Salary: $50000
--------------------
Employee ID: M001
Name: Bob
Total Salary: $95000
```
