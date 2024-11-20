from test_framework import generic_test
from test_framework.test_failure import TestFailure
from typing import List

class ElementWIthCacheMax:
    def __init__(self, element, max):
        self.max = max
        self.element = element
class Stack:
    def __init__(self):
        self.element_with_cache_max: List[ElementWIthCacheMax] = []

    def empty(self) -> bool:
        return len(self.element_with_cache_max) == 0

    def max(self) -> int:
        return self.element_with_cache_max[-1].max 

    def pop(self) -> int:
        return self.element_with_cache_max.pop().element 

    def push(self, x: int) -> None:
        # Determine the new maximum value to cache
        if self.empty():
            new_max = x 
        else:
            # Take the maximum of the current element and the current max
            new_max = max(x, self.max())
        
        new_element = ElementWIthCacheMax(x, new_max)

        self.element_with_cache_max.append(new_element)


def stack_tester(ops):
    try:
        s = Stack()

        for (op, arg) in ops:
            if op == 'Stack':
                s = Stack()
            elif op == 'push':
                s.push(arg)
            elif op == 'pop':
                result = s.pop()
                if result != arg:
                    raise TestFailure('Pop: expected ' + str(arg) + ', got ' +
                                      str(result))
            elif op == 'max':
                result = s.max()
                if result != arg:
                    raise TestFailure('Max: expected ' + str(arg) + ', got ' +
                                      str(result))
            elif op == 'empty':
                result = int(s.empty())
                if result != arg:
                    raise TestFailure('Empty: expected ' + str(arg) +
                                      ', got ' + str(result))
            else:
                raise RuntimeError('Unsupported stack operation: ' + op)
    except IndexError:
        raise TestFailure('Unexpected IndexError exception')


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('stack_with_max.py',
                                       'stack_with_max.tsv', stack_tester))
