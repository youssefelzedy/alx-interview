#!/usr/bin/python3
"""
Pascal's Triangle
"""


def pascal_triangle(n):
    """
    Returns a list of lists of integers representing the Pascal’s triangle of n

        Args:
        n (int): number of rows of Pascal's triangle

        Returns:
        list: list of lists of integers representing Pascal's triangle of n
    """

    if n <= 0:
        return []

    triangle = []

    for row_num in range(n):
        row = [1] * (row_num + 1)
        for j in range(1, row_num):
            row[j] = triangle[row_num - 1][j - 1] + triangle[row_num - 1][j]
        triangle.append(row)

    return triangle
