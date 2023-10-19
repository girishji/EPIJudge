#include <algorithm>
#include <vector>

#include "test_framework/generic_test.h"
using std::vector;
double BuyAndSellStockOnce(const vector<double> &prices) {
  // TODO - you fill in here.
  // return 0.0;
  double profit{0.0}, sell{prices.back()};

  for (auto rit = prices.rbegin(); rit != prices.rend(); rit++) {
    if (*rit > sell) {
      sell = *rit;
      continue;
    }
    profit = std::max(profit, sell - *rit);
  }
  return profit;
}

int main(int argc, char *argv[]) {
  std::vector<std::string> args{argv + 1, argv + argc};
  std::vector<std::string> param_names{"prices"};
  return GenericTestMain(args, "buy_and_sell_stock.cc",
                         "buy_and_sell_stock.tsv", &BuyAndSellStockOnce,
                         DefaultComparator{}, param_names);
}
