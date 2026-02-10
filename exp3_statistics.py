"""
Experiment 3: Mean, Median, and Mode Calculation

This experiment demonstrates how to calculate basic statistical measures for a dataset.
It covers:
1.  **Mean**: The arithmetic average of a dataset (Sum of elements / Count of elements).
2.  **Median**: The middle value separating the higher half from the lower half of a data sample.
3.  **Mode**: The value that appears most frequently in the data set.
"""


# Sample dataset
numbers = [4, 2, 7, 2, 9, 4, 5, 4, 8, 2]

print(f"Data set: {numbers}")

# Calculate Mean (average)
mean = sum(numbers) / len(numbers)
print(f"Mean: {mean}")

# Calculate Median (middle value when sorted)
sorted_numbers = sorted(numbers)
n = len(numbers)
if n % 2 == 0:
    # If even number of elements, median is average of two middle values
    median = (sorted_numbers[n//2 - 1] + sorted_numbers[n//2]) / 2
else:
    # If odd, median is the middle element
    median = sorted_numbers[n//2]
print(f"Median: {median}")

# Calculate Mode (most frequent value)
mode_value = None
max_count = 0
for num in set(numbers):
    count = numbers.count(num)
    if count > max_count:
        max_count = count
        mode_value = num
print(f"Mode: {mode_value}")