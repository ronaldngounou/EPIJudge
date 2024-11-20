from binary_tree_node import BinaryTreeNode
from test_framework import generic_test


def is_symmetric(tree: BinaryTreeNode) -> bool:
    if not tree:
        return False
    return is_symmetric_helper(tree.left, tree.right)

def is_symmetric_helper(subtree0: BinaryTreeNode, subtree1: BinaryTreeNode) -> bool:
    if not subtree0 and not subtree1:
        return True 
    elif subtree1 and subtree0:
        return subtree0.data == subtree1.data \
            and is_symmetric_helper(subtree0.left, subtree1.right) \
            and is_symmetric_helper(subtree0.right, subtree1.left)
    return False


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('is_tree_symmetric.py',
                                       'is_tree_symmetric.tsv', is_symmetric))
