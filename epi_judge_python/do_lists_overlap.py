import functools
from typing import Optional

from list_node import ListNode
from test_framework import generic_test
from test_framework.test_failure import TestFailure
from test_framework.test_utils import enable_executor_hook


def cycle(head):
    its = prev = head
    if its and its.next:
        itf = head.next
        while its and itf:
            if its is itf:
                return its, prev
            prev = its
            its = its.next
            itf = itf.next
            if itf:
                itf = itf.next
    return None, None


def cycle_node(l0, l1):
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
    return None


def overlapping_lists(l0: ListNode, l1: ListNode) -> Optional[ListNode]:
    c0, p0 = cycle(l0)
    c1, p1 = cycle(l1)
    if p0:
        p0.next = None
    if p1:
        p1.next = None
    cn = cycle_node(l0, l1)
    if p0:
        p0.next = c0
    if p1:
        p1.next = c1
    return cn


@enable_executor_hook
def overlapping_lists_wrapper(executor, l0, l1, common, cycle0, cycle1):
    if common:
        if not l0:
            l0 = common
        else:
            it = l0
            while it.next:
                it = it.next
            it.next = common

        if not l1:
            l1 = common
        else:
            it = l1
            while it.next:
                it = it.next
            it.next = common

    if cycle0 != -1 and l0:
        last = l0
        while last.next:
            last = last.next
        it = l0
        for _ in range(cycle0):
            if not it:
                raise RuntimeError("Invalid input data")
            it = it.next
        last.next = it

    if cycle1 != -1 and l1:
        last = l1
        while last.next:
            last = last.next
        it = l1
        for _ in range(cycle1):
            if not it:
                raise RuntimeError("Invalid input data")
            it = it.next
        last.next = it

    common_nodes = set()
    it = common
    while it and id(it) not in common_nodes:
        common_nodes.add(id(it))
        it = it.next

    result = executor.run(functools.partial(overlapping_lists, l0, l1))

    if not (id(result) in common_nodes or (not common_nodes and not result)):
        raise TestFailure("Invalid result")


if __name__ == "__main__":
    exit(
        generic_test.generic_test_main(
            "do_lists_overlap.py", "do_lists_overlap.tsv", overlapping_lists_wrapper
        )
    )
