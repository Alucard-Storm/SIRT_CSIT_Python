"""
Experiment 2: Lists, Tuples, and Dictionaries

This experiment explores Python's built-in collection data types, which are used to store multiple items in a single variable.
It covers:
1.  **Lists**: Ordered, mutable collections that allow duplicate elements.
2.  **Tuples**: Ordered, immutable collections (cannot be changed after creation).
3.  **Dictionaries**: Unordered (conceptually) collections of key-value pairs, where keys must be unique.
"""


def demonstrate_collections():
    # List: An ordered, mutable (changeable) collection of items
    print("=== List Operations ===")
    my_list = [1, 2, 3, 4, 5]
    print(f"Original list: {my_list}")
    
    # Adding an element to the end of the list
    my_list.append(6)
    print(f"After append: {my_list}")
    
    # Removing a specific element by value
    my_list.remove(3)
    print(f"After removing 3: {my_list}")
    
    # Tuple: An ordered, immutable (unchangeable) collection
    print("\n=== Tuple Operations ===")
    my_tuple = (1, 2, 3, "hello", 5.5)
    print(f"Tuple: {my_tuple}")
    # Tuples are often used for fixed data that shouldn't change
    print(f"Tuple length: {len(my_tuple)}")
    print(f"First element: {my_tuple[0]}")
    
    # Dictionary: A collection of key-value pairs (unordered in older versions, ordered since 3.7)
    print("\n=== Dictionary Operations ===")
    my_dict = {
        "name": "John",
        "age": 30,
        "city": "New York"
    }
    print(f"Dictionary: {my_dict}")
    
    # Adding a new key-value pair
    my_dict["occupation"] = "Developer"
    print(f"After adding new key: {my_dict}")
    
    # Accessing values using their keys
    print(f"Name extracted from dictionary: {my_dict['name']}")

# Execute the demonstration
demonstrate_collections()