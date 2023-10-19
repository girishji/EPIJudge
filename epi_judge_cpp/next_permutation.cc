#include <__bit_reference>
#include <algorithm>
#include <limits>
#include <type_traits>
#include <vector>

#include "test_framework/generic_test.h"
using std::vector;

void printv(const vector<int> &v) {
  std::for_each_n(v.begin(), v.size(),
                  [](const int x) { std::cout << " " << x; });
  std::cout << " " << std::endl;
}
vector<int> NextPermutation(vector<int> perm) {
  size_t idx = std::numeric_limits<size_t>::max();
  for (auto i = perm.size() - 1; i > 0; i--) {
    if (perm[i - 1] < perm[i]) {
      idx = i - 1;
      break;
    }
  }
  if (idx == std::numeric_limits<size_t>::max()) {
    return {};
  }

  auto swap =
      std::find_if(perm.rbegin(), perm.rend(),
                   [&perm, &idx](const int x) { return x > perm[idx]; });
  std::swap(perm[idx], *swap);

  std::reverse(perm.begin() + idx + 1, perm.end());

  // size_t swap = perm.size() - 1;
  // for (auto i = idx + 1; i < perm.size() - 1; i++) {
  //   if (perm[i + 1] <= perm[idx]) {
  //     swap = i;
  //     break;
  //   }
  // }
  //
  // std::swap(perm[idx], perm[swap]);
  //
  // for (auto i = perm.size() - 1; i > idx + 1; i--) {
  //   if (perm[i] > perm[i - 1]) {
  //     std::swap(perm[i], perm[i - 1]);
  //   }
  // }
  // for (auto i = perm.size() - 1, j = idx + 1; i > (perm.size() + idx - 1) /
  // 2;
  //      i--, j++) {
  //   std::swap(perm[i], perm[j]);
  // }
  return perm;
}

int main(int argc, char *argv[]) {
  std::vector<std::string> args{argv + 1, argv + argc};
  std::vector<std::string> param_names{"perm"};
  return GenericTestMain(args, "next_permutation.cc", "next_permutation.tsv",
                         &NextPermutation, DefaultComparator{}, param_names);
}
