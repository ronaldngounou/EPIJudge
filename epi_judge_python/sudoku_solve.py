import copy
import functools
import math
from typing import List

from test_framework import generic_test
from test_framework.test_failure import TestFailure
from test_framework.test_utils import enable_executor_hook


def solve_sudoku(partial_assignment: List[List[int]]) -> bool:
    for row in range(9):
        for col in range(9):
            if partial_assignment[row][col] == 0:
                for num in range(1, 10):
                    if is_valid(partial_assignment, row, col, num):
                        partial_assignment[row][col] = num 
                        
                        if solve_sudoku(partial_assignment):
                            return True

                        partial_assignment[row][col] = 0 #Backtrack
                
                return False # Return False to trigger backtracking
    return True
                    



def is_valid(board, row, col, num):
    # Check if num is in the row 
    if num in board[row]:
        return False

    # Check if num is in the col 
    for i in range(9):
        if board[i][col] == num:
            return False 

    # Check if num is the 3x3 box
    start_row, start_col = (row // 3) * 3, (col // 3) * 3 
    for i in range(3):
        for j in range(3):
            if board[start_row + i][start_col + j] == num:
                return False 
    
    return True 



def assert_unique_seq(seq):
    seen = set()
    for x in seq:
        if x == 0:
            raise TestFailure('Cell left uninitialized')
        if x < 0 or x > len(seq):
            raise TestFailure('Cell value out of range')
        if x in seen:
            raise TestFailure('Duplicate value in section')
        seen.add(x)


def gather_square_block(data, block_size, n):
    block_x = (n % block_size) * block_size
    block_y = (n // block_size) * block_size

    return [
        data[block_x + i][block_y + j] for j in range(block_size)
        for i in range(block_size)
    ]


@enable_executor_hook
def solve_sudoku_wrapper(executor, partial_assignment):
    solved = copy.deepcopy(partial_assignment)

    executor.run(functools.partial(solve_sudoku, solved))

    if len(partial_assignment) != len(solved):
        raise TestFailure('Initial cell assignment has been changed')

    for (br, sr) in zip(partial_assignment, solved):
        if len(br) != len(sr):
            raise TestFailure('Initial cell assignment has been changed')
        for (bcell, scell) in zip(br, sr):
            if bcell != 0 and bcell != scell:
                raise TestFailure('Initial cell assignment has been changed')

    block_size = int(math.sqrt(len(solved)))
    for i, solved_row in enumerate(solved):
        assert_unique_seq(solved_row)
        assert_unique_seq([row[i] for row in solved])
        assert_unique_seq(gather_square_block(solved, block_size, i))


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('sudoku_solve.py', 'sudoku_solve.tsv',
                                       solve_sudoku_wrapper))
