#include <string>
#include <iostream>

#include "test_framework/generic_test.h"
#include "test_framework/test_failure.h"
using std::string;

string IntToString(int x) {
  // bool isneg = false;
  // if (x < 0) {
  //   isneg = true;
  //   x = -x;
  // }
  bool isneg = x < 0 ? true : false;
  unsigned int xx = isneg ? -x : x;
  string res;
  do {
    res = static_cast<char>(xx % 10 + '0') + res;
    xx /= 10;
  } while (xx > 0);  
  if (isneg) {
    res = '-' + res;
  }
  return res;
}

int StringToInt(const string& s) {
  bool isneg = false;
  int res = 0;
  // for (size_t i = s.size() - 1; i >= 0; i--) {
  for (size_t i = 0; i < s.size(); i++) {
    if (isdigit(s[i])) {
      res *= 10;
      res += static_cast<int>(s[i] - '0');
    } else if (s[i] == '-' && i == 0) {
      isneg = true;
    } else {

    }
  }
  if (isneg) {
    res = -res;
  }
  return res;
}
void Wrapper(int x, const string& s) {
  if (stoi(IntToString(x)) != x) {
    throw TestFailure("Int to string conversion failed");
  }

  if (StringToInt(s) != x) {
    throw TestFailure("String to int conversion failed");
  }
}

int main(int argc, char* argv[]) {
// string foo = IntToString(-2147483648);
// std::cout << foo  << std::endl;
  std::vector<std::string> args{argv + 1, argv + argc};
  std::vector<std::string> param_names{"x", "s"};
  return GenericTestMain(args, "string_integer_interconversion.cc",
                         "string_integer_interconversion.tsv", &Wrapper,
                         DefaultComparator{}, param_names);
}
