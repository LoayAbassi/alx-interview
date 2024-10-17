#!/usr/bin/env python3
"""contains a minoperations function"""


def minOperations(n: int) -> int:
    """
    Args:
        n (int): goal Hs

    Returns:
        int: _description_
    """
    if n <= 1:
        return 0

    divisor: int = 2

    operations: int = 0

    while n > 1:
        if n % divisor == 0:
            operations += divisor
            n //= divisor

        else:
            divisor += 1

    return operations
