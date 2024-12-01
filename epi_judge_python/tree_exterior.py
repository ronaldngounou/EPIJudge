import functools
from typing import List

from binary_tree_node import BinaryTreeNode
from test_framework import generic_test
from test_framework.test_failure import TestFailure
from test_framework.test_utils import enable_executor_hook


def exterior_binary_tree(tree: BinaryTreeNode) -> List[BinaryTreeNode]:
    def is_leaf(node: BinaryTreeNode) -> bool:
        return not node.left and not node.right
    
    def left_boundary(subtree: BinaryTreeNode):
        if not subtree or is_leaf(subtree):
            return 
        exterior.append(subtree)
        
        if subtree.left:
            left_boundary(subtree.left)
        else:
            left_boundary(subtree.right)

    
    def right_boundary(subtree: BinaryTreeNode):
        if not subtree or is_leaf(subtree):
            return 
        if subtree.right:
            right_boundary(subtree.right)
        else:
            right_boundary(subtree.left)
        exterior.append(subtree)
    
    def leaves(subtree: BinaryTreeNode):
        if not subtree: 
            return 
        if not subtree.left and not subtree.right:
            exterior.append(subtree)
            return
        
        leaves(subtree.left)
        leaves(subtree.right) 
    
    if not tree:
        return []

    exterior = [tree]
    left_boundary(tree.left)
    leaves(tree.left)
    leaves(tree.right)
    right_boundary(tree.right)

    return exterior




def create_output_list(L):
    if any(l is None for l in L):
        raise TestFailure('Resulting list contains None')
    return [l.data for l in L]


@enable_executor_hook
def create_output_list_wrapper(executor, tree):
    result = executor.run(functools.partial(exterior_binary_tree, tree))

    return create_output_list(result)


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('tree_exterior.py', 'tree_exterior.tsv',
                                       create_output_list_wrapper))
