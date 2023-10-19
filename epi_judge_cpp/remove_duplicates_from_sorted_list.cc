#include <memory>

#include "list_node.h"
#include "test_framework/generic_test.h"
using std::shared_ptr;

shared_ptr<ListNode<int>> RemoveDuplicates(const shared_ptr<ListNode<int>> &L) {
  if (L && L->next) {
    auto fr{L->next}, ba{L};
    while (fr) {
      if (fr->data == ba->data) {
        ba->next = fr->next;
        auto t = fr;
        fr = fr->next;
        t.reset();
      } else {
        fr = fr->next;
        ba = ba->next;
      }
    }
  }
  return L;
}

int main(int argc, char *argv[]) {
  std::vector<std::string> args{argv + 1, argv + argc};
  std::vector<std::string> param_names{"L"};
  return GenericTestMain(args, "remove_duplicates_from_sorted_list.cc",
                         "remove_duplicates_from_sorted_list.tsv",
                         &RemoveDuplicates, DefaultComparator{}, param_names);
}
