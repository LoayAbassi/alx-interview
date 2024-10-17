#!/usr/bin/env python3
"""Contains a minOperations function"""

def minOperations(n: int) -> int:
    """
    Args:
        n (int): goal 'H's number
    Returns:
        int: minimum operations to reach n
    """
    if n <= 1:
        return 0

    operations = 0
    divisor = 2

    # Loop until n becomes 1
    while n > 1:
        # Check if divisor can divide n
        while n % divisor == 0:
            operations += divisor  # Add the divisor to operations
            n //= divisor  # Reduce n
        divisor += 1  # Move to the next potential divisor

        # Optimization: Stop if divisor exceeds sqrt(n)
        if divisor * divisor > n:
            if n > 1:  # If n is still greater than 1, it is prime
                operations += n  # Add n itself as an operation
            break

    return operations