#include "list_node.h"
#include "test_framework/generic_test.h"
#include <memory>

shared_ptr<ListNode<int>> AddTwoNumbers(shared_ptr<ListNode<int>> L1,
                                        shared_ptr<ListNode<int>> L2) {
  auto l{L1}, r{L2};
  auto dummy = std::make_shared<ListNode<int>>(), tail{dummy};

  int carry = 0;
  auto append = [&tail, &carry](int sum) {
    carry = sum / 10;
    tail->next = std::make_shared<ListNode<int>>(sum % 10);
    tail = tail->next;
  };

  while (l || r) {
    append(carry + (l ? l->data : 0) + (r ? r->data : 0));
    if (l) {
      l = l->next;
    }
    if (r) {
      r = r->next;
    }
  }
  if (carry) {
    append(carry);
  }
  return dummy->next;
}

int main(int argc, char* argv[]) {
  std::vector<std::string> args{argv + 1, argv + argc};
  std::vector<std::string> param_names{"L1", "L2"};
  return GenericTestMain(args, "int_as_list_add.cc", "int_as_list_add.tsv",
                         &AddTwoNumbers, DefaultComparator{}, param_names);
}
