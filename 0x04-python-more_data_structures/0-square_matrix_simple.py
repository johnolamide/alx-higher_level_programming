#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    """square of all values in a matrix

    Args:
        matrix: matrix of integers

    Returns:
        squared values of matrix
    """
    new_matrix = []
    for row in matrix:
        new_row = [i**2 for i in row]
        new_matrix.append(new_row)
    return new_matrix


if __name__ == "__main__":
    matrix = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]

    new_matrix = square_matrix_simple(matrix)
    print(new_matrix)
    print(matrix)
