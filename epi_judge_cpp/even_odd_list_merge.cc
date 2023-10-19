#include "list_node.h"
#include "test_framework/generic_test.h"
shared_ptr<ListNode<int>> EvenOddMerge(const shared_ptr<ListNode<int>> &L) {
  if (L && L->next) {
    auto even{L}, odd_head{L->next}, odd{L->next};
    while (even->next) {
      even->next = even->next->next;
      if (odd->next) {
        odd->next = odd->next->next;
        even = even->next;
        odd = odd->next;
      }
    }
    even->next = odd_head;
  }
  return L;
}

int main(int argc, char *argv[]) {
  std::vector<std::string> args{argv + 1, argv + argc};
  std::vector<std::string> param_names{"L"};
  return GenericTestMain(args, "even_odd_list_merge.cc",
                         "even_odd_list_merge.tsv", &EvenOddMerge,
                         DefaultComparator{}, param_names);
}
