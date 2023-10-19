#include <algorithm>
#include <cstddef>
#include <cstdlib>
#include <string>
#include <vector>

#include "test_framework/generic_test.h"
using std::string;
using std::vector;

vector<string> GetValidIpAddress(const string &s) {
  if (s.size() > 12) {
    return {};
  }
  auto is_valid = [](const string &s) {
    return !(s.size() > 1 && s.front() == '0') && std::atoi(s.c_str()) < 256;
  };
  vector<string> result;
  for (auto i = 1; i <= 3; i++) {
    auto sub1 = s.substr(0, i);
    if (is_valid(sub1)) {
      for (auto j = 1; j <= 3 && (i + j < s.size()); j++) {
        auto sub2 = s.substr(i, j);
        if (is_valid(sub2)) {
          for (auto k = 1; k <= 3 && (i + j + k < s.size()); k++) {
            auto sub3 = s.substr(i + j, k);
            if (is_valid(sub3)) {
              auto sub4 = s.substr(i + j + k, s.size());
              if (is_valid(sub4)) {
                result.push_back(sub1 + '.' + sub2 + '.' + sub3 + '.' + sub4);
              }
            }
          }
        }
      }
    }
  }
  return result;
}

int main(int argc, char *argv[]) {
  std::vector<std::string> args{argv + 1, argv + argc};
  std::vector<std::string> param_names{"s"};
  return GenericTestMain(args, "valid_ip_addresses.cc",
                         "valid_ip_addresses.tsv", &GetValidIpAddress,
                         UnorderedComparator{}, param_names);
}
