#include <iostream>
#include <string>

#include "test_framework/generic_test.h"
#include "test_framework/test_failure.h"
using std::string;

string IntToString(int x) {
  long xx = x;
  auto negative = (xx < 0);
  std::deque<char> num;
  xx = abs(xx);
  if (xx == 0) {
    num.push_back('0');
  }
  while (xx) {
    char digit = '0' + xx % 10;
    xx /= 10;
    num.push_front(digit);
  }
  if (negative) {
    num.push_front('-');
  }
  return string(num.begin(), num.end());

  // // bool isneg = false;
  // // if (x < 0) {
  // //   isneg = true;
  // //   x = -x;
  // // }
  // bool isneg = x < 0 ? true : false;
  // unsigned int xx = isneg ? -x : x;
  // string res;
  // do {
  //   res = static_cast<char>(xx % 10 + '0') + res;
  //   xx /= 10;
  // } while (xx > 0);
  // if (isneg) {
  //   res = '-' + res;
  // }
  // return res;
}

int StringToInt(const string &s) {
  long res = 0;
  for (auto &ch : s) {
    if (ch != '-' && ch != '+') {
      res *= 10;
      res += ch - '0';
    }
  }
  res = s.front() == '-' ? -res : res;
  return res;
}
void Wrapper(int x, const string &s) {
  if (stoi(IntToString(x)) != x) {
    throw TestFailure("Int to string conversion failed");
  }

  if (StringToInt(s) != x) {
    throw TestFailure("String to int conversion failed");
  }
}

int main(int argc, char *argv[]) {
  // string foo = IntToString(-2147483648);
  // std::cout << foo  << std::endl;
  std::vector<std::string> args{argv + 1, argv + argc};
  std::vector<std::string> param_names{"x", "s"};
  return GenericTestMain(args, "string_integer_interconversion.cc",
                         "string_integer_interconversion.tsv", &Wrapper,
                         DefaultComparator{}, param_names);
}
