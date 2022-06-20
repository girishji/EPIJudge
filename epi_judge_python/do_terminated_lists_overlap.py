import functools

from list_node import ListNode
from test_framework import generic_test
from test_framework.test_failure import TestFailure
from test_framework.test_utils import enable_executor_hook


def overlapping_no_cycle_lists(l0: ListNode, l1: ListNode) -> ListNode:
    n0 = n1 = 0
    it = l0
    while it:
        n0 += 1
        it = it.next
    it = l1
    while it:
        n1 += 1
        it = it.next
    if not n0 or not n1:
        return None
    for _ in range(abs(n0 - n1)):
        if n0 > n1:
            l0 = l0.next
        else:
            l1 = l1.next
    for _ in range(min(n0, n1)):
        if l0 is l1:
            return l0
        l0 = l0.next
        l1 = l1.next

    # return ListNode()
    return None


@enable_executor_hook
def overlapping_no_cycle_lists_wrapper(executor, l0, l1, common):
    if common:
        if l0:
            i = l0
            while i.next:
                i = i.next
            i.next = common
        else:
            l0 = common

        if l1:
            i = l1
            while i.next:
                i = i.next
            i.next = common
        else:
            l1 = common

    result = executor.run(functools.partial(overlapping_no_cycle_lists, l0,
                                            l1))

    if result != common:
        raise TestFailure('Invalid result')


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('do_terminated_lists_overlap.py',
                                       'do_terminated_lists_overlap.tsv',
                                       overlapping_no_cycle_lists_wrapper))
