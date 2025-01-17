#include <algorithm>
#include <bitset>
#include <deque>
#include <vector>

#include "test_framework/generic_test.h"
using std::vector;
// Given n, return all primes up to and including n.
vector<int> GeneratePrimes(int n) {
  // TODO - you fill in here.
  // return {};

  if (n < 2) {
    return {};
  }
  std::deque<bool> sieve(n + 1, true);
  sieve[0] = sieve[1] = false;
  for (auto i = 0; i <= n; i++) {
    if (sieve[i]) {
      for (auto j = i + 1; j <= n; j++) {
        if (sieve[j] && (j % i == 0)) {
          sieve[j] = false;
        }
      }
    }
  }

  vector<int> result;
  for (auto i = 0; i <= n; i++) {
    if (sieve[i]) {
      result.emplace_back(i);
    }
  }
  return result;
}

int main(int argc, char *argv[]) {
  std::vector<std::string> args{argv + 1, argv + argc};
  std::vector<std::string> param_names{"n"};
  return GenericTestMain(args, "prime_sieve.cc", "prime_sieve.tsv",
                         &GeneratePrimes, DefaultComparator{}, param_names);
}
