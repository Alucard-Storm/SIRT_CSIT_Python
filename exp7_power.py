# Experiment 7: Exponentiation

def calculate_power(base, exponent):
    return base ** exponent

def main():
    try:
        base = float(input("Enter the base number: "))
        exponent = int(input("Enter the exponent: "))
        
        # Using built-in operator
        result = calculate_power(base, exponent)
        
        print(f"{base} raised to power {exponent} = {result}")
    
    except ValueError:
        print("Please enter valid numbers")

main() 