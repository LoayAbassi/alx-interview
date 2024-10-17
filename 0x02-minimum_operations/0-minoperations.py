#!/usr/bin/env python3
"""
This module contains the minOperations
function, which calculates the fewest
number of operations needed to result
in exactly n 'H' characters.
"""


def minOperations(n):
    """
    Calculate the minimum number of 
    operations needed to result in exactly
    n 'H' characters.

    Args:
        n (int): The target number of 'H' characters.

    Returns:
        int: The minimum number of operations,
        or 0 if n is impossible to achieve.
    """
    if n <= 1:
        return 0

    divisor = 2
    operations = 0

    while n > 1:
        while n % divisor == 0:
            operations += divisor
            n //= divisor
        divisor += 1

    return operations
