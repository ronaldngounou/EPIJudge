import functools
from typing import Optional

from binary_tree_with_parent_prototype import BinaryTreeNode
from test_framework import generic_test
from test_framework.binary_tree_utils import must_find_node
from test_framework.test_utils import enable_executor_hook


def find_successor(node: BinaryTreeNode) -> Optional[BinaryTreeNode]:
    """
    The successor in a binary tree is the node that appears immediately after
    the given node in an inorder traversal.
    """
    if not node:
        return None 
    cur_node = node 
    
    if cur_node.right:
        # Find the left most element in node's right subtree
        cur_node =  cur_node.right 
        while cur_node.left:
            cur_node = cur_node.left 
        return cur_node 
    
    # Find the closest ancestor whose left subtree contains node 
    while cur_node.parent and cur_node.parent.right == cur_node:
        cur_node = cur_node.parent 
    
    return cur_node.parent 

@enable_executor_hook
def find_successor_wrapper(executor, tree, node_idx):
    node = must_find_node(tree, node_idx)

    result = executor.run(functools.partial(find_successor, node))

    return result.data if result else -1


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('successor_in_tree.py',
                                       'successor_in_tree.tsv',
                                       find_successor_wrapper))
