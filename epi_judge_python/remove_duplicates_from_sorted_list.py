from typing import Optional

from list_node import ListNode
from test_framework import generic_test


def remove_duplicates(L: ListNode) -> Optional[ListNode]:
    it1 = L
    if L and L.next:
        it2 = L.next
        while it2:
            if it1.data == it2.data:
                it1.next = it2.next
            else:
                it1 = it2
            it2 = it2.next

    return L


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            'remove_duplicates_from_sorted_list.py',
            'remove_duplicates_from_sorted_list.tsv', remove_duplicates))
