from binary_tree_node import BinaryTreeNode
from test_framework import generic_test


def has_path_sum(tree: BinaryTreeNode, remaining_weight: int) -> bool:
    def do_sum(tree, wt, isum):
        isum += tree.data
        if not tree.left and not tree.right:
            return isum == wt
        if tree.left and tree.right:
            return any([do_sum(tree.left, wt, isum), do_sum(tree.right, wt, isum)])
        return (
            do_sum(tree.left, wt, isum) if tree.left else do_sum(tree.right, wt, isum)
        )

    return do_sum(tree, remaining_weight, 0) if tree else False


if __name__ == "__main__":
    exit(generic_test.generic_test_main("path_sum.py", "path_sum.tsv", has_path_sum))
