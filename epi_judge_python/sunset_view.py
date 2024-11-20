from typing import Iterator, List

from test_framework import generic_test

class BuildingWithHeight():
    def __init__(self, id, height):
        self.id = id 
        self.height = height
        
def examine_buildings_with_sunset(sequence: Iterator[int]) -> List[int]:
    stack: List[BuildingWithHeight] = []

    for builiding_idx, builiding_height in enumerate(sequence):
        while stack and builiding_height >= stack[-1].height:
            stack.pop()
        stack.append(BuildingWithHeight(builiding_idx, builiding_height))
    
    return [c.id for c in reversed(stack)]

def examine_buildings_with_sunset_wrapper(sequence):
    return examine_buildings_with_sunset(iter(sequence))


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('sunset_view.py', 'sunset_view.tsv',
                                       examine_buildings_with_sunset))
