'''
Given a matrix of numbers and a given index, flip all values along that index.

eg. 1 2 3
    4 5 6
    7 8 9

If index=1, then result  = 1 8 3
                           4 5 6
                           7 2 9

Assumption: It will always be a square matrix.
'''

from typing import Any

def flip_one(matrix: list[list[Any]],
             index: int)->list:

    length = len(matrix)

    # add a check to see that the index is within range
    if not 0 <= index < length:
        raise IndexError(f'Please specify index value between [0, {length-1}]')

    # collect all values in in a reverse order in a list
    values = []

    for x in range(1,length+1):

        row_index = length - x

        value = matrix[row_index][index]

        values.append(value)

    for i in range(length):

        matrix[i][index] = values[i]

    return matrix
