from list_node import ListNode
from test_framework import generic_test


def is_linked_list_a_palindrome(L: ListNode) -> bool:
    if not L or not L.next:
        return True
    sl = fa = L
    while fa and fa.next and fa.next.next:
        sl = sl.next
        fa = fa.next.next
    sec = sl.next
    rev = L
    t = rev.next
    rev.next = None
    while rev is not sl:
        t2 = t.next
        t.next = rev
        rev = t
        t = t2
    if not fa.next:
        sl = sl.next
    while sl and sec:
        if sec.data != sl.data:
            return False
        sl = sl.next
        sec = sec.next
    return True


if __name__ == "__main__":
    exit(
        generic_test.generic_test_main(
            "is_list_palindromic.py",
            "is_list_palindromic.tsv",
            is_linked_list_a_palindrome,
        )
    )
