from typing import List

from binary_tree_with_parent_prototype import BinaryTreeNode
from test_framework import generic_test


def inorder_traversal(tree: BinaryTreeNode) -> List[int]:
    res = []
    prev, res = None, []
    while tree:
        # have 2 pointers, prev and tree
        if prev is tree.parent:  # going down
            if tree.left:
                prev = tree
                tree = tree.left
            else:
                res.append(tree.data)
                prev = tree
                tree = tree.right or tree.parent
        elif prev is tree.left:  # going up
            res.append(tree.data)
            prev = tree
            tree = tree.right or tree.parent
        else:  # done with subtree
            prev = tree
            tree = tree.parent

    return res


if __name__ == "__main__":
    exit(
        generic_test.generic_test_main(
            "tree_with_parent_inorder.py",
            "tree_with_parent_inorder.tsv",
            inorder_traversal,
        )
    )
