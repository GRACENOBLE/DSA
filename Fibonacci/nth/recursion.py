def fibonacci_number(n: int) -> int:
    """
    Returns the nth fibonacci number by recursion
    """
   
    if n <= 1 :
        return n
    else:
        return fibonacci_number(n-1) + fibonacci_number(n-2)
    
print(fibonacci_number(5))
# end def