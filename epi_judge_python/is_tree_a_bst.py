from binary_tree_node import BinaryTreeNode
from test_framework import generic_test


def is_binary_tree_bst(tree: BinaryTreeNode) -> bool:
    
    def is_bst(tree):
        lmin, lmax, rmin, rmax = [tree.data] * 4
        if tree.left:
            lmin, lmax, bst = is_bst(tree.left)
            if not bst or lmax > tree.data:
                return (0, 0, False)
        if tree.right:
            rmin, rmax, bst = is_bst(tree.right)
            if not bst or rmin < tree.data:
                return (0, 0, False)
        return (lmin, rmax, True)

    return is_bst(tree)[2] if tree else True

    # from collections import deque
    #
    # que = deque([tree])
    # while que:
    #     n = que.popleft()
    #     if n.left and n.left.data > n.data or (n.right and n.right.data < n.data):
    #         return False
    #     if n.left:
    #         que.append(n.left)
    #     if n.right:
    #         que.append(n.right)
    # return True



if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('is_tree_a_bst.py', 'is_tree_a_bst.tsv',
                                       is_binary_tree_bst))
