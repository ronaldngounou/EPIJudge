import functools
from typing import Optional

from binary_tree_with_parent_prototype import BinaryTreeNode
from test_framework import generic_test
from test_framework.binary_tree_utils import must_find_node
from test_framework.test_failure import TestFailure
from test_framework.test_utils import enable_executor_hook


def lca_without_hashmap(node0: BinaryTreeNode,
        node1: BinaryTreeNode) -> Optional[BinaryTreeNode]:
    """
    If both nodes are at the same level and if we traverse up using parent pointers
    of both nodes, the first common node in the path to root is the lca.
    1. Calculate the depth of both nodes.
    2. Move up from the deeper node to the delta between the depths
    3. Once both are at the same level, traverse them up and return the first common node.
    """
    depth0, depth1 = map(get_depth, (node0, node1))

    # Make node 0 the deeper node to simplify the code
    if depth1 > depth0:
        node1, node0 = node0, node1

    delta_depth = abs(depth1 - depth0)

    # Go up (ascend) from the deeper node 
    while delta_depth > 0:
        node0 = node0.parent
        delta_depth -= 1
    
    # Now ascends both nodes until we reach LCA
    while node0 != node1:
        node0 = node0.parent 
        node1 = node1.parent 
    
    return node0 


def get_depth(node: BinaryTreeNode) -> int:
    depth = 0 
    while node.parent is not None:
        depth += 1
        node = node.parent 
    
    return depth 

   


def lca_with_hashmap(node0: BinaryTreeNode,
        node1: BinaryTreeNode) -> Optional[BinaryTreeNode]:
    """
    One appproach consist at using a hashmap to store the node ancestors in the hashmap
    This approach has both time and space complexity of O(h), where h is the height of the tree.
    """
    ancestors = {}

    # Insert node1 and its ancestors in the map
    while node0 is not None:
        ancestors[node0] = True 
        node0 = node0.parent 
    
    # Check if node2 is present in node1 ancestors
    while node1 is not None:
        if node1 in ancestors:
            return node1 
        
        node1 = node1.parent     

    return None 





@enable_executor_hook
def lca_wrapper(executor, tree, node0, node1):
    result = executor.run(
        functools.partial(lca_without_hashmap, must_find_node(tree, node0),
                          must_find_node(tree, node1)))

    if result is None:
        raise TestFailure('Result can\'t be None')
    return result.data


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('lowest_common_ancestor_with_parent.py',
                                       'lowest_common_ancestor.tsv',
                                       lca_wrapper))
