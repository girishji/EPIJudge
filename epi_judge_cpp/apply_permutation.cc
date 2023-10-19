#include <vector>

#include "test_framework/generic_test.h"
using std::vector;

void ApplyPermutation(vector<int> perm, vector<int>* A_ptr) {
  // TODO - you fill in here.
  auto &A {*A_ptr};

  for (auto i = 0; i < perm.size(); i++) {
    auto idx = i;
    int temp = A[idx];
    while(perm[idx] != idx) {
      std::swap(A[perm[idx]], temp);
      std::swap(idx, perm[idx]);
    }
  }
  return;
}
vector<int> ApplyPermutationWrapper(const vector<int>& perm, vector<int> A) {
  ApplyPermutation(perm, &A);
  return A;
}

int main(int argc, char* argv[]) {
  std::vector<std::string> args{argv + 1, argv + argc};
  std::vector<std::string> param_names{"perm", "A"};
  return GenericTestMain(args, "apply_permutation.cc", "apply_permutation.tsv",
                         &ApplyPermutationWrapper, DefaultComparator{},
                         param_names);
}
