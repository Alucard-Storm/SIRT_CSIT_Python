# Experiment 8: Fibonacci Series

def fibonacci_iterative(n):
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    
    fib = [0, 1]
    for i in range(2, n):
        fib.append(fib[i-1] + fib[i-2])
    return fib

def fibonacci_recursive(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci_recursive(n-1) + fibonacci_recursive(n-2)

def main():
    try:
        n = int(input("Enter the number of Fibonacci terms to generate: "))
        
        # Using iterative method
        fib_series = fibonacci_iterative(n)
        print(f"Fibonacci series (iterative): {fib_series}")
        
        # Using recursive method
        print("Fibonacci series (recursive):", end=" ")
        for i in range(n):
            print(fibonacci_recursive(i), end=" ")
        print()
    
    except ValueError:
        print("Please enter a valid integer")

if __name__ == "__main__":
    main() 