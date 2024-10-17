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
    current_length: int = 1
    operations: int = 0
    while current_length < n:
        if n % current_length == 0:
            operations += 1
            current_length *= 2
        else:
            operations += 2
            current_length += 1

    return operations
