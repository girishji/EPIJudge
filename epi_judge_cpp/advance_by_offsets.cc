#include <vector>

#include "test_framework/generic_test.h"
using std::vector;

void printv(const vector<int> v) {
  for (auto e: v) {
    std::cout << " " << e;
  }
  std::cout << " " << std::endl;
}

bool CanReachEnd(const vector<int> &max_advance_steps) {
  // TODO - you fill in here.

  // printv(max_advance_steps);
  if (max_advance_steps.size() == 1) {
    return true;
  }

  auto rit = max_advance_steps.rbegin();
  while (true) {
    int step = 1;
    auto it = rit + 1;
    for (; it != max_advance_steps.rend(); it++) {
      if (*it >= step) {
        rit = it;
        break;
      }
      step++;
    }
    if (it == max_advance_steps.rend()) {
      return false;
    }
    if (rit == (max_advance_steps.rend() - 1)) {
      return true;
    }
  }
}

int main(int argc, char *argv[]) {
  std::vector<std::string> args{argv + 1, argv + argc};
  std::vector<std::string> param_names{"max_advance_steps"};
  return GenericTestMain(args, "advance_by_offsets.cc",
                         "advance_by_offsets.tsv", &CanReachEnd,
                         DefaultComparator{}, param_names);
}
