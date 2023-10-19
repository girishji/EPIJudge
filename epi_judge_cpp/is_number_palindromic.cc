#include "test_framework/generic_test.h"
bool IsPalindromeNumber(int x) {
  // TODO - you fill in here.
  // return true;

  if (x < 0) {
    return false;
  }

  long long reversed{0};
  int temp{x};
  while (x) {
    reversed *= 10;
    reversed += (x % 10);
    x /= 10;
  }
  return (reversed == temp) ? true : false;
}

int main(int argc, char *argv[]) {
  std::vector<std::string> args{argv + 1, argv + argc};
  std::vector<std::string> param_names{"x"};
  return GenericTestMain(args, "is_number_palindromic.cc",
                         "is_number_palindromic.tsv", &IsPalindromeNumber,
                         DefaultComparator{}, param_names);
}
