# Pascal's Triangle Function

## Overview
This document describes the `pascal_triangle(n)` function, which generates Pascal's triangle up to the nth row. Pascal's triangle is a triangular array of the binomial coefficients. 

## Function Definition
```python
def pascal_triangle(n):
    """
    Generates Pascal's triangle up to the nth row.

    Args:
    n (int): The number of rows of Pascal's triangle to generate.

    Returns:
    list of lists: A list of lists of integers representing Pascal's triangle.
                   Returns an empty list if n <= 0.
    
    Examples:
    >>> pascal_triangle(5)
    [
        [1],
        [1, 1],
        [1, 2, 1],
        [1, 3, 3, 1],
        [1, 4, 6, 4, 1]
    ]
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


## Usage
The function can be used to generate Pascal's triangle for any positive integer `n`. Here are a few examples of its usage:

### Example 1: Generating Pascal's Triangle with 5 Rows
```python
print(pascal_triangle(5))
```
Output:
```
[
    [1],
    [1, 1],
    [1, 2, 1],
    [1, 3, 3, 1],
    [1, 4, 6, 4, 1]
]
```

### Example 2: Generating Pascal's Triangle with 0 Rows
```python
print(pascal_triangle(0))
```
Output:
```
[]
```

### Example 3: Generating Pascal's Triangle with 7 Rows
```python
print(pascal_triangle(7))
```
Output:
```
[
    [1],
    [1, 1],
    [1, 2, 1],
    [1, 3, 3, 1],
    [1, 4, 6, 4, 1],
    [1, 5, 10, 10, 5, 1],
    [1, 6, 15, 20, 15, 6, 1]
]
```

## Edge Cases
- **n <= 0**: Returns an empty list.
- **n = 1**: Returns a single row `[[1]]`.

## Assumptions
- The input `n` will always be an integer.

## Conclusion
The `pascal_triangle(n)` function is a simple yet effective way to generate Pascal's triangle. This function demonstrates basic list manipulation and the use of nested loops in Python. It is a useful tool for educational purposes and for solving combinatorial problems.
