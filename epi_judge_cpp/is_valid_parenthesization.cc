#include <string>

#include "test_framework/generic_test.h"
using std::string;
bool IsWellFormed(const string &s) {
  std::stack<char> parens;
  for (auto &ch : s) {
    if (ch == '(' || ch == '{' || ch == '[') {
      parens.push(ch);
    } else {
      if (parens.empty()) {
        return false;
      }
      if ((ch == ')' && parens.top() != '(') ||
          (ch == '}' && parens.top() != '{') ||
          (ch == ']' && parens.top() != '[')) {
        return false;
      }
      parens.pop();
    }
  }
  return parens.empty();
}

int main(int argc, char *argv[]) {
  std::vector<std::string> args{argv + 1, argv + argc};
  std::vector<std::string> param_names{"s"};
  return GenericTestMain(args, "is_valid_parenthesization.cc",
                         "is_valid_parenthesization.tsv", &IsWellFormed,
                         DefaultComparator{}, param_names);
}
