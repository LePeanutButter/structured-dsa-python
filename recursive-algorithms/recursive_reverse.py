"""
recursive_reverse.py
--------------------
This module provides a recursive function to return the reverse of a given list.
The function `reverso` works by recursively calling itself on the tail of the list
and then concatenating the head element at the end. When the input list is empty,
an empty list is returned.

Usage:
    The function accepts a list and returns a new list whose elements are in reverse order.
"""

def reverso(a):
    """
    Recursively returns the reverse of the list 'a'.
    
    This function processes the list by removing the first element and then
    appending it at the end of the result from the recursive call on the remainder
    of the list. The base case is reached when the provided list is empty.
    
    Args:
        a (list): A list of elements.
        
    Returns:
        list: A new list that is the reverse of 'a'.
        
    Invariant:
        - Initiation: The reversed list starts empty.
        - Stability: Elements are added recursively in reverse order.
        - Termination: Occurs when 'a' is empty.
    """
    b = []
    if len(a) == 0:
        return b
    else:
        return reverso(a[1:]) + [a[0]]
