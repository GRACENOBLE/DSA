numbers = [7, 12, 9, 4, 11]

current_number = numbers[0]
for number in numbers:
    if number < current_number:
        current_number = number

print(f"The smallest number is {current_number}")
