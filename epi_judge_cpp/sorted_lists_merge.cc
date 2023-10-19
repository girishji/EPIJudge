#include "list_node.h"
#include "test_framework/generic_test.h"
#include <memory>
shared_ptr<ListNode<int>> MergeTwoSortedLists(shared_ptr<ListNode<int>> L1,
                                              shared_ptr<ListNode<int>> L2) {
  // auto head = L1->data < L2->data
  //                 ? std::make_shared<ListNode<int>>(L1->data, nullptr)
  //                 : std::make_shared<ListNode<int>>(L2->data, nullptr);
  auto head = std::make_shared<ListNode<int>>();
  auto tail = head;
  auto append_node = [&tail](shared_ptr<ListNode<int>> &node) {
    // tail->next = std::make_shared<ListNode<int>>(node->data);
    tail->next = node;
    node = node->next;
    tail = tail->next;
  };

  while (L1 && L2) {
    append_node(L1->data < L2->data ? L1 : L2);
  }
  tail->next = L1 ? L1 : L2;
  return head->next;
}

int main(int argc, char *argv[]) {
  std::vector<std::string> args{argv + 1, argv + argc};
  std::vector<std::string> param_names{"L1", "L2"};
  return GenericTestMain(args, "sorted_lists_merge.cc",
                         "sorted_lists_merge.tsv", &MergeTwoSortedLists,
                         DefaultComparator{}, param_names);
}
