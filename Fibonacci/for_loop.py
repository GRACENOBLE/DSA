"""
This uses a for loop to generate the fibonacci sequence.
"""

fibonacci_numbers=[0,1]

for _ in range(2,18):
    fibonacci_numbers.append(fibonacci_numbers[len(fibonacci_numbers)-2]+fibonacci_numbers[len(fibonacci_numbers)-1])

print(fibonacci_numbers)