from typing import List

from binary_tree_node import BinaryTreeNode
from test_framework import generic_test


def binary_tree_from_preorder_inorder(preorder: List[int],
                                      inorder: List[int]) -> BinaryTreeNode:
    if not preorder:
        return None
    root = preorder[0]
    if len(preorder) == 1:
        return BinaryTreeNode(root, None, None)
    lio = inorder[:inorder.index(root)]
    leftn = rightn = None
    if len(lio) > 0:
        lpo = preorder[1:len(lio) + 1]
        leftn = binary_tree_from_preorder_inorder(lpo, lio)
    rio = inorder[inorder.index(root) + 1:]
    if len(rio) > 0:
        rpo = preorder[1 + len(lio):]
        rightn = binary_tree_from_preorder_inorder(rpo, rio)
    return BinaryTreeNode(preorder[0], leftn, rightn)


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('tree_from_preorder_inorder.py',
                                       'tree_from_preorder_inorder.tsv',
                                       binary_tree_from_preorder_inorder))
