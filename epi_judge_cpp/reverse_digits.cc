#include "test_framework/generic_test.h"
long long Reverse(int x) {
  // TODO - you fill in here.
  // return 0;

  bool negative{x < 0};
  x = (negative ? -x : x);
  long long result{0};
  
  while (x) {
    int quot = x % 10;
    x /= 10;
    result *= 10;
    result += quot;
  }
  return negative ? -result : result;
}

int main(int argc, char* argv[]) {
  std::vector<std::string> args{argv + 1, argv + argc};
  std::vector<std::string> param_names{"x"};
  return GenericTestMain(args, "reverse_digits.cc", "reverse_digits.tsv",
                         &Reverse, DefaultComparator{}, param_names);
}
