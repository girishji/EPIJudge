#include <algorithm>
#include <vector>

#include "test_framework/generic_test.h"
using std::vector;
bool TestRowColumn(const vector<vector<int>> &partial_assignment,
                   const bool col_row = false) {
  for (auto i = 0; i < partial_assignment.size(); i++) {
    vector<bool> tester(10, false);
    for (auto j = 0; j < partial_assignment.size(); j++) {
      auto row = !col_row ? i : j;
      auto col = !col_row ? j : i;
      if (partial_assignment[row][col]) {
        if (tester[partial_assignment[row][col]]) {
          return false;
        } else {
          tester[partial_assignment[row][col]] = true;
        }
      }
    }
  }
  return true;
}

bool TestSubMatrix(const vector<vector<int>> &partial_assignment,
                   bool col_row = false) {
  for (auto i = 0; i < 3; i++) {
    auto rbegin = i * 3;
    for (auto j = 0; j < 3; j++) {
      auto cbegin = j * 3;
      vector<bool> tester(10, false);
      for (auto ri = rbegin; ri < rbegin + 3; ri++) {
        for (auto ci = cbegin; ci < cbegin + 3; ci++) {
          auto row = !col_row ? ri : ci;
          auto col = !col_row ? ci : ri;
          if (partial_assignment[row][col]) {
            if (tester[partial_assignment[row][col]]) {
              return false;
            } else {
              tester[partial_assignment[row][col]] = true;
            }
          }
        }
      }
    }
  }
  return true;
}

void printv(const vector<vector<int>> &v) {
  std::cout << std::endl;
  std::for_each(v.begin(), v.end(), [](const auto &col) {
    std::for_each(col.begin(), col.end(),
                  [](const auto &x) { std::cout << " " << x; });
    std::cout << std::endl;
  });
}

// Check if a partially filled matrix has any conflicts.
bool IsValidSudoku(const vector<vector<int>> &partial_assignment) {
  return (TestRowColumn(partial_assignment) &&
          TestRowColumn(partial_assignment, true) &&
          TestSubMatrix(partial_assignment) &&
          TestSubMatrix(partial_assignment, true));
}

int main(int argc, char *argv[]) {
  std::vector<std::string> args{argv + 1, argv + argc};
  std::vector<std::string> param_names{"partial_assignment"};
  return GenericTestMain(args, "is_valid_sudoku.cc", "is_valid_sudoku.tsv",
                         &IsValidSudoku, DefaultComparator{}, param_names);
}
