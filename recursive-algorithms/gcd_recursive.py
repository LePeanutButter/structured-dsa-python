"""
gcd_recursive.py
----------------
This module implements a recursive function to compute the Greatest Common Divisor (GCD)
of two positive integers using Euclid's algorithm.

The function `mcd` takes two integers `m` and `n` as inputs and recursively returns 
their GCD by applying the Euclidean method. The program prompts the user for two positive integers,
ensuring valid input (non-negative integers), and then outputs the computed GCD.

Usage:
    This program reads two positive integers from the console and prints the GCD.
"""

def mcd(m, n):
    """
    Recursively computes the Greatest Common Divisor (GCD) of two non-negative integers using the Euclidean algorithm.

    Args:
        m (int): The first non-negative integer.
        n (int): The second non-negative integer.

    Returns:
        int: The greatest common divisor of m and n.

    Strategy:
        - Base case: if n equals 0, return m.
        - Recursive case: otherwise, call mcd(n, m % n) until m % n equals 0.
    """
    if n == 0:
        return m
    else:
        return mcd(n, m % n)

# Prompt for user input with validation to ensure positive integers.
num1 = int(input("Digite su primer numero:\n"))
while num1 < 0:
    num1 = int(input("Diga un numero entero positivo. Digite su primer numero:\n"))
    
num2 = int(input("Digite su segundo numero:\n"))
while num2 < 0:
    num2 = int(input("Diga un numero entero positivo. Digite su segundo numero:\n"))

# Print the computed Greatest Common Divisor (GCD).
print(f"El maximo comun divisor entre los numeros {num1} y {num2} es {mcd(num1, num2)}")