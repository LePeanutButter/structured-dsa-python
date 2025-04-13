"""
even_sum_recursive.py
---------------------
This module implements a recursive function to compute the sum of all positive even integers
from a given number N down to 2. The algorithm handles cases where N is even or odd by adjusting
the input appropriately, and relies on two base cases:
  - When N equals 0, the sum is 0.
  - When N equals 2, the sum is 2.
  
For odd values of N, the function decrements by 1 to convert it to an even number before proceeding.
For even values greater than 2, the function adds N to the sum of even numbers from N-2 down to 2.
  
Usage:
    The program reads an integer N from standard input and computes the sum of even integers
    from N down to 2 using recursion.
"""

# Read input number from the user
n = int(input("n="))

def suma(n):
    """
    Recursively computes the sum of even positive integers from n down to 2.
    
    If n is 2, returns 2 (base case). If n is 0, returns 0.
    If n is odd, it is decremented by 1 to become even before computing the sum.
    If n is even and greater than 2, the function returns n plus the sum of even numbers
    from n-2 down to 2.
    
    Args:
        n (int): The starting positive integer.
    
    Returns:
        int: The sum of all even integers from the adjusted value of n down to 2.
    """
    elite = 0
    if n == 2:
        elite = 2 + elite
        return elite
    elif n == 0:
        return elite
    elif n % 2 != 0:
        elite = suma(n - 1)
        return elite
    elif n % 2 == 0:
        elite = n + suma(n - 2)
        return elite

# Compute and print the sum of even positive integers from n down to 2
print(suma(n))
