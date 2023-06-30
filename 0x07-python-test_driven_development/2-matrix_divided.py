#!/usr/bin/python3
"""
    Module contains: matrix_divided function
"""


def matrix_divided(matrix, div):
    """ a function that divides all elements of a matrix

        Args:
            matrix (list of lists): a list of lists of integers or float
            div (int or float): number to divide the matrix elements

        Returns:
            list of lists: a new matrix

        Raises:
            TypeError: if matrix is not a list of list or row is not
                        the same size
            ZeroDivisionError: for division by zero
    """
    matrix_error = "matrix must be a matrix (list of lists) of integers/floats"
    # check if matrix is a list of list
    if (type(matrix) != list):
        raise TypeError(matrix_error)
    # check if every value in the matrix is an int or float value
    else:
        for row in matrix:
            if (type(row) != list):
                raise TypeError(matrix_error)
            row_length = len(matrix[0])
            if len(row) != row_length:
                raise TypeError("Each row of the matrix must have the same size")
            for element in row:
                if (type(element) != int and type(element) != float):
                    raise TypeError(matrix_error)
    # check if div is not an integer or float value
    if (type(div) != int and type(div) != float):
        raise TypeError("div must be a number")
    # check for zero division
    if div == 0:
        raise ZeroDivisionError("division by zero")
    result = [list(map(lambda x: round(x / div, 2), row)) for row in matrix]
    return result


if __name__ == "__main__":
    matrix = [
        [1, 2, 3],
        [4, 5, 6]
    ]
    print(matrix_divided(matrix, 3))
    print(matrix)
