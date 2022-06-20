from typing import List

from binary_tree_node import BinaryTreeNode
from test_framework import generic_test
from collections import deque


def binary_tree_depth_order(tree: BinaryTreeNode) -> List[List[int]]:
    que = deque()
    dummy = BinaryTreeNode(None, None, None)
    res = []
    if not tree:
        return []
    que.append(tree)
    que.append(dummy)
    lev = []
    while que:
        n = que.popleft()
        if n is dummy:
            res.append(lev)
            lev = []
            if que:
                que.append(dummy)
            continue
        lev.append(n.data)
        if n.left:
            que.append(n.left)
        if n.right:
            que.append(n.right)
    return res


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('tree_level_order.py',
                                       'tree_level_order.tsv',
                                       binary_tree_depth_order))
