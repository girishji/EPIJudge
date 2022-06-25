import functools

from bst_node import BstNode
from test_framework import generic_test
from test_framework.binary_tree_utils import must_find_node
from test_framework.test_utils import enable_executor_hook


def pair_includes_ancestor_and_descendant_of_m(
    possible_anc_or_desc_0: BstNode, possible_anc_or_desc_1: BstNode, middle: BstNode
) -> bool:
    if any(
        [
            middle.data == possible_anc_or_desc_0.data,
            middle.data == possible_anc_or_desc_1.data,
            possible_anc_or_desc_0.data == possible_anc_or_desc_1.data,
        ]
    ):
        return False

    def find_desc(start, n):
        if not start:
            return False
        if start.data == n.data:
            return True
        if n.data < start.data:
            return find_desc(start.left, n)
        return find_desc(start.right, n)

    return (
        find_desc(possible_anc_or_desc_0, middle)
        and find_desc(middle, possible_anc_or_desc_1)
    ) or (
        find_desc(possible_anc_or_desc_1, middle)
        and find_desc(middle, possible_anc_or_desc_0)
    )


@enable_executor_hook
def pair_includes_ancestor_and_descendant_of_m_wrapper(
    executor, tree, possible_anc_or_desc_0, possible_anc_or_desc_1, middle_idx
):
    candidate0 = must_find_node(tree, possible_anc_or_desc_0)
    candidate1 = must_find_node(tree, possible_anc_or_desc_1)
    middle_node = must_find_node(tree, middle_idx)

    return executor.run(
        functools.partial(
            pair_includes_ancestor_and_descendant_of_m,
            candidate0,
            candidate1,
            middle_node,
        )
    )


if __name__ == "__main__":
    exit(
        generic_test.generic_test_main(
            "descendant_and_ancestor_in_bst.py",
            "descendant_and_ancestor_in_bst.tsv",
            pair_includes_ancestor_and_descendant_of_m_wrapper,
        )
    )
