"""
recursive_subarray_sum.py
-------------------------
This module implements a recursive solution to sum the elements of a sub-array between two given indices.
It uses a divide-and-conquer approach by splitting the sub-array and a helper function to "conquer" (i.e., sum)
the elements recursively.

The approach:
    - If the list is empty, the sum is 0.
    - If the sub-array has only one element (i.e., i == j), it returns twice that element.
      (According to the provided strategy, the idea is to add the element with itself.)
    - If the index j is greater than i (indicating an error or an unexpected configuration according to the invariant),
      it returns 0.
    - Otherwise, the function splits the sub-array into two parts and recursively sums both parts using the helper function.
    
Note:
    The implementation uses a helper function `conquistar` to compute the sum of a list recursively.
"""

def dividir(lista, i, j):
    """
    Recursively computes a sum over a sub-array of 'lista' delimited by indices i and j.

    Args:
        lista (list): A list of integers.
        i (int): The starting index for the sub-array.
        j (int): The ending index for the sub-array.

    Returns:
        int: The sum of the sub-array between indices i and j, based on a recursive divide-and-conquer strategy.

    Strategy:
        - If the list is empty, return 0.
        - If i equals j, return the sum of the element at index i with itself.
        - If j is greater than i, return 0.
        - Otherwise, split the sub-array by the midpoint and sum the results of the two halves using `conquistar`.
    """
    if len(lista) == 0:
        return 0
    elif i == j:
        k = lista[i] + lista[i]
        return k
    elif j > i:
        return 0
    else:
        mid = (i + j) // 2
        left = lista[i:mid + 1]
        right = lista[mid + 1:j + 1]
        suma = conquistar(left) + conquistar(right)
        return suma  

def conquistar(a):
    """
    Recursively calculates the sum of all elements in the list 'a'.

    Args:
        a (list): A list (sub-array) of integers.

    Returns:
        int: The sum of the elements of the list.
        
    Strategy:
        - If the list has one element, return that element.
        - Otherwise, return the first element plus the recursive sum of the rest of the list.
    """
    if len(a) == 1:
        return a[0]
    else:
        return a[0] + conquistar(a[1:])
