from typing import Optional

from list_node import ListNode
from test_framework import generic_test


def even_odd_merge(L: ListNode) -> Optional[ListNode]:
    ev = L
    if L and L.next:
        l2 = od = L.next
    else:
        return L
    while ev.next and od.next:
        ev.next = od.next
        ev = ev.next
        od.next = ev.next
        od = od.next if od.next else od
    ev.next = l2
    od.next = None
    return L


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('even_odd_list_merge.py',
                                       'even_odd_list_merge.tsv',
                                       even_odd_merge))
