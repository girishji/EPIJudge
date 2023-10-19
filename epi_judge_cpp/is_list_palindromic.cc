#include "list_node.h"
#include "test_framework/generic_test.h"

shared_ptr<ListNode<int>> Reversed(shared_ptr<ListNode<int>> st,
                                   shared_ptr<ListNode<int>> en) {
  if (st != en) {
    auto left{st}, middle{st->next}, right{st->next->next};
    while (middle != en) {
      middle->next = left;
      left = middle;
      middle = right;
      right = right->next;
    }
    middle->next = left;
  }
  st->next.reset();
  return en;
}

bool Palindrome(shared_ptr<ListNode<int>> left,
                shared_ptr<ListNode<int>> right) {
  while (left) {
    if (left->data != right->data) {
      return false;
    }
    left = left->next;
    right = right->next;
  }
  return true;
}

bool IsLinkedListAPalindrome(shared_ptr<ListNode<int>> L) {
  int count = 0;
  for (auto ptr{L}; ptr; ptr = ptr->next) {
    count++;
  }
  if (auto half = count / 2) {
    auto en{L};
    while (--half) {
      en = en->next;
    }
    auto right = count % 2 == 0 ? en->next : en->next->next;
    auto left = Reversed(L, en);

    return Palindrome(left, right);
  }
  return true;
}

int main(int argc, char *argv[]) {
  std::vector<std::string> args{argv + 1, argv + argc};
  std::vector<std::string> param_names{"L"};
  return GenericTestMain(args, "is_list_palindromic.cc",
                         "is_list_palindromic.tsv", &IsLinkedListAPalindrome,
                         DefaultComparator{}, param_names);
}
