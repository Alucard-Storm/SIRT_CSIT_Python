# Experiment No 12

## Aim
Inheritance in Python

## Objective
Demonstrate single or multilevel inheritance using classes and objects.

## Process Flow
1. Define a base class `Animal` with a method `speak`.
2. Define a derived class `Dog` that inherits from `Animal`.
3. Override the `speak` method in `Dog`.
4. Create instances and call the method.

## Code
```python
class Animal:
    def speak(self):
        print("Animal speaks")

class Dog(Animal):
    def speak(self):
        print("Dog barks")

a = Animal()
a.speak()

d = Dog()
d.speak()
```
---

## Outcome

```bash
Animal speaks
Dog barks
```
