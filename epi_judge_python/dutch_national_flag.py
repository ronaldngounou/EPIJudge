import functools
from typing import List

from test_framework import generic_test
from test_framework.test_failure import TestFailure
from test_framework.test_utils import enable_executor_hook

RED, WHITE, BLUE = range(3)


def dutch_flag_partition(pivot_index: int, A: List[int]) -> None:
    """
    Rearrange an array A such that the elements less less than the pivot
    appear first, followed by the elements equal to the pivot, followed by
    the elements greater than the pivot.

    [1, 2, 1, 0, 2, 2, 1, 1, 1, 0, 0, 0]	0
    s
    e                   
                                      l
    
    pivot = 1

    """
    pivot = A[pivot_index]
    smaller, equal, larger = 0, 0, len(A) 

    while equal < larger:
        if A[equal] < pivot:
            A[equal], A[smaller] = A[smaller], A[equal]
            equal += 1 
            smaller += 1

        elif A[equal] > pivot:
            larger -= 1
            A[larger], A[equal] = A[equal], A[larger]

        elif A[equal] == pivot:
            equal += 1 






@enable_executor_hook
def dutch_flag_partition_wrapper(executor, A, pivot_idx):
    count = [0, 0, 0]
    for x in A:
        count[x] += 1
    pivot = A[pivot_idx]

    executor.run(functools.partial(dutch_flag_partition, pivot_idx, A))

    i = 0
    while i < len(A) and A[i] < pivot:
        count[A[i]] -= 1
        i += 1
    while i < len(A) and A[i] == pivot:
        count[A[i]] -= 1
        i += 1
    while i < len(A) and A[i] > pivot:
        count[A[i]] -= 1
        i += 1

    if i != len(A):
        raise TestFailure('Not partitioned after {}th element'.format(i))
    elif any(count):
        raise TestFailure('Some elements are missing from original array')


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('dutch_national_flag.py',
                                       'dutch_national_flag.tsv',
                                       dutch_flag_partition_wrapper))
