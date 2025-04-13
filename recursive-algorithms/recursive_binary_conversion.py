"""
recursive_binary_conversion.py
------------------------------
This module provides a recursive function to convert a positive integer into its binary representation.
The algorithm repeatedly divides the number by 2 and records the remainder in a global list. 
Once the recursion terminates, the collected remainders (representing the binary digits) are reversed
and joined into a string that represents the binary notation of the input integer.

Usage:
    The program reads a positive integer from standard input, calls the recursive binary conversion function,
    and prints the resulting binary string.
"""

# Read a positive integer from the user.
n = int(input("n="))

def binario(n):
    """
    Recursively computes the binary representation of the integer n.
    
    For each recursive call, the function divides n by 2 and appends the remainder ("1" or "0")
    to the global list 'lista'. The base case occurs when the integer division of n by 2 is zero,
    at which point the function appends "1" and terminates.
    
    Args:
        n (int): The current integer value to convert to binary.
    """
    if n // 2 == 0:
        lista.append("1")
    else:
        if n % 2 == 0:
            lista.append("0")
        else:
            lista.append("1")
        return binario(n // 2)

# Global list to store binary digits during recursion.
lista = []
binario(n)
# The binary string is the reversed version of the appended list.
print(''.join(lista[::-1]))
