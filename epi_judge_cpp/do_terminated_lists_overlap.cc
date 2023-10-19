#include <memory>

#include "list_node.h"
#include "test_framework/generic_test.h"
#include "test_framework/test_failure.h"
#include "test_framework/timed_executor.h"
using std::shared_ptr;

shared_ptr<ListNode<int>>
OverlappingNoCycleLists(shared_ptr<ListNode<int>> l0,
                        shared_ptr<ListNode<int>> l1) {
  auto endl0{l0}, endl1{l1};
  int len0, len1;

  for (len0 = 0; endl0 && endl0->next; endl0 = endl0->next, len0++)
    ;
  for (len1 = 0; endl1 && endl1->next; endl1 = endl1->next, len1++)
    ;
  auto advance = [](shared_ptr<ListNode<int>> &ptr, int count) {
    while (count--) {
      ptr = ptr->next;
    }
  };

  if (endl0 == endl1) {
    auto hop0{l0}, hop1{l1};
    advance(len0 > len1 ? hop0 : hop1, abs(len0 - len1));
    while (hop0 != hop1) {
      hop0 = hop0->next;
      hop1 = hop1->next;
    }
    return hop0;
  }

  return nullptr;
}
void OverlappingNoCycleListsWrapper(TimedExecutor &executor,
                                    shared_ptr<ListNode<int>> l0,
                                    shared_ptr<ListNode<int>> l1,
                                    shared_ptr<ListNode<int>> common) {
  if (common) {
    if (l0) {
      auto i = l0;
      while (i->next) {
        i = i->next;
      }
      i->next = common;
    } else {
      l0 = common;
    }

    if (l1) {
      auto i = l1;
      while (i->next) {
        i = i->next;
      }
      i->next = common;
    } else {
      l1 = common;
    }
  }

  auto result = executor.Run([&] { return OverlappingNoCycleLists(l0, l1); });

  if (result != common) {
    throw TestFailure("Invalid result");
  }
}

int main(int argc, char *argv[]) {
  std::vector<std::string> args{argv + 1, argv + argc};
  std::vector<std::string> param_names{"executor", "l0", "l1", "common"};
  return GenericTestMain(
      args, "do_terminated_lists_overlap.cc", "do_terminated_lists_overlap.tsv",
      &OverlappingNoCycleListsWrapper, DefaultComparator{}, param_names);
}
