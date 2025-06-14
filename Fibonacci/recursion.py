fibonacci_numbers = [0,1]

def generate_fibonacci_numbers(x:int, y: int ):
    """
    This function takes in the previous two fibonnaci numbers and generates a new one recursively
    """
    if len(fibonacci_numbers) < 18:    
        fibonacci_numbers.append(x+y)
        generate_fibonacci_numbers(y,fibonacci_numbers[-1])

generate_fibonacci_numbers(fibonacci_numbers[0],fibonacci_numbers[1])
print(fibonacci_numbers)