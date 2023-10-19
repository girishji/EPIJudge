import collections
from typing import List

from bst_node import BstNode
from test_framework import generic_test

Interval = collections.namedtuple("Interval", ("left", "right"))


def range_lookup_in_bst(tree: BstNode, interval: Interval) -> List[int]:

    searching = True
    res = []

    def range_lookup(tree, interval):
        nonlocal searching, res
        if searching:
            if interval.left.data <= tree.data:
                if (
                    (tree.left and tree.left.data < interval.left.data)
                    or not tree.left
                    or interval.left.data == tree.data
                ):
                    searching = False
                    res.append(tree)
                    return
                range_lookup(tree.left, interval)
            else:
                if tree.right:
                    range_lookup(tree.right, interval)
                else:
                    searching = False
        else:
            if not tree:
                return
            range_lookup(tree.left, interval)
            if tree.data > interval.right.data:
                return
            res.append(tree)
            range_lookup(tree.right, interval)

    if tree:
        range_lookup(tree, interval, True)
    return res if tree else []


def range_lookup_in_bst_wrapper(tree, i):
    return range_lookup_in_bst(tree, Interval(*i))


if __name__ == "__main__":
    exit(
        generic_test.generic_test_main(
            "range_lookup_in_bst.py",
            "range_lookup_in_bst.tsv",
            range_lookup_in_bst_wrapper,
        )
    )
