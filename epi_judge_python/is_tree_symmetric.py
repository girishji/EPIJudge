from binary_tree_node import BinaryTreeNode
from test_framework import generic_test


def iot(tree):
    if not tree:
        return []
    return iot(tree.left) + [tree.data] + iot(tree.right)


def is_symmetric(tree: BinaryTreeNode) -> bool:
    if not tree:
        return True
    lst = iot(tree.left)
    rst = iot(tree.right)
    if len(rst) > 1:
        rst.reverse()
    return lst == rst


if __name__ == "__main__":
    exit(
        generic_test.generic_test_main(
            "is_tree_symmetric.py", "is_tree_symmetric.tsv", is_symmetric
        )
    )
