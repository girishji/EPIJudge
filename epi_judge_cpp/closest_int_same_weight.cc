#include "test_framework/generic_test.h"
unsigned long long ClosestIntSameBitCount(unsigned long long x) {
  size_t lsize{sizeof(unsigned long long) * 8};
  unsigned long long one{1};

  bool found{false};
  for (auto i = 0; i < lsize - 1; i++) {
    if (((x & (one << i)) == 0) && (x & (one << (i + 1))) > 0) {
      x |= (one << i);
      x &= ~(one << (i + 1));
      return x;
    }
    if (((x & (one << i)) > 0) && (x & (one << (i + 1))) == 0) {
      x &= ~(one << i);
      x |= (one << (i + 1));
      return x;
    }
  }
  return 0;

  // int i = 0;
  // auto y = x;
  // if (x % 2 == 0) {
  //   while ((x & 1) == 0) {
  //     x >>= 1;
  //     i++;
  //   }
  // } else {
  //   while ((x & 1) > 0) {
  //     x >>= 1;
  //     i++;
  //   }
  // }
  // // std::cout << std::bitset<32>(1 << i | 1 << (i-1)) << std::endl;
  // return y ^ (1 << i | 1 << (i - 1));
}

int main(int argc, char *argv[]) {
  std::vector<std::string> args{argv + 1, argv + argc};
  std::vector<std::string> param_names{"x"};
  return GenericTestMain(args, "closest_int_same_weight.cc",
                         "closest_int_same_weight.tsv", &ClosestIntSameBitCount,
                         DefaultComparator{}, param_names);
}
