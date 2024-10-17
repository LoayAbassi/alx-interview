#!/usr/bin/env python3
"""contains a minoperations function"""


def minOperations(n):
    """
    Args:
        n (int): goal Hs

    Returns:
        int: _description_
    """
    if n <= 1:
        return 0

    divisor= 2

    operations= 0

    while n > 1:
        if n % divisor == 0:
            operations += divisor
            n //= divisor

        else:
            divisor += 1

    return operations
