#include "test_framework/generic_test.h"
short Parity(unsigned long long x) {
  std::array<short, 1 << 8> tester = {0};
  for (size_t i = 0; i < tester.size(); i++) {
    auto temp = i;
    short p = 0;
    while (temp > 0) {
      p += (temp & 1) > 0 ? 1 : 0;
      temp >>= 1;
    }
    tester[i] = p % 2 == 0 ? 0 : 1;
  }
  short mask = 0xff;
  short par = 0;
  do {
    par += tester[x & mask];
    x >>= 8;
  } while (x > 0);
  return par % 2 == 0 ? 0 : 1;
}

int main(int argc, char *argv[]) {
  std::vector<std::string> args{argv + 1, argv + argc};
  std::vector<std::string> param_names{"x"};
  return GenericTestMain(args, "parity.cc", "parity.tsv", &Parity,
                         DefaultComparator{}, param_names);
}
