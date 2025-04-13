# Recursive Algorithms Suite

## Introduction
This repository is a collection of six distinct recursive programs that serve as examples of solving common computational problems using recursion. The projects range from sorting and summing operations to computing the greatest common divisor, converting integers to binary, and reversing lists. Each module demonstrates a clean and educational recursive approach.

## Files Overview
- **recursive_sort.py:**  
  Implements two recursive functions, `sortRec2` and `sortRec`, that sort a list of integers in ascending order by repeatedly selecting the minimum element and recursively sorting the remainder of the list.

- **recursive_subarray_sum.py:**  
  Contains a divide-and-conquer approach to calculate the sum of elements within a subarray delimited by indices `i` and `j`. It uses a helper function `conquistar` to recursively sum the elements.

- **even_sum_recursive.py:**  
  Provides a recursive function to compute the sum of all positive even integers from a given number `N` down to 2. The function handles odd inputs by decrementing until it reaches an even number.

- **gcd_recursive.py:**  
  Implements the Euclidean algorithm recursively to calculate the Greatest Common Divisor (GCD) of two positive integers entered by the user.

- **recursive_binary_conversion.py:**  
  Converts a positive integer to its binary representation recursively by dividing the number by 2 and collecting remainders, which are then reversed to form the binary string.

- **recursive_reverse.py:**  
  Defines a recursive function `reverso` that returns a new list with the elements of the input list in reversed order.
