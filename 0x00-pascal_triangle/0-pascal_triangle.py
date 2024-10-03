#!/usr/bin/python3
"""
contains pascal's triangle function
"""


def pascal_triangle(n):
    """
        Generates Pascal's triangle up to the nth row.

        Args:
            n (int): The number of rows to generate.

        Returns:
            List[List[int]]: Pascal's triangle with n rows.
    """
    if n <= 0:
        return []
    l = []
    for i in range(n):
        row = []
        for j in range(i+1):
            if (i > 0 and j > 0 and j < len(l[i-1])):
                row.append(l[i-1][j-1]+l[i-1][j])
            else:
                row.append(1)

        l.append(row)

    return l
