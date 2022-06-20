import functools
from typing import Optional

from list_node import ListNode
from test_framework import generic_test
from test_framework.test_failure import TestFailure
from test_framework.test_utils import enable_executor_hook

def prnt(l):
    pt = l
    print()
    while pt.next:
        print(pt.data, ' ', end="")
        pt = pt.next
    print(pt.data, ' ', end="")
    print()


def list_pivoting(l: ListNode, x: int) -> Optional[ListNode]:
    if not l or not l.next:
        return l
    dummyh = ListNode(0, l)
    piv = prev = l
    while piv and piv.data != x and piv.next:
        prev = piv
        piv = piv.next
    last = piv
    while last.next:
        last = last.next
    it, it2 = l, dummyh
    while it and it.next and it is not piv:
        if it.data > x:
            it2.next = it.next
            last.next = it
            last = last.next
            last.next = None
            it = it2.next

        else:
            it2 = it
            it = it.next

    it = it2 = piv
    while it is not last and it.next:
        if it.data < x:
            it2.next = it.next
            it.next = piv
            prev.next = it
            prev = prev.next
            it = it2.next
        else:
            it2 = it
            it = it.next
    prnt(dummyh.next)
    prnt(l)
    return l 


def linked_to_list(l):
    v = list()
    while l is not None:
        v.append(l.data)
        l = l.next
    return v


@enable_executor_hook
def list_pivoting_wrapper(executor, l, x):
    original = linked_to_list(l)

    l = executor.run(functools.partial(list_pivoting, l, x))

    pivoted = linked_to_list(l)
    mode = -1
    for i in pivoted:
        if mode == -1:
            if i == x:
                mode = 0
            elif i > x:
                mode = 1
        elif mode == 0:
            if i < x:
                raise TestFailure('List is not pivoted')
            elif i > x:
                mode = 1
        else:
            if i <= x:
                raise TestFailure('List is not pivoted')

    if sorted(original) != sorted(pivoted):
        raise TestFailure('Result list contains different values')


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('pivot_list.py', 'pivot_list.tsv',
                                       list_pivoting_wrapper))
