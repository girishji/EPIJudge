from typing import List, Optional

from bst_node import BstNode
from test_framework import generic_test


def rebuild_bst_from_preorder(preorder_sequence: List[int]
                              ) -> Optional[BstNode]:
    
    def preorder(seq):
        if not seq:
            return None
        tree = BstNode(seq[0])
        if len(seq) == 1:
            return tree
        tree.left = preorder([s for s in seq if s < seq[0]])
        tree.right = preorder([s for s in seq if s > seq[0]])
        return tree

    return preorder(preorder_sequence)


    # tree = BstNode(preorder_sequence[0])
    # stack = [tree]
    # idx = 1
    # while idx < len(preorder_sequence):
    #     parent = stack[-1]
    #     n = BstNode(preorder_sequence[idx])
    #     if n.data < parent.data:
    #         parent.left = n
    #         stack.append(n)
    #         idx += 1
    #     else:
    #         if len(stack) < 2:
    #             parent.right = n
    #             stack.append(n)
    #             idx += 1
    #         else:
    #             gparent = stack[-2]
    #             if parent is gparent.left and n.data > gparent.data:
    #                 stack.pop()
    #             elif parent is gparent.right:
    #                 j = -3
    #                 while len(stack) >= -j and gparent is stack[j].right:
    #                     gparent = stack[j]
    #                     j -= 1
    #                 if len(stack) >= -j and n.data > stack[j].data:
    #                     stack.pop()
    #                 else:
    #                     parent.right = n
    #                     stack.append(n)
    #                     idx += 1
    #             else:
    #                 parent.right = n
    #                 stack.append(n)
    #                 idx += 1
    #
    # return tree if preorder_sequence else None


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('bst_from_preorder.py',
                                       'bst_from_preorder.tsv',
                                       rebuild_bst_from_preorder))
