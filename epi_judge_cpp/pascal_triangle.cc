#include <vector>

#include "test_framework/generic_test.h"
using std::vector;
vector<vector<int>> GeneratePascalTriangle(int num_rows) {
  if (num_rows == 0) {
    return {};
  }
  vector<vector<int>> pascal;
  pascal.push_back({1});
  for (auto i = 1; i < num_rows; i++) {
    auto &prev = pascal.back();
    vector<int> row;
    row.emplace_back(prev[0]);
    for (auto it = prev.begin(); it != prev.end() - 1; it++) {
      row.emplace_back(*it + *(it + 1));
    }
    row.emplace_back(prev[0]);
    pascal.push_back(row);
  }

  return pascal;
}

int main(int argc, char *argv[]) {
  std::vector<std::string> args{argv + 1, argv + argc};
  std::vector<std::string> param_names{"num_rows"};
  return GenericTestMain(args, "pascal_triangle.cc", "pascal_triangle.tsv",
                         &GeneratePascalTriangle, DefaultComparator{},
                         param_names);
}
