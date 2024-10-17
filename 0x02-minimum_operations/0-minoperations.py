#!/usr/bin/python3
"""
This module contains the minOperations
function, which calculates the fewest
number of operations needed to result
in exactly n 'H' characters.
"""


def minOperations(n: int) -> int:
    """
    Calculate the minimum number of 
    operations needed to result in exactly
    n 'H' characters.


    """
    if n <= 1:
        return 0

    divisor: int = 2
    operations: int = 0

    while n > 1:
        while n % divisor == 0:
            operations += divisor
            n //= divisor
        divisor += 1

    return operations
