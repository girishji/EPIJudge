#include <_ctype.h>
#include <iterator>
#include <string>

#include "test_framework/generic_test.h"
using std::string;
bool IsPalindrome(const string& s) {
  if (s.empty() || s.size() == 1) {
    return true;
  }
  auto fi = s.begin();
  auto bi = s.rbegin();
  while (std::distance(s.begin(), fi) + std::distance(s.rbegin(), bi) <= s.size()) {
    while (!isalnum(*fi)) {
      fi++;
    }
    while (!isalnum(*bi)) {
      bi++;
    }
    if (toupper(*fi) != toupper(*bi)) {
      return false;
    }
    fi++;
    bi++;
  }
  return true;
}

int main(int argc, char* argv[]) {
  std::vector<std::string> args{argv + 1, argv + argc};
  std::vector<std::string> param_names{"s"};
  return GenericTestMain(args, "is_string_palindromic_punctuation.cc",
                         "is_string_palindromic_punctuation.tsv", &IsPalindrome,
                         DefaultComparator{}, param_names);
}
