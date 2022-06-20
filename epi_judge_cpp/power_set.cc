#include <cmath>
#include <vector>

#include "test_framework/generic_test.h"
using std::vector;

vector<vector<int>> GeneratePowerSet(const vector<int> &input_set) {
  if (input_set.empty()) {
    return {{}};
  }
  vector<vector<int>> res;
  for (unsigned long long i = 0; i < pow(2, input_set.size()); i++) {
    vector<int> t;
    auto x = i;
    for (size_t j = 0; j < input_set.size(); j++) {
      if (((x >> j) & 1) > 0) {
        t.emplace(t.begin(), input_set[j]);
      }
    }
    res.emplace_back(t);
  }
  return res;
}

int main(int argc, char *argv[]) {
  std::vector<std::string> args{argv + 1, argv + argc};
  std::vector<std::string> param_names{"input_set"};
  return GenericTestMain(args, "power_set.cc", "power_set.tsv",
                         &GeneratePowerSet, UnorderedComparator{}, param_names);
}
