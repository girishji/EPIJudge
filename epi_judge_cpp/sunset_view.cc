#include <iterator>
#include <vector>

#include "test_framework/generic_test.h"
using std::vector;
vector<int> ExamineBuildingsWithSunset(
    vector<int>::const_iterator sequence_begin,
    const vector<int>::const_iterator& sequence_end) {
  std::stack<int> wtoe;
  int size = 0;
  int max_height = 0;
  for (auto it = sequence_begin; it != sequence_end; it++) {
    if (*it > max_height) {
      max_height = *it;
      while (!wtoe.empty()) {
        wtoe.pop();
      }
    }
    wtoe.emplace(*it);
    size++;
  }

  max_height = 0;
  vector<int> result;
  int index = size - 1;
  while (!wtoe.empty()) {
    if (wtoe.top() > max_height) {
      max_height = wtoe.top();
      result.emplace_back(index);
    }
    wtoe.pop();
    index--;
  }
  return result;
}
vector<int> ExamineBuildingsWithSunsetWrapper(const vector<int>& sequence) {
  return ExamineBuildingsWithSunset(cbegin(sequence), cend(sequence));
}

int main(int argc, char* argv[]) {
  std::vector<std::string> args{argv + 1, argv + argc};
  std::vector<std::string> param_names{"sequence"};
  return GenericTestMain(args, "sunset_view.cc", "sunset_view.tsv",
                         &ExamineBuildingsWithSunsetWrapper,
                         DefaultComparator{}, param_names);
}
