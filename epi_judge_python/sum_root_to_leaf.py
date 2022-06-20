from binary_tree_node import BinaryTreeNode
from test_framework import generic_test


def sum_root_to_leaf(tree: BinaryTreeNode) -> int:
    def preorder(node, num, _sum):
        num *= 2
        num += node.data
        if not node.left and not node.right:
            return _sum + num
        _suml = _sumr = 0
        if node.left:
            _suml = preorder(node.left, num, _sum)
        if node.right:
            _sumr = preorder(node.right, num, _sum)
        return _suml + _sumr

    _sum, num = 0, 0
    return preorder(tree, num, _sum) if tree else 0


if __name__ == "__main__":
    exit(
        generic_test.generic_test_main(
            "sum_root_to_leaf.py", "sum_root_to_leaf.tsv", sum_root_to_leaf
        )
    )
