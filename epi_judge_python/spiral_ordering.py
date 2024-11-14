from typing import List

from test_framework import generic_test


def matrix_in_spiral_order(square_matrix: List[List[int]]) -> List[int]:
    if not square_matrix:
        return []
    
    rows, cols = len(square_matrix), len(square_matrix[0])
    row = 0 
    col = -1
    direction = 1 
    result = []

    while rows > 0 and cols > 0:
        for _ in range(cols):
            col += direction 
            result.append(square_matrix[row][col])
        rows -= 1 

        for _ in range(rows):
            row += direction 
            result.append(square_matrix[row][col])
        cols -= 1 

        direction *= -1 
    
    return result 



if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('spiral_ordering.py',
                                       'spiral_ordering.tsv',
                                       matrix_in_spiral_order))
