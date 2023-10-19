#include <cctype>
#include <string>

#include "test_framework/generic_test.h"
#include "test_framework/test_failure.h"
using std::string;
string Decoding(const string &s) {
  int count{0};
  string result;
  for (auto i = 0; i < s.size(); i++) {
    if (std::isdigit(s[i])) {
      count = count * 10 + (s[i] - '0');
    } else {
      for (auto j = 0; j < count; j++) {
        result.push_back(s[i]);
      }
      count = 0;
    }
  }
  return result;
}
string Encoding(const string &s) {
  string result;
  char seen = s.front();
  int count = 0;
  for (auto &ch : s) {
    if (ch == seen) {
      count++;
    } else {
      result.append(std::to_string(count));
      result.push_back(seen);
      seen = ch;
      count = 1;
    }
  }
  result.append(std::to_string(count));
  result.push_back(seen);
  return result;
}
void RleTester(const string &encoded, const string &decoded) {
  if (Decoding(encoded) != decoded) {
    throw TestFailure("Decoding failed");
  }
  if (Encoding(decoded) != encoded) {
    throw TestFailure("Encoding failed");
  }
}

int main(int argc, char *argv[]) {
  std::vector<std::string> args{argv + 1, argv + argc};
  std::vector<std::string> param_names{"encoded", "decoded"};
  return GenericTestMain(args, "run_length_compression.cc",
                         "run_length_compression.tsv", &RleTester,
                         DefaultComparator{}, param_names);
}
