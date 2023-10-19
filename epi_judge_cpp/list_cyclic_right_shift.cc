#include <memory>

#include "list_node.h"
#include "test_framework/generic_test.h"
using std::shared_ptr;

shared_ptr<ListNode<int>> CyclicallyRightShiftList(shared_ptr<ListNode<int>> L,
                                                   int k) {
  auto dummy = std::make_shared<ListNode<int>>(0, L);
  auto shifter{dummy};
  if (L && k) {
    int count{0};
    while (shifter->next) {
      shifter = shifter->next;
      count++;
    }
    auto rotation = count - (k % count);
    if (rotation < count) {
      shifter = dummy;
      while (rotation--) {
        shifter = shifter->next;
      }
      auto temp{L};
      L = shifter->next;
      shifter->next.reset();
      shifter = L;
      while (shifter->next) {
        shifter = shifter->next;
      }
      shifter->next = temp;
    }
  }
  return L;
}

int main(int argc, char *argv[]) {
  std::vector<std::string> args{argv + 1, argv + argc};
  std::vector<std::string> param_names{"L", "k"};
  return GenericTestMain(
      args, "list_cyclic_right_shift.cc", "list_cyclic_right_shift.tsv",
      &CyclicallyRightShiftList, DefaultComparator{}, param_names);
}
