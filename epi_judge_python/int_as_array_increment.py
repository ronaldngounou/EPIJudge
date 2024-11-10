from typing import List

from test_framework import generic_test


def plus_one(A: List[int]) -> List[int]:
    """
    Add +1 to a number represented as list.
    """
    A[-1] += 1 
    n = len(A) - 1
    for i in range(n, 0, -1): 
        if A[i] != 10:
            break 
        A[i] = 0 
        A[i - 1] += 1 
    else:
        if A[0] == 10:
            # There is a carry out. 
            # We can append a 0 at the end of the array 
            # and set the first element of the array to be 1
            A.append(0) 
            A[0] = 1 
    
    return A 


    

if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('int_as_array_increment.py',
                                       'int_as_array_increment.tsv', plus_one))
