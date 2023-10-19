#include <algorithm>
#include <vector>

#include "test_framework/generic_test.h"
using std::vector;

template <typename St, typename En> double BuyAndSellStock(St start, En end) {
  double profit{0.0}, buy{*start};
  for (auto it = start; it != end; it++) {
    if (*it < buy) {
      buy = *it;
    } else {
      profit = std::max(profit, *it - buy);
    }
  }
  return profit;
}

double BuyAndSellStockTwice(const vector<double> &prices) {
  // TODO - you fill in here.

  double profit{0.0}, buy{prices.front()}, sell{prices.front()};
  for (auto it = prices.begin(); it != prices.end(); it++) {
    profit = std::max(profit, BuyAndSellStock(prices.begin(), it + 1) +
                                  BuyAndSellStock(it, prices.end()));
  }
  return profit;
}

int main(int argc, char *argv[]) {
  std::vector<std::string> args{argv + 1, argv + argc};
  std::vector<std::string> param_names{"prices"};
  return GenericTestMain(args, "buy_and_sell_stock_twice.cc",
                         "buy_and_sell_stock_twice.tsv", &BuyAndSellStockTwice,
                         DefaultComparator{}, param_names);
}
