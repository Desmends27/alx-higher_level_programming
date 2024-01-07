#!/usr/bin/python3
"""
    This is the matrix_divided module"
"""

def matrix_divided(matrix, div):
    """
    Args:
        matrix: list of list of integer/floats
        div: number to divide by
    Raises:
        TypeError: if matrix is not a list of lists of integers/floats
        TypeError: if div is not a number
        ZeroDivisionError: if div is zero
    """

    if not isinstance(matrix, list) or len(matrix) == 0:
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    if not isinstance(div, (float, int)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    new_matrix = [list(row) for row in matrix]
    n = len(matrix[0])
    for row in new_matrix:
        if not isinstance(row, list):
            raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
        if len(row) != n:
            raise TypeError("matrix must have each row with the same size")
        for i, elem in enumerate(row):
            if not isinstance(elem, (float, int)):
                raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
            row[i] = round(elem / div, 2)
    return new_matrix
