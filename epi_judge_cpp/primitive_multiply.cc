#include "test_framework/generic_test.h"
unsigned long long Multiply(unsigned long long x, unsigned long long y) {
  unsigned long long result{0};
  while (y) {
    if (y & 1) {
      result += x;
    }
    y >>= 1;
    x <<= 1;
  }
  return result;
}

int main(int argc, char* argv[]) {
  std::vector<std::string> args{argv + 1, argv + argc};
  std::vector<std::string> param_names{"x", "y"};
  return GenericTestMain(args, "primitive_multiply.cc",
                         "primitive_multiply.tsv", &Multiply,
                         DefaultComparator{}, param_names);
}
