import functools
from typing import List

from binary_tree_node import BinaryTreeNode
from test_framework import generic_test
from test_framework.test_utils import enable_executor_hook


def reconstruct_preorder(preorder: List[int]) -> BinaryTreeNode:
    if not preorder:
        return None
    def construct(preorder, idx):
        if not preorder[idx]:
            return idx + 1, None
        lidx, lroot = construct(preorder, idx + 1)
        ridx, rroot = construct(preorder, lidx)
        return ridx, BinaryTreeNode(preorder[idx], lroot, rroot)

    return construct(preorder, 0)[1]

    # root = BinaryTreeNode(preorder[0], None, None)
    # node = root
    # ln = rn = None
    # for n in preorder:
    #     if not n:
    #         if not ln and not rn:
    #             node.left = None
    #             ln = True
    #         elif ln and not rn:
    #             node.right = None
    #             rn = True
    #         else:
    #             ln = rn = False
    #
    #     
    # return BinaryTreeNode()


@enable_executor_hook
def reconstruct_preorder_wrapper(executor, data):
    data = [None if x == 'null' else int(x) for x in data]
    return executor.run(functools.partial(reconstruct_preorder, data))


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('tree_from_preorder_with_null.py',
                                       'tree_from_preorder_with_null.tsv',
                                       reconstruct_preorder_wrapper))
