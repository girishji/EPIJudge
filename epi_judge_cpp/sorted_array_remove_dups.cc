#include <algorithm>
#include <limits>
#include <vector>

#include "test_framework/generic_test.h"
#include "test_framework/timed_executor.h"
using std::vector;
// Returns the number of valid entries after deletion.
int DeleteDuplicates(vector<int> *A_ptr) {
  // TODO - you fill in here.
  // return 0;

  auto &A{*A_ptr};
  // std::for_each(A.begin(), A.end(), [](const int n){std::cout << " " << n;});
  // std::cout << " " << std::endl;
  if (!A.size()) {
    return 0;
  }

  int prev = std::numeric_limits<int>::min();
  int count = 1;
  for (auto &elem : A) {
    if (prev == std::numeric_limits<int>::min()) {
      prev = elem;
    } else {
      if (elem > prev) {
        count++;
        prev = elem;
      }
    }
  }
  prev = A[0];
  // std::cout << "count " << count << std::endl;
  for (auto i = 1; i < count; i++) {
    if (A[i] <= prev) {
      // swap
      // std::cout << "swap Ai " << A[i] << std::endl;
      for (auto j = i + 1; j < A.size(); j++) {
        if (A[j] > prev) {
          // std::cout << "swap " << A[i] << " " << A[j] << std::endl;
          std::swap(A[j], A[i]);
          break;
        }
      }
    }
    prev = A[i];
  }
  return count;
}

vector<int> DeleteDuplicatesWrapper(TimedExecutor &executor, vector<int> A) {
  int end = executor.Run([&] { return DeleteDuplicates(&A); });
  A.resize(end);
  return A;
}

int main(int argc, char *argv[]) {
  std::vector<std::string> args{argv + 1, argv + argc};
  std::vector<std::string> param_names{"executor", "A"};
  return GenericTestMain(
      args, "sorted_array_remove_dups.cc", "sorted_array_remove_dups.tsv",
      &DeleteDuplicatesWrapper, DefaultComparator{}, param_names);
}
