#include <tuple>
#include <vector>

#include "test_framework/generic_test.h"
using std::vector;
void RotateMatrix(vector<vector<int>> *square_matrix_ptr) {
  auto &sm{*square_matrix_ptr};
  if (sm.size() < 2) {
    return;
  }
  auto top = std::make_tuple(0, sm.size() - 2, 0);
  auto right = std::make_tuple(0, sm.size() - 2, sm.size() - 1);
  auto bottom = std::make_tuple(sm.size() - 1, 1, sm.size() - 1);
  auto left = std::make_tuple(sm.size() - 1, 1, 0);

  vector<int> swap(sm.size(), 0);
  for (auto count = 0; count < sm.size() / 2; count++) {
    auto [cbegin, cend, row] = top;
    for (auto col = cbegin, i = 0; col <= cend; col++, i++) {
      swap[i] = sm[row][col];
    }
    {
      auto [rbegin, rend, col] = right;
      for (auto row = rbegin, i = 0; row <= rend; row++, i++) {
        std::swap(swap[i], sm[row][col]);
      }
      right = {rbegin + 1, rend - 1, col - 1};
    }
    {
      auto [cbegin, cend, row] = bottom;
      for (int col = cbegin, i = 0; col >= cend; col--, i++) {
        std::swap(swap[i], sm[row][col]);
      }
      bottom = {cbegin - 1, cend + 1, row - 1};
    }
    {
      auto [rbegin, rend, col] = left;
      for (int row = rbegin, i = 0; row >= rend; row--, i++) {
        std::swap(swap[i], sm[row][col]);
      }
      left = {rbegin - 1, rend + 1, col + 1};
    }
    {
      auto [cbegin, cend, row] = top;
      for (auto col = cbegin, i = 0; col <= cend; col++, i++) {
        std::swap(swap[i], sm[row][col]);
      }
      top = {cbegin + 1, cend - 1, row + 1};
    }
  }

  return;
}
vector<vector<int>> RotateMatrixWrapper(vector<vector<int>> square_matrix) {
  RotateMatrix(&square_matrix);
  return square_matrix;
}

int main(int argc, char *argv[]) {
  std::vector<std::string> args{argv + 1, argv + argc};
  std::vector<std::string> param_names{"square_matrix"};
  return GenericTestMain(args, "matrix_rotation.cc", "matrix_rotation.tsv",
                         &RotateMatrixWrapper, DefaultComparator{},
                         param_names);
}
