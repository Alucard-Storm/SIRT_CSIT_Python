"""
Experiment 3: Mean, Median, and Mode Calculation

This experiment demonstrates how to calculate basic statistical measures for a dataset.
It covers:
1.  **Mean**: The arithmetic average of a dataset (Sum of elements / Count of elements).
2.  **Median**: The middle value separating the higher half from the lower half of a data sample.
3.  **Mode**: The value that appears most frequently in the data set.
"""


from collections import Counter

def calculate_statistics(numbers):
    # Mean: The average of all numbers (Sum / Count)
    mean_value = sum(numbers) / len(numbers)
    
    # Median: The middle value in a sorted list
    sorted_numbers = sorted(numbers)
    n = len(numbers)
    if n % 2 == 0:
        # If even number of elements, median is average of two middle elements
        median_value = (sorted_numbers[n//2 - 1] + sorted_numbers[n//2]) / 2
    else:
        # If odd, median is the central element
        median_value = sorted_numbers[n//2]
    
    # Mode: The value that appears most frequently
    counter = Counter(numbers)
    # most_common(1) returns a list like [(value, count)], so we take [0][0]
    mode_value = counter.most_common(1)[0][0]
    
    return mean_value, median_value, mode_value

def main():
    # Sample dataset
    numbers = [4, 2, 7, 2, 9, 4, 5, 4, 8, 2]
    
    # Unpacking the returned statistics
    mean_val, median_val, mode_val = calculate_statistics(numbers)
    
    print(f"Data set: {numbers}")
    print(f"Arithmetic Mean: {mean_val}")
    print(f"Median Value: {median_val}")
    print(f"Statistical Mode: {mode_val}")

# Entry point
main()