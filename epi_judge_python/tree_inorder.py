from typing import List

from binary_tree_node import BinaryTreeNode
from test_framework import generic_test


def inorder_traversal(tree: BinaryTreeNode) -> List[int]:
    stack = [tree] if tree else []
    res = []
    processed = set()
    while stack:
        if stack[-1].left and stack[-1].left not in processed:
            stack.append(stack[-1].left)
        else:
            n = stack.pop()
            processed.add(n)
            res.append(n.data)
            if n.right and n.right not in processed:
                stack.append(n.right)

    return res


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('tree_inorder.py', 'tree_inorder.tsv',
                                       inorder_traversal))
