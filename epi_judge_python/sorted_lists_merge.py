from typing import Optional

from list_node import ListNode
from test_framework import generic_test


def merge_two_sorted_lists(
    L1: Optional[ListNode], L2: Optional[ListNode]
) -> Optional[ListNode]:
    if not L1 and not L2:
        return None
    if not L1:
        return L2
    elif not L2:
        return L1
    else:
        if L1.data < L2.data:
            head = sm = L1
            lr = L2
        else:
            head = sm = L2
            lr = L1
    while sm and lr:
        while sm.next and sm.data == sm.next.data:
            sm = sm.next
        while sm.next and sm.next.data <= lr.data:
            sm = sm.next
        tmp = sm.next
        sm.next, lr = lr, tmp
        sm = sm.next
    return head


if __name__ == "__main__":
    exit(
        generic_test.generic_test_main(
            "sorted_lists_merge.py", "sorted_lists_merge.tsv", merge_two_sorted_lists
        )
    )
