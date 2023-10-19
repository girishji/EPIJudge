#include <algorithm>
#include <tuple>
#include <vector>

#include "test_framework/generic_test.h"
using std::vector;

void printv(const vector<int> &v) {
  std::cout << " " << std::endl;
  std::for_each(v.begin(), v.end(), [](const int x) { std::cout << " " << x; });
  std::cout << " " << std::endl;
}
vector<int> MatrixInSpiralOrder(const vector<vector<int>> &square_matrix) {
  if (square_matrix.empty()) {
    return {};
  }
  enum class Dir { right, down, left, up };
  auto right = std::make_tuple(Dir::right, 0, square_matrix.size() - 1, 0);
  auto down = std::make_tuple(Dir::down, 1, square_matrix.size() - 1,
                              square_matrix.size() - 1);
  auto left = std::make_tuple(Dir::left, square_matrix.size() - 2, 0,
                              square_matrix.size() - 1);
  auto up = std::make_tuple(Dir::up, square_matrix.size() - 2, 1, 0);

  vector<int> result;
  while (true) {
    {
      auto [d, cbegin, cend, row] = right;
      if (cbegin > cend) {
        break;
      }
      for (auto col = cbegin; col <= cend; col++) {
        result.push_back(square_matrix[row][col]);
      }
      right = {d, cbegin + 1, cend - 1, row + 1};
    }
    {
      auto [d, rbegin, rend, col] = down;
      if (rbegin > rend) {
        break;
      }
      for (auto row = rbegin; row <= rend; row++) {
        result.push_back(square_matrix[row][col]);
      }
      down = {d, rbegin + 1, rend - 1, col - 1};
    }
    {
      auto [d, cbegin, cend, row] = left;
      if (cbegin < cend) {
        break;
      }
      for (auto col = cbegin; col >= cend; col--) {
        result.push_back(square_matrix[row][col]);
        if (col == cend) {
          break;
        }
      }
      left = {d, cbegin - 1, cend + 1, row - 1};
    }
    {
      auto [d, rbegin, rend, col] = up;
      if (rbegin < rend) {
        break;
      }
      for (auto row = rbegin; row >= rend; row--) {
        result.push_back(square_matrix[row][col]);
        if (row == rend) {
          break;
        }
      }
      up = {d, rbegin - 1, rend + 1, col + 1};
    }
  }
  return result;
}

int main(int argc, char *argv[]) {
  std::vector<std::string> args{argv + 1, argv + argc};
  std::vector<std::string> param_names{"square_matrix"};
  return GenericTestMain(args, "spiral_ordering.cc", "spiral_ordering.tsv",
                         &MatrixInSpiralOrder, DefaultComparator{},
                         param_names);
}
