import functools
from typing import Optional

from binary_tree_node import BinaryTreeNode
from test_framework import generic_test
from test_framework.binary_tree_utils import must_find_node, strip_parent_link
from test_framework.test_failure import TestFailure
from test_framework.test_utils import enable_executor_hook


def post(tree, nodes):
    if not tree:
        return None, nodes
    lst, ln = post(tree.left, nodes.copy())
    rst, rn = post(tree.right, nodes.copy())
    if lst:
        return lst, []
    if rst:
        return rst, []
    remaining = [n for n in ln if n in rn]
    if tree in remaining:
        remaining.remove(tree)
    if not remaining:
        return tree, []
    return None, remaining


def lca(
    tree: BinaryTreeNode, node0: BinaryTreeNode, node1: BinaryTreeNode
) -> Optional[BinaryTreeNode]:
    if node0 is node1:
        return node0
    return post(tree, [node0, node1])[0]


@enable_executor_hook
def lca_wrapper(executor, tree, key1, key2):
    strip_parent_link(tree)
    result = executor.run(
        functools.partial(
            lca, tree, must_find_node(tree, key1), must_find_node(tree, key2)
        )
    )

    if result is None:
        raise TestFailure("Result can't be None")
    return result.data


if __name__ == "__main__":
    exit(
        generic_test.generic_test_main(
            "lowest_common_ancestor.py", "lowest_common_ancestor.tsv", lca_wrapper
        )
    )
