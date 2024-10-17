#!/usr/bin/env python3
"""contains a minoperations function."""


def minOperations(n: int) -> int:
    """
    Minoperation function.

    Args:
        n (int): goal number
    Returns:
        int: minimum operations
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
