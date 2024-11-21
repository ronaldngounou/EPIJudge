from binary_tree_node import BinaryTreeNode
from test_framework import generic_test


def has_path_sum(tree: BinaryTreeNode, remaining_weight: int) -> bool:
    """
    Check if there exits a leaf whose path weight is equal to the 'remaining_weight' integer.
    Args: 
        - tree
        - remaining_weight
    """
    if not tree:
        return False

    # helper function
    return has_path_sum_rec(tree, remaining_weight, 0)

def has_path_sum_rec(node: BinaryTreeNode, remaining_weight: int, partial_weight: int) -> bool:
    """
    Helper function to compute 'has_path_sum()'
    """
    # Base case 
    if not node:
        return False
    # Add the current node's data to the running sum 
    partial_weight += node.data 

    # Case1: Leaf
    if is_leaf(node):
        return partial_weight == remaining_weight 

    # Case2: Non-Leaf
    return has_path_sum_rec(node.left, remaining_weight, partial_weight) \
        or has_path_sum_rec(node.right, remaining_weight, partial_weight)


def is_leaf(node: BinaryTreeNode) -> bool:
    """
    Check if a node is a leaf.
    """
    return not node.left and not node.right 



if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('path_sum.py', 'path_sum.tsv',
                                       has_path_sum))
