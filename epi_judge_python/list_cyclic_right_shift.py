from typing import Optional

from list_node import ListNode
from test_framework import generic_test


def cyclically_right_shift_list(L: ListNode, k: int) -> Optional[ListNode]:
    if not L:
        return None
    it2 = it1 = L
    length = 0
    while it1:
        length += 1
        it1 = it1.next 
    it1 = L
    for _ in range(k % length):
        it2 = it2.next
    if it1 is it2:
        return L
    while it2.next:
        it1 = it1.next
        it2 = it2.next
    st = it1.next
    it1.next = None
    it2.next = L
    return st

if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('list_cyclic_right_shift.py',
                                       'list_cyclic_right_shift.tsv',
                                       cyclically_right_shift_list))
