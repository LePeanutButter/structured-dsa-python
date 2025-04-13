"""
recursive_sort.py
-----------------
This module provides two recursive functions to sort a list of integers in ascending order.
The sorting is based on the idea of selecting the minimum element of the list, placing it at the front,
and then recursively sorting the rest of the list.

Functions:
    - sortRec2(sequence): Removes the smallest element from the list and recursively sorts the remainder using sortRec.
    - sortRec(sequence): Recursively sorts the list by creating a modified copy without the smallest element,
      and concatenating the result.
      
Both functions terminate when the input list has 0 or 1 elements.
"""

def sortRec2(sequence = []):
    """
    Recursively sorts a list of integers in ascending order.
    
    This function selects the smallest element from the input list, removes it, and then
    recursively sorts the remaining elements (using the 'sortRec' function) before concatenating
    the smallest element at the front.

    Args:
        sequence (list): A list of integers to be sorted.

    Returns:
        list: A list of integers sorted in ascending order.
    """
    if len(sequence) <= 1:
        return sequence
    ele = [min(sequence)]
    sequence.remove(ele[0])
    return ele + sortRec(sequence)

def sortRec(sequence = []):
    """
    Recursively sorts a list of integers in ascending order.
    
    This function creates a copy of the input list, selects and removes the smallest element,
    and then recursively sorts the remainder. It returns the sorted list once the list length
    is reduced to 1 or 0.

    Args:
        sequence (list): A list of integers to be sorted.

    Returns:
        list: A list of integers sorted in ascending order.
    """
    ele = []
    seq_modified = sequence[:]
    if len(sequence) > 1:
        ele = [min(sequence)]
        seq_modified.remove(ele[0])
    return sequence if len(sequence) <= 1 else (ele + sortRec(seq_modified))