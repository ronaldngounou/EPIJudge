import functools
from typing import Optional

from binary_tree_node import BinaryTreeNode
from test_framework import generic_test
from test_framework.binary_tree_utils import must_find_node, strip_parent_link
from test_framework.test_failure import TestFailure
from test_framework.test_utils import enable_executor_hook


def lca(tree: BinaryTreeNode, node0: BinaryTreeNode,
        node1: BinaryTreeNode) -> Optional[BinaryTreeNode]:
    return lca_rec(tree, node0, node1)

def lca_rec(root: BinaryTreeNode, node0: BinaryTreeNode, node1: BinaryTreeNode):
    """
    Returns the LCA of a binary tree node.
    Args:
        - node0
        - node1
        - node2
    """
    if not root:
        return None 
    
    if root.data == node0.data or root.data == node1.data:
        return root 

    left = lca_rec(root.left, node0, node1)
    right = lca_rec(root.right, node0, node1)

    if left is None:
        return right 
    if right is None:
        return left 
    if left and right:
        return root 
    
    # return left if left else right 

    





@enable_executor_hook
def lca_wrapper(executor, tree, key1, key2):
    strip_parent_link(tree)
    result = executor.run(
        functools.partial(lca, tree, must_find_node(tree, key1),
                          must_find_node(tree, key2)))

    if result is None:
        raise TestFailure('Result can\'t be None')
    return result.data


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('lowest_common_ancestor.py',
                                       'lowest_common_ancestor.tsv',
                                       lca_wrapper))
