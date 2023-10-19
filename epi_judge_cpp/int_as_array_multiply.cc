#include <algorithm>
#include <vector>

#include "test_framework/generic_test.h"
using std::vector;

void add_digits(vector<int> &result, const vector<int> &p) {
  auto itr = result.rbegin();
  auto itp = p.rbegin();
  int carry{0};
  while ((itr != result.rend()) && (itp != p.rend())) {
    auto digit = *itr + *itp + carry;
    *itr = digit % 10;
    carry = digit / 10;
    itr++;
    itp++;
  }
  while (itr != result.rend()) {
    auto digit = *itr + carry;
    *itr = digit % 10;
    carry = digit / 10;
    itr++;
  }
  while (itp != p.rend()) {
    auto digit = *itp + carry;
    result.insert(result.begin(), digit % 10);
    carry = digit / 10;
    itp++;
  }
  if (carry) {
    result.insert(result.begin(), carry);
  }
}

void print_digits(const vector<int> &vec) {
  for (auto &elem : vec) {
    std::cout << " " << elem;
  }
  std::cout << " " << std::endl;
}

vector<int> Multiply(vector<int> num1, vector<int> num2) {
  // TODO - you fill in here.
  // return {};

  if (((num1.size() == 1) && (num1.front() == 0)) ||
      ((num2.size() == 1) && (num2.front() == 0))) {
    return {0};
  }

  // std::cout << "num1:" << std::endl;
  // print_digits(num1);
  // std::cout << "num2:" << std::endl;
  // print_digits(num2);
  bool negative = (num1.front() < 0 && num2.front() > 0) ||
                  (num1.front() > 0 && num2.front() < 0);
  if (num1.front() < 0) {
    num1.front() = -num1.front();
  }
  if (num2.front() < 0) {
    num2.front() = -num2.front();
  }

  vector<int> result;

  auto base{0};
  for (auto it1 = num1.rbegin(); it1 != num1.rend(); it1++) {
    int reminder{0};
    vector<int> product;
    for (auto it2 = num2.rbegin(); it2 != num2.rend(); it2++) {
      int mult = *it1 * *it2 + reminder;
      product.insert(product.begin(), mult % 10);
      reminder = mult / 10;
    }
    if (reminder) {
      product.insert(product.begin(), reminder);
    }
    if (base == 0) {
      result = product;
      // print_digits(result);
    } else {
      for (auto i = 0; i < base; i++) {
        product.push_back(0);
      }
      // print_digits(product);
      add_digits(result, product);
      // print_digits(result);
    }
    base++;
  }
  if (negative) {
    result.front() = -result.front();
  }
  return result;
}

int main(int argc, char *argv[]) {
  std::vector<std::string> args{argv + 1, argv + argc};
  std::vector<std::string> param_names{"num1", "num2"};
  return GenericTestMain(args, "int_as_array_multiply.cc",
                         "int_as_array_multiply.tsv", &Multiply,
                         DefaultComparator{}, param_names);
}
