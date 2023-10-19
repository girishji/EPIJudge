#include <string>
#include <unordered_map>

#include "test_framework/generic_test.h"
using std::string;

string ConvertBase(const string &num_as_string, int b1, int b2) {
  if (num_as_string.empty()) {
    return "";
  }
  unsigned long num = 0;
  for (auto it = num_as_string.begin(); it != num_as_string.end(); it++) {
    if (*it != '-') {
      num *= b1;
      num += (isdigit(*it) ? *it - '0' : *it - 'A' + 10);
    }
  }
  std::deque<char> nstr;
  if (num == 0) {
    return "0";
  }
  while (num) {
    int d = num % b2;
    nstr.push_front(d > 9 ? d - 10 + 'A' : '0' + d);
    num /= b2;
  }
  if (num_as_string.front() == '-') {
    nstr.push_front('-');
  }
  return string(nstr.begin(), nstr.end());
}

int main(int argc, char *argv[]) {
  std::vector<std::string> args{argv + 1, argv + argc};
  std::vector<std::string> param_names{"num_as_string", "b1", "b2"};
  return GenericTestMain(args, "convert_base.cc", "convert_base.tsv",
                         &ConvertBase, DefaultComparator{}, param_names);
}
