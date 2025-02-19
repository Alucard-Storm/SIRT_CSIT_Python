# Experiment 3: Mean, Median, and Mode

from collections import Counter

def calculate_statistics(numbers):
    # Mean calculation
    mean_value = sum(numbers) / len(numbers)
    
    # Median calculation
    sorted_numbers = sorted(numbers)
    n = len(numbers)
    if n % 2 == 0:
        median_value = (sorted_numbers[n//2 - 1] + sorted_numbers[n//2]) / 2
    else:
        median_value = sorted_numbers[n//2]
    
    # Mode calculation
    counter = Counter(numbers)
    mode_value = counter.most_common(1)[0][0]
    
    return mean_value, median_value, mode_value

def main():
    numbers = [4, 2, 7, 2, 9, 4, 5, 4, 8, 2]
    mean_val, median_val, mode_val = calculate_statistics(numbers)
    
    print(f"Numbers: {numbers}")
    print(f"Mean: {mean_val}")
    print(f"Median: {median_val}")
    print(f"Mode: {mode_val}")

main() 