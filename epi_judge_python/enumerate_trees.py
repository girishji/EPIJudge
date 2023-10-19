import functools
from typing import List, Optional

from binary_tree_node import BinaryTreeNode
from test_framework import generic_test
from test_framework.test_utils import enable_executor_hook


def generate_all_binary_trees(num_nodes: int) -> List[Optional[BinaryTreeNode]]:

    if num_nodes == 0:
        return [None]

    result = []

    for left_tree_count in range(num_nodes):
        right_tree_count = num_nodes - left_tree_count - 1
        left_subtrees = generate_all_binary_trees(left_tree_count)
        right_subtrees = generate_all_binary_trees(right_tree_count)

        result += [
            BinaryTreeNode(0, left, right)
            for left in left_subtrees
            for right in right_subtrees
        ]
    return result

    # trees = []
    #
    # def solve(n, tree):
    #     nonlocal trees
    #     if n == 0:
    #         return []
    #     if n == 1:
    #         if not tree:
    #             trees.append([1, 0, 0])
    #             return
    #         trees.append(tree)
    #     else:
    #         if not tree:
    #             tree = [1] + [0] * ((1 << n) - 2)
    #         for i in range(len(tree)):
    #             if not tree[i]:
    #                 continue
    #             if n > 1:
    #                 left = 2 * i + 1
    #                 right = 2 * i + 2
    #                 tr = tree.copy()
    #                 if tr[left] == 0:
    #                     tr[left] = 1
    #                     solve(n - 1, tr)
    #                 tr = tree.copy()
    #                 if tr[right] == 0:
    #                     tr[right] = 1
    #                     solve(n - 1, tr)
    #             else:
    #                 break
    #
    # solve(num_nodes, [])
    # # print("trees", trees)
    #
    #
    # def preorder(n, arr):
    #     tree = BinaryTreeNode()
    #     left = 2 * n + 1
    #     right = 2 * n + 2
    #     if left < len(arr) and arr[left]:
    #         tree.left = preorder(left, arr)
    #     if right < len(arr) and arr[right]:
    #         tree.right = preorder(right, arr)
    #     return tree
    #
    # result = []
    # while trees:
    #     tr = trees.pop()
    #     if tr in trees:
    #         continue
    #     # print(tr)
    #     result.append(preorder(0, tr))
    #
    # return [[]] if num_nodes == 0 else result


# generate_all_binary_trees(3)


def serialize_structure(tree):
    result = []
    q = [tree]
    while q:
        a = q.pop(0)
        result.append(0 if not a else 1)
        if a:
            q.append(a.left)
            q.append(a.right)
    return result


@enable_executor_hook
def generate_all_binary_trees_wrapper(executor, num_nodes):
    result = executor.run(functools.partial(generate_all_binary_trees, num_nodes))

    return sorted(map(serialize_structure, result))


if __name__ == "__main__":
    exit(
        generic_test.generic_test_main(
            "enumerate_trees.py",
            "enumerate_trees.tsv",
            generate_all_binary_trees_wrapper,
        )
    )
