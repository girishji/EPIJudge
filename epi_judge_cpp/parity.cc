#include "test_framework/generic_test.h"
short Parity(unsigned long long x) {
  static std::array<unsigned short, 1 << 8> parity_val{0};
  static bool parity_calculated = false;
  if (!parity_calculated) {
    for (unsigned short i = 0; i < 1 << 8; ++i) {
      short bit_count = 0;
      unsigned short n = i;
      while (n) {
        bit_count += n & 1;
        n >>= 1;
      }
      parity_val[i] = (bit_count % 2 == 0) ? 0 : 1;
    }
  }

  short parity = 0;
  for (int i = 0; i < 8; ++i) {
    parity += parity_val[x & 0xff];
    x >>= 8;
  }
  return (parity % 2 == 0) ? 0 : 1;

  // std::array<short, 1 << 8> tester = {0};
  // for (size_t i = 0; i < tester.size(); i++) {
  //   auto temp = i;
  //   short p = 0;
  //   while (temp > 0) {
  //     p += (temp & 1) > 0 ? 1 : 0;
  //     temp >>= 1;
  //   }
  //   tester[i] = p % 2 == 0 ? 0 : 1;
  // }
  // short mask = 0xff;
  // short par = 0;
  // do {
  //   par += tester[x & mask];
  //   x >>= 8;
  // } while (x > 0);
  // return par % 2 == 0 ? 0 : 1;
}

int main(int argc, char *argv[]) {
  std::vector<std::string> args{argv + 1, argv + argc};
  std::vector<std::string> param_names{"x"};
  return GenericTestMain(args, "parity.cc", "parity.tsv", &Parity,
                         DefaultComparator{}, param_names);
}
