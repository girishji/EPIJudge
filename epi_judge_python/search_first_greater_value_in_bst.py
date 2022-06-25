from typing import Optional

from bst_node import BstNode
from test_framework import generic_test


def find_first_greater_than_k(tree: BstNode, k: int) -> Optional[BstNode]:
    # examine pairs

    def get_next(tree):
        if not tree.right:
            return None
        tree = tree.right
        while tree.left:
            tree = tree.left
        return tree

    def get_prev(tree):
        if not tree.left:
            return None
        tree = tree.left
        while tree.right:
            tree = tree.right
        return tree

    if not tree:
        return None
    if k >= tree.data:
        nextv = get_next(tree)
        if nextv:
            return nextv if nextv.data > k else find_first_greater_than_k(tree.right, k)
        return nextv
    else:
        prev = get_prev(tree)
        if prev:
            return tree if prev.data <= k else find_first_greater_than_k(tree.left, k)
        return tree


def find_first_greater_than_k_wrapper(tree, k):
    result = find_first_greater_than_k(tree, k)
    return result.data if result else -1


if __name__ == "__main__":
    exit(
        generic_test.generic_test_main(
            "search_first_greater_value_in_bst.py",
            "search_first_greater_value_in_bst.tsv",
            find_first_greater_than_k_wrapper,
        )
    )
