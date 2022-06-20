#include "test_framework/generic_test.h"
long long SwapBits(long long x, int i, int j) {
  if (i == j) {
    return x;
  }
  long long one = 1;
  short ib = (x >> i) & one;
  short jb = (x >> j) & one;
  // std::cout << std::bitset<64>(x) << std::endl;
  if (ib != jb) {
    x ^= one << i;
    x ^= one << j;
  }
  return x;
}

int main(int argc, char *argv[]) {
  std::vector<std::string> args{argv + 1, argv + argc};
  std::vector<std::string> param_names{"x", "i", "j"};
  return GenericTestMain(args, "swap_bits.cc", "swap_bits.tsv", &SwapBits,
                         DefaultComparator{}, param_names);
}
