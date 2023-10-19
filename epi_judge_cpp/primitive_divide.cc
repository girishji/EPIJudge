#include "test_framework/generic_test.h"
int Divide(int x, int y) {
  // TODO - you fill in here.
  // return 0;

  int result{0};
  while (x >= y) {
    for (auto i = 0; i < sizeof(int) * 8; ++i) {
      if (((y << i) > x) || ((y << i) < y)) {
        result += 1 << (i - 1);
        x -= (y << (i - 1));
        break;
      } 
    }
  }
  return result;
}

int main(int argc, char* argv[]) {
  std::vector<std::string> args{argv + 1, argv + argc};
  std::vector<std::string> param_names{"x", "y"};
  return GenericTestMain(args, "primitive_divide.cc", "primitive_divide.tsv",
                         &Divide, DefaultComparator{}, param_names);
}
