#include "test_framework/generic_test.h"

unsigned short rev(unsigned short x) {
  for (size_t i = 0; i < 8; i++) {
    if ((x >> i & 1) != (x >> (15 - i) & 1)) {
      x ^= 1 << i;
      x ^= 1 << (15 - i);
    }
  }
  return x;
}

unsigned long long ReverseBits(unsigned long long x) {
  std::array<unsigned short, 1 << 16> reversed = {0};
  for (size_t i = 0; i < reversed.size(); i++) {
    reversed[i] = rev(i);
  }
  unsigned long long res = reversed[x & 0xffff];
  for (size_t i = 0; i < 3; i++) {
    res <<= 16;
    x >>= 16;
    res |= reversed[x & 0xffff];
  }
  return res;
}

int main(int argc, char *argv[]) {
  std::vector<std::string> args{argv + 1, argv + argc};
  std::vector<std::string> param_names{"x"};
  return GenericTestMain(args, "reverse_bits.cc", "reverse_bits.tsv",
                         &ReverseBits, DefaultComparator{}, param_names);
}
