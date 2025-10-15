# Import random module to generate random numbers
import random

# Create a list of 100 random numbers from 0 to 1000
numbers = [random.randint(0, 1000) for _ in range(100)]

# Sort the list manually (without using sort() or sorted())
# Using simple bubble sort algorithm
for i in range(len(numbers)):
    for j in range(0, len(numbers) - i - 1):
        if numbers[j] > numbers[j + 1]:
            # Swap if the current element is greater than the next one
            numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]

# Separate even and odd numbers into two lists
even_numbers = [num for num in numbers if num % 2 == 0]
odd_numbers = [num for num in numbers if num % 2 != 0]

# Calculate the average for even numbers
average_even = sum(even_numbers) / len(even_numbers) if even_numbers else 0

# Calculate the average for odd numbers
average_odd = sum(odd_numbers) / len(odd_numbers) if odd_numbers else 0

# Print both averages in the console
print("Average of even numbers:", average_even)
print("Average of odd numbers:", average_odd)
