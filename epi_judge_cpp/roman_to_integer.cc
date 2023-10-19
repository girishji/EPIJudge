#include <string>
#include <unordered_map>

#include "test_framework/generic_test.h"
using std::string;
int RomanToInteger(const string &s) {
  enum class Roman { I, V, X, L, C, D, M };
  std::unordered_map<char, Roman> cmap = {
      {'I', Roman::I}, {'V', Roman::V}, {'X', Roman::X}, {'L', Roman::L},
      {'C', Roman::C}, {'D', Roman::D}, {'M', Roman::M},
  };
  std::unordered_map<Roman, int> rmap = {
      {Roman::I, 1},   {Roman::V, 5},   {Roman::X, 10},   {Roman::L, 50},
      {Roman::C, 100}, {Roman::D, 500}, {Roman::M, 1000},
  };
  char prev = s.back();
  int result = 0;
  for (auto it = s.rbegin(); it != s.rend(); it++) {
    if (cmap[*it] < cmap[prev]) {
      result -= rmap[cmap[*it]];
    } else {
      result += rmap[cmap[*it]];
    }
    prev = *it;
  }
  return result;
}

int main(int argc, char *argv[]) {
  std::vector<std::string> args{argv + 1, argv + argc};
  std::vector<std::string> param_names{"s"};
  return GenericTestMain(args, "roman_to_integer.cc", "roman_to_integer.tsv",
                         &RomanToInteger, DefaultComparator{}, param_names);
}
