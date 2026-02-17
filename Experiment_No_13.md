# Experiment No 13

## Aim

Functional Polymorphism (Case Study: Restaurant Order System)

## Objective

Achieve polymorphism using default arguments to handle flexible customer orders in a restaurant system.

## Process Flow

1. **Define Function:** Create a function `take_order` that accepts `item_name` (mandatory), `quantity` (default=1), and `customization` (default=None).
2. **Handle Defaults:**
    * If only `item_name` is provided, assume quantity is 1 and no customization.
    * If `quantity` is provided, update the count.
    * If `customization` is provided, add the special note.
3. **Simulate Orders:** Call the function with different combinations of arguments to simulate various customer scenarios.

## Code

```python
def take_order(item_name, quantity=1, customization=None):
    """
    Simulates taking a restaurant order with varying levels of detail.
    """
    order_summary = f"Order: {quantity} x {item_name}"
    
    if customization:
        order_summary += f" [Note: {customization}]"
    
    return order_summary

# Case Study: Restaurant Order Processing
print("--- Kitchen Ticket System ---")

# Scenario 1: Quick coffee order (Defaults used)
print(take_order("Cappuccino"))

# Scenario 2: Ordering specifically 2 burgers (Quantity specified)
print(take_order("Cheeseburger", 2))

# Scenario 3: Specific pizza order (All arguments specified)
print(take_order("Margherita Pizza", 1, "Extra Cheese & Basil"))

# Scenario 4: Large custom order
print(take_order("Pasta Alfredo", 3, "No Parsley"))
```

---

## Output

```bash
--- Kitchen Ticket System ---
Order: 1 x Cappuccino
Order: 2 x Cheeseburger
Order: 1 x Margherita Pizza [Note: Extra Cheese & Basil]
Order: 3 x Pasta Alfredo [Note: No Parsley]
```
