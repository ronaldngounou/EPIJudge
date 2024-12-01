from typing import List

from binary_tree_with_parent_prototype import BinaryTreeNode
from test_framework import generic_test


def inorder_traversal(tree: BinaryTreeNode) -> List[int]:
    if not tree:
        return []
    node = tree 
    prev = None
    inorder = []

    while node:
        if prev is node.parent:
            # If we came down to node from prev 
            if node.left:
                next = node.left
            else:
                inorder.append(node.data)
                # Done with left, so now go right if right is not empty
                next = node.right if node.right else node.parent 
        elif node.left is prev:
            inorder.append(node.data)
            # Done with left, so go right if right is not empty. Otherwise go up
            next = node.right if node.right else node.parent 
        else:
            next = node.parent 
        
        prev = node
        node = next

    return inorder

        


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('tree_with_parent_inorder.py',
                                       'tree_with_parent_inorder.tsv',
                                       inorder_traversal))
