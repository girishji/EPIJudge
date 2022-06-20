from binary_tree_node import BinaryTreeNode
from test_framework import generic_test


def height(tree):
    if not tree:
        return 0, True
    hl, balancedl = height(tree.left)
    hr, balancedr = height(tree.right)
    if not balancedl or not balancedr or abs(hl - hr) > 1:
        return 0, False
    return max(hl, hr) + 1, True


def is_balanced_binary_tree(tree: BinaryTreeNode) -> bool:
    return height(tree)[1]


if __name__ == "__main__":
    exit(
        generic_test.generic_test_main(
            "is_tree_balanced.py", "is_tree_balanced.tsv", is_balanced_binary_tree
        )
    )
