# Experiment 8: Fibonacci Series

def fibonacci(n):
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    
    fib = [0, 1]
    for i in range(2, n):
        fib.append(fib[i-1] + fib[i-2])
    return fib

def main():
    try:
        n = int(input("Enter the number of Fibonacci terms to generate: "))
        
        # Using iterative method
        fib_series = fibonacci(n)
        print(f"Fibonacci series : {fib_series}")
            
    except ValueError:
        print("Please enter a valid integer")

main() 