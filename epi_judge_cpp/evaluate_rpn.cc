#include <cstdlib>
#include <set>
#include <stack>
#include <string>

#include "test_framework/generic_test.h"
using std::string;
int Evaluate(const string &expression) {
  if (expression.empty()) {
    return 0;
  }
  auto lifo = std::stack<int>();

  auto evaluate = [&lifo](const string operand) {
    auto var = lifo.top();
    lifo.pop();
    auto var2 = lifo.top();
    lifo.pop();
    switch (operand.front()) {
    case '+':
      return var2 + var;
    case '-':
      return var2 - var;
    case '/':
      return var2 / var;
    case '*':
      return var2 * var;
    }
    return -1;
  };

  auto sstream = std::stringstream(expression);
  string token;
  while (std::getline(sstream, token, ',')) {
    if (token == "+" || token == "-" || token == "*" || token == "/") {
      lifo.push(evaluate(token));
    } else {
      lifo.push(std::atoi(token.c_str()));
    }
  }
  return lifo.top();
}

int main(int argc, char *argv[]) {
  std::vector<std::string> args{argv + 1, argv + argc};
  std::vector<std::string> param_names{"expression"};
  return GenericTestMain(args, "evaluate_rpn.cc", "evaluate_rpn.tsv", &Evaluate,
                         DefaultComparator{}, param_names);
}
