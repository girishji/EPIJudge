#include "list_node.h"
#include "test_framework/generic_test.h"
#include <memory>

shared_ptr<ListNode<int>> ReverseSublist(shared_ptr<ListNode<int>> L, int start,
                                         int finish) {

  auto dummy_head = std::make_shared<ListNode<int>>(0, L);
  auto pstart{dummy_head}, pfinish{L};
  for (; start > 1; start--, pstart = pstart->next)
    ;
  for (; finish > 1; finish--, pfinish = pfinish->next)
    ;

  auto temp = pstart->next;
  pstart->next = pfinish;
  pstart = temp->next;
  temp->next = pfinish->next;
  for (; pstart != pfinish; pstart = pstart->next) {
    auto lead = pstart->next;
    pstart->next = 

  }

  // if (finish <= start || !L) {
  //   return L;
  // }
  // auto start_p{L}, finish_p{L}, follow{L};
  // for (auto i = 1; i < start; i++) {
  //   if (i != 1) {
  //     follow = start_p;
  //   }
  //   start_p = start_p->next;
  // }
  // for (; finish > 1; finish--, finish_p = finish_p->next)
  //   ;
  //
  // bool first_node_reversed = false;
  // if (follow != start_p) {
  //   auto temp = finish_p->next;
  //   follow->next = finish_p;
  //   follow = start_p->next;
  //   start_p->next = temp;
  // } else {
  //   auto temp = finish_p->next;
  //   follow = start_p->next;
  //   start_p->next = temp;
  //   first_node_reversed = true;
  // }
  // while (follow != finish_p) {
  //   auto temp = follow;
  //   follow = follow->next;
  //   temp->next = start_p;
  //   start_p = temp;
  // }
  // follow->next = start_p;
  // return first_node_reversed ? follow : L;
}

int main(int argc, char *argv[]) {
  std::vector<std::string> args{argv + 1, argv + argc};
  std::vector<std::string> param_names{"L", "start", "finish"};
  return GenericTestMain(args, "reverse_sublist.cc", "reverse_sublist.tsv",
                         &ReverseSublist, DefaultComparator{}, param_names);
}
