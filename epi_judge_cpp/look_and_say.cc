#include <string>

#include "test_framework/generic_test.h"
using std::string;

string LookAndSay(int n) {
  string current{"1"};
  for (auto i = 1; i < n; i++) {
    string prev(current);
    current.clear();
    char seen = prev[0];
    int count = 0;
    for (auto &ch : prev) {
      if (ch == seen) {
        count++;
      } else {
        current += std::to_string(count);
        current.push_back(seen);
        seen = ch;
        count = 1;
      }
    }
    if (count) {
      current += std::to_string(count);
      current.push_back(seen);
    }
  }
  return current;
}

int main(int argc, char *argv[]) {
  std::vector<std::string> args{argv + 1, argv + argc};
  std::vector<std::string> param_names{"n"};
  return GenericTestMain(args, "look_and_say.cc", "look_and_say.tsv",
                         &LookAndSay, DefaultComparator{}, param_names);
}
