"""
Experiment 2: Lists, Tuples, and Dictionaries

This experiment explores Python's built-in collection data types, which are used to store multiple items in a single variable.
It covers:
1.  **Lists**: Ordered, mutable collections that allow duplicate elements.
2.  **Tuples**: Ordered, immutable collections (cannot be changed after creation).
3.  **Dictionaries**: Unordered (conceptually) collections of key-value pairs, where keys must be unique.
"""


# List: Ordered, mutable (changeable) collection
print("=== List Operations ===")
my_list = [1, 2, 3, 4, 5]
print(f"Original list: {my_list}")

# Add element to list
my_list.append(6)
print(f"After append: {my_list}")

# Remove element from list
my_list.remove(3)
print(f"After removing 3: {my_list}")

# Tuple: Ordered, immutable (unchangeable) collection
print("\n=== Tuple Operations ===")
my_tuple = (1, 2, 3, "hello", 5.5)
print(f"Tuple: {my_tuple}")
print(f"Length: {len(my_tuple)}")
print(f"First element: {my_tuple[0]}")

# Dictionary: Collection of key-value pairs
print("\n=== Dictionary Operations ===")
my_dict = {
    "name": "John",
    "age": 30,
    "city": "New York"
}
print(f"Dictionary: {my_dict}")

# Add new key-value pair
my_dict["job"] = "Developer"
print(f"After adding new key: {my_dict}")

# Access value by key
print(f"Name: {my_dict['name']}")