# Experiment 5: Check Even Number

def is_even(number):
    return number % 2 == 0

def main():
    try:
        number = int(input("Enter a number to check if it's even: "))
        if is_even(number):
            print(f"{number} is even")
        else:
            print(f"{number} is odd")
    except ValueError:
        print("Please enter a valid integer")

if __name__ == "__main__":
    main() 