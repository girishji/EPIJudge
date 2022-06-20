import functools
from typing import List

from binary_tree_node import BinaryTreeNode
from test_framework import generic_test
from test_framework.test_failure import TestFailure
from test_framework.test_utils import enable_executor_hook


def exterior_binary_tree(tree: BinaryTreeNode) -> List[BinaryTreeNode]:
    if not tree:
        return []

    def leaves(tree):
        if not tree.left and not tree.right:
            res.append(tree)
            return
        if tree.left:
            leaves(tree.left)
        if tree.right:
            leaves(tree.right)

    def leftside(tree):
        if tree.left:
            res.append(tree)
            leftside(tree.left)
        elif tree.right:
            res.append(tree)
            leftside(tree.right)

    def rightside(tree):
        if tree.right:
            rightside(tree.right)
            res.append(tree)
        elif tree.left:
            rightside(tree.left)
            res.append(tree)

    res = [tree]
    if tree.left:
        leftside(tree.left)
    if tree.left or tree.right:
        leaves(tree)
    if tree.right:
        rightside(tree.right)
    return res


def create_output_list(L):
    if any(l is None for l in L):
        raise TestFailure("Resulting list contains None")
    return [l.data for l in L]


@enable_executor_hook
def create_output_list_wrapper(executor, tree):
    result = executor.run(functools.partial(exterior_binary_tree, tree))

    return create_output_list(result)


if __name__ == "__main__":
    exit(
        generic_test.generic_test_main(
            "tree_exterior.py", "tree_exterior.tsv", create_output_list_wrapper
        )
    )
