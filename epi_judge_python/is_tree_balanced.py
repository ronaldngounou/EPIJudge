from binary_tree_node import BinaryTreeNode
from test_framework import generic_test


def is_balanced_binary_tree(tree: BinaryTreeNode) -> bool:
    if not tree:
        return True 
    
    balanceFactor = height(tree.left) - height(tree.right)

    if (abs(balanceFactor) <= 1 and is_balanced_binary_tree(tree.left) \
                                and is_balanced_binary_tree(tree.right)):
                                return True 
    
    return False

def height(tree: BinaryTreeNode) -> int:
    if not tree:
        return 0 
    return 1 + max(height(tree.left), height(tree.right))
                            


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('is_tree_balanced.py',
                                       'is_tree_balanced.tsv',
                                       is_balanced_binary_tree))
