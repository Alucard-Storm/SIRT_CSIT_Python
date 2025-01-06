# Experiment 7: Exponentiation

def calculate_power(base, exponent):
    return base ** exponent

def calculate_power_recursive(base, exponent):
    if exponent == 0:
        return 1
    elif exponent < 0:
        return 1 / calculate_power_recursive(base, -exponent)
    elif exponent % 2 == 0:
        temp = calculate_power_recursive(base, exponent//2)
        return temp * temp
    else:
        return base * calculate_power_recursive(base, exponent-1)

def main():
    try:
        base = float(input("Enter the base number: "))
        exponent = int(input("Enter the exponent: "))
        
        # Using built-in operator
        result1 = calculate_power(base, exponent)
        # Using recursive method
        result2 = calculate_power_recursive(base, exponent)
        
        print(f"{base} raised to power {exponent} = {result1}")
        print(f"Using recursive method: {result2}")
    
    except ValueError:
        print("Please enter valid numbers")

if __name__ == "__main__":
    main() 