# Experiment 2: Lists, Tuples, and Dictionaries

def demonstrate_collections():
    # List demonstration
    print("=== List Operations ===")
    my_list = [1, 2, 3, 4, 5]
    print(f"Original list: {my_list}")
    my_list.append(6)
    print(f"After append: {my_list}")
    my_list.remove(3)
    print(f"After removing 3: {my_list}")
    
    # Tuple demonstration
    print("\n=== Tuple Operations ===")
    my_tuple = (1, 2, 3, "hello", 5.5)
    print(f"Tuple: {my_tuple}")
    print(f"Tuple length: {len(my_tuple)}")
    print(f"First element: {my_tuple[0]}")
    
    # Dictionary demonstration
    print("\n=== Dictionary Operations ===")
    my_dict = {
        "name": "John",
        "age": 30,
        "city": "New York"
    }
    print(f"Dictionary: {my_dict}")
    my_dict["occupation"] = "Developer"
    print(f"After adding new key: {my_dict}")
    print(f"Name: {my_dict['name']}")

demonstrate_collections() 