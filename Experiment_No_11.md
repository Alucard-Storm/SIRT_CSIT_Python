# Experiment No 11

## Aim

Functions and Modular Programming (Case Study: Banking Transaction System)

## Objective

Define and call functions with arguments and return values to simulate a modular banking system.

## Process Flow

1. **Initialize State:** Create a variable `balance` to store the account funds (simulating a database).
2. **Define Functions:**
    * `check_balance()`: Returns the current balance.
    * `deposit(amount)`: Adds amount to balance and returns the new balance.
    * `withdraw(amount)`: Checks if funds are sufficient, then deducts amount or returns an error.
3. **Execute Transactions:** Call these functions in a sequence to simulate a user's session at an ATM.

## Code

```python
# Global variable to store account balance
balance = 0

def check_balance():
    """Returns the current account balance."""
    return balance

def deposit(amount):
    """Adds money to the account."""
    global balance
    if amount > 0:
        balance += amount
        print(f"Deposited: ${amount}")
    else:
        print("Invalid deposit amount")
    return balance

def withdraw(amount):
    """Withdraws money if sufficient funds exist."""
    global balance
    if 0 < amount <= balance:
        balance -= amount
        print(f"Withdrew: ${amount}")
    elif amount > balance:
        print(f"Failed Withdrawal: ${amount} (Insufficient Funds)")
    else:
        print("Invalid withdrawal amount")
    return balance

# Case Study: ATM Session
print("--- Banking System Simulation ---")

# 1. Initial Check
print(f"Current Balance: ${check_balance()}")

# 2. Deposit Salary
deposit(5000)
print(f"Balance after deposit: ${check_balance()}")

# 3. Withdraw Cash
withdraw(1200)

# 4. Attempt Overdraft
withdraw(10000)

# 5. Final Check
print(f"Final Balance: ${check_balance()}")
```

---

## Output

```bash
--- Banking System Simulation ---
Current Balance: $0
Deposited: $5000
Balance after deposit: $5000
Withdrew: $1200
Failed Withdrawal: $10000 (Insufficient Funds)
Final Balance: $3800
```
