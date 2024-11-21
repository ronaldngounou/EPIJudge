from binary_tree_node import BinaryTreeNode
from test_framework import generic_test


def sum_root_to_leaf(tree: BinaryTreeNode) -> int:
    """
    Compute the sum of the binary numbers represented by the root-to-leaf paths.
    Args:
        - tree: BinaryTreeNode
    """
    if not tree:
        return 0
    return sum_root_to_leaf_rec(tree, 0)


def sum_root_to_leaf_rec(node: BinaryTreeNode, partial_path_sum) -> int:
    """
    Compute the sum of the binary numbers represented by the root-to-leaf paths.
    """
    if not node:
        return 0
    
    partial_path_sum = 2 * partial_path_sum + node.data
    if is_leaf(node):
        return partial_path_sum

    # Recurse in the left and rigth subtrees
    return sum_root_to_leaf_rec(node.left, partial_path_sum) \
        + sum_root_to_leaf_rec(node.right, partial_path_sum)

def is_leaf(node):
    #return node.left is None and node.right is None 
    return not node.left and not node.right


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('sum_root_to_leaf.py',
                                       'sum_root_to_leaf.tsv',
                                       sum_root_to_leaf))
