#include <algorithm>
#include <cctype>
#include <string>

#include "test_framework/generic_test.h"
using std::string;

// Returns the index of the first character of the substring if found, -1
// otherwise.
int RabinKarp(const string &t, const string &s) {
  if (t.size() < s.size()) {
    return -1;
  }
  unsigned long hash{0}, running{0};
  int hsize = std::min<unsigned long>(12, s.size());
  for (auto i = 0; i < hsize; i++) {
    hash = hash * 26 + (std::tolower(s[i]) - 'a');
    running = running * 26 + (std::tolower(t[i]) - 'a');
  }

  for (auto i = 0; i < (t.size() - hsize + 1); i++) {
    if (hash == running) {
      bool match = true;
      for (auto j = 0; j < s.size(); j++) {
        if (s[j] != t[i + j]) {
          match = false;
        }
      }
      if (match) {
        return i;
      }
    }
    running -= pow(26, hsize - 1) * (std::tolower(t[i]) - 'a');
    if (i < t.size() - hsize) {
      running = running * 26 + (std::tolower(t[i + hsize]) - 'a');
    }
  }

  return -1;
}

int main(int argc, char *argv[]) {
  std::vector<std::string> args{argv + 1, argv + argc};
  std::vector<std::string> param_names{"t", "s"};
  return GenericTestMain(args, "substring_match.cc", "substring_match.tsv",
                         &RabinKarp, DefaultComparator{}, param_names);
}
