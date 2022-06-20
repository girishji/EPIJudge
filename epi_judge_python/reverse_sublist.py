from typing import Optional

from list_node import ListNode
from test_framework import generic_test


def reverse_sublist(L: ListNode, start: int, finish: int) -> Optional[ListNode]:
    if start == finish:
        return L
    dh = st = ListNode(0, L)
    for _ in range(1, start):
        st = st.next
    swp = st.next
    tmp = swp.next
    for _ in range(start, finish):
        tmp2 = tmp.next
        tmp.next = swp
        swp = tmp
        tmp = tmp2

    st.next.next = tmp
    st.next = swp
    return dh.next


if __name__ == "__main__":
    exit(
        generic_test.generic_test_main(
            "reverse_sublist.py", "reverse_sublist.tsv", reverse_sublist
        )
    )
