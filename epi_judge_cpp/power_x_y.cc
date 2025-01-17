#include "test_framework/generic_test.h"
double Power(double x, int y) {
  // TODO - you fill in here.
  // return 0.0;

  double result{1.0};
  bool negative{false};

  if (y < 0) {
    negative = true;
    y = -y;
  }
  while (y) {
    // std::cout << "y"  << y << std::endl;
    if (y & 1) {
      result *= x;
    }
    y >>= 1;
    x *= x;
  }

  return negative ? 1 / result : result;
}

int main(int argc, char *argv[]) {
  std::vector<std::string> args{argv + 1, argv + argc};
  std::vector<std::string> param_names{"x", "y"};
  return GenericTestMain(args, "power_x_y.cc", "power_x_y.tsv", &Power,
                         DefaultComparator{}, param_names);
}
