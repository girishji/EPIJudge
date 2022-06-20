from typing import Optional

from list_node import ListNode
from test_framework import generic_test


def add_two_numbers(L1: ListNode, L2: ListNode) -> Optional[ListNode]:
    if not L1 and not L2:
        return None
    if not L1:
        return L2
    if not L2:
        return L1
    it = result = ListNode(0, None)
    carry = 0
    while L1 and L2: 
        r = carry + L1.data + L2.data
        carry = r // 10
        it.next = ListNode(r % 10, None)
        it = it.next
        L1 = L1.next
        L2 = L2.next
    while L1:
        r = carry + L1.data
        carry = r // 10
        it.next = ListNode(r % 10, None)
        it = it.next
        L1 = L1.next
    while L2:
        r = carry + L2.data
        carry = r // 10
        it.next = ListNode(r % 10, None)
        it = it.next
        L2 = L2.next
    if carry:
        it.next = ListNode(carry, None)

    return result.next


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('int_as_list_add.py',
                                       'int_as_list_add.tsv', add_two_numbers))
