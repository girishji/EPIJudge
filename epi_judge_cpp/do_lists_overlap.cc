#include <set>
#include <stdexcept>

#include "list_node.h"
#include "test_framework/generic_test.h"
#include "test_framework/test_failure.h"
#include "test_framework/timed_executor.h"

shared_ptr<ListNode<int>> CycleNode(shared_ptr<ListNode<int>> head) {
  auto slow{head}, fast{head};

  while (fast && fast->next) {
    slow = slow->next;
    fast = fast->next->next;

    if (slow == fast) {
      int clen = 0;
      do {
        clen++;
        slow = slow->next;
      } while (slow != fast);

      auto front = head;
      while (clen--) {
        front = front->next;
      }

      auto back = head;
      while (front != back) {
        front = front->next;
        back = back->next;
      }
      return front;
    }
  }
  while (slow->next) {
    slow = slow->next;
  }
  return slow;
}

shared_ptr<ListNode<int>> OverlappingLists(shared_ptr<ListNode<int>> l0,
                                           shared_ptr<ListNode<int>> l1) {
  if (!l0 || !l1) {
    return nullptr;
  }
  auto cycle0 = CycleNode(l0);
  auto cycle1 = CycleNode(l1);
  if (cycle0->next && cycle1->next) {
    bool overlap = cycle0 == cycle1 ? true : false;
    if (!overlap) {
      for (auto ptr = cycle0->next; ptr != cycle0; ptr = ptr->next) {
        if (ptr == cycle1) {
          overlap = true;
        }
      }
    }
    return overlap ? cycle0 : nullptr;
  }

  auto Count = [](shared_ptr<ListNode<int>> p) {
    int count = 0;
    while (p->next) {
      count++;
      p = p->next;
    }
    return count;
  };

  auto AdvancePtr = [](shared_ptr<ListNode<int>> &p, int count) {
    while (count--) {
      p = p->next;
    }
  };

  if (!cycle0->next && !cycle1->next) {
    if (cycle0 == cycle1) {
      int count0 = Count(l0);
      int count1 = Count(l1);
      AdvancePtr(count0 > count1 ? l0 : l1, abs(count0 - count1));
      while (l0 != l1) {
        l0 = l0->next;
        l1 = l1->next;
      }
      return l0;
    }
  }
  return nullptr;
}
void OverlappingListsWrapper(TimedExecutor &executor,
                             shared_ptr<ListNode<int>> l0,
                             shared_ptr<ListNode<int>> l1,
                             shared_ptr<ListNode<int>> common, int cycle0,
                             int cycle1) {
  if (common) {
    if (!l0) {
      l0 = common;
    } else {
      auto it = l0;
      while (it->next) {
        it = it->next;
      }
      it->next = common;
    }

    if (!l1) {
      l1 = common;
    } else {
      auto it = l1;
      while (it->next) {
        it = it->next;
      }
      it->next = common;
    }
  }

  if (cycle0 != -1 && l0) {
    auto last = l0;
    while (last->next) {
      last = last->next;
    }
    auto it = l0;
    while (cycle0-- > 0) {
      if (!it) {
        throw std::runtime_error("Invalid input data");
      }
      it = it->next;
    }
    last->next = it;
  }

  if (cycle1 != -1 && l1) {
    auto last = l1;
    while (last->next) {
      last = last->next;
    }
    auto it = l1;
    while (cycle1-- > 0) {
      if (!it) {
        throw std::runtime_error("Invalid input data");
      }
      it = it->next;
    }
    last->next = it;
  }

  std::set<shared_ptr<ListNode<int>>> common_nodes;
  auto it = common;
  while (it && common_nodes.count(it) == 0) {
    common_nodes.insert(it);
    it = it->next;
  }

  auto result = executor.Run([&] { return OverlappingLists(l0, l1); });

  if (!((common_nodes.empty() && result == nullptr) ||
        common_nodes.count(result) > 0)) {
    throw TestFailure("Invalid result");
  }
}

int main(int argc, char *argv[]) {
  std::vector<std::string> args{argv + 1, argv + argc};
  std::vector<std::string> param_names{"executor", "l0",     "l1",
                                       "common",   "cycle0", "cycle1"};
  return GenericTestMain(args, "do_lists_overlap.cc", "do_lists_overlap.tsv",
                         &OverlappingListsWrapper, DefaultComparator{},
                         param_names);
}
