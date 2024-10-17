#!/usr/bin/env python3
"""
contains a minoperations function
"""


def minOperations(n):
    """
    returns minimum operations
    """
    if n <= 1:
        return 0

    divisor = 2
    operations = 0

    while n > 1:
        while not (n % divisor):
            operations += divisor
            n /= divisor
        divisor += 1

    return operations
