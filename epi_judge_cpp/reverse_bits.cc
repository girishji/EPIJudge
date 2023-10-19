#include "test_framework/generic_test.h"
#include <bitset>
#include <ranges>

// unsigned short rev(unsigned short x) {
//   for (size_t i = 0; i < 8; i++) {
//     if ((x >> i & 1) != (x >> (15 - i) & 1)) {
//       x ^= 1 << i;
//       x ^= 1 << (15 - i);
//     }
//   }
//   return x;
// }

unsigned long long ReverseBits(unsigned long long x) {
  // using namespace std::ranges;

  // std::vector<int> const vec{1, 2, 3, 4, 5, 6, 7, 8, 9, 10};
  //
  // for (auto &i : std::views::reverse(vec)) {
  //   std::cout << i << ",";
  // }

  size_t lsize = sizeof(unsigned long long) * 8;
  for (size_t n = 0; n < lsize / 2; ++n) {
    size_t i{n}, j{lsize - n - 1};
    unsigned long long one = 1;
    if (((x >> i) & 1) != ((x >> j) & 1)) {
      x ^= (one << i);
      x ^= (one << j);
    }
  }
  return x;

  // std::array<unsigned short, 1 << 16> reversed = {0};
  // for (size_t i = 0; i < reversed.size(); i++) {
  //   reversed[i] = rev(i);
  // }
  // unsigned long long res = reversed[x & 0xffff];
  // for (size_t i = 0; i < 3; i++) {
  //   res <<= 16;
  //   x >>= 16;
  //   res |= reversed[x & 0xffff];
  // }
  // return res;
}

int main(int argc, char *argv[]) {
  std::vector<std::string> args{argv + 1, argv + argc};
  std::vector<std::string> param_names{"x"};
  return GenericTestMain(args, "reverse_bits.cc", "reverse_bits.tsv",
                         &ReverseBits, DefaultComparator{}, param_names);
}
