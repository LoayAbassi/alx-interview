#!/usr/bin/env python3
"""contains a minoperations function"""


def minOperations(n: int) -> int:
    """
    Args:
        n (int): goal 'H's number
    Returns:
        int: minimum operations to reach n
    """
    if n <= 1:
        return 0

    root: int = 2

    operations: int = 0

    while root <= n:
        if n % root == 0:
            operations += root
            n = n / root
            root -= 1
        root += 1

    return operations
