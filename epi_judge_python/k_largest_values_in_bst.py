from typing import List

from bst_node import BstNode
from test_framework import generic_test, test_utils


def find_k_largest_in_bst(tree: BstNode, k: int) -> List[int]:
    res = []

    def postorder(tree, k):
        if tree.right:
            postorder(tree.right, k)
        if len(res) < k:
            res.append(tree.data)
        if tree.left:
            postorder(tree.left, k)
        return res

    return postorder(tree, k) if tree else []


if __name__ == "__main__":
    exit(
        generic_test.generic_test_main(
            "k_largest_values_in_bst.py",
            "k_largest_values_in_bst.tsv",
            find_k_largest_in_bst,
            test_utils.unordered_compare,
        )
    )
