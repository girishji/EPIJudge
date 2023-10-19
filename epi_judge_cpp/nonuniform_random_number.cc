#include <algorithm>
#include <functional>
#include <iterator>
#include <numeric>
#include <random>
#include <unordered_map>
#include <vector>

#include "test_framework/generic_test.h"
#include "test_framework/random_sequence_checker.h"
#include "test_framework/timed_executor.h"
using std::abs;
using std::bind;
using std::unordered_map;
using std::vector;

int GenRandom(int max) {
  std::random_device seed;
  static std::mt19937 gen{seed()};                   // seed the generator
  static std::uniform_int_distribution dist{0, max}; // set min and max
  int guess = dist(gen);                             // generate number
  return guess;
}

int NonuniformRandomNumberGeneration(const vector<int> &values,
                                     const vector<double> &probabilities) {
  auto interval = values.size() * 1000;
  int x = GenRandom(interval);
  vector<double> sums(probabilities.size());
  std::partial_sum(probabilities.begin(), probabilities.end(), std::back_inserter(sums));
  auto selected =
      std::upper_bound(sums.begin(), sums.end(), x / 1000.0);
  auto dist = std::distance(sums.begin(), selected);
  return values[dist + 1];
}
bool NonuniformRandomNumberGenerationRunner(
    TimedExecutor &executor, const vector<int> &values,
    const vector<double> &probabilities) {
  constexpr int kN = 1000000;
  vector<int> results;

  executor.Run([&] {
    for (int i = 0; i < kN; ++i) {
      results.emplace_back(
          NonuniformRandomNumberGeneration(values, probabilities));
    }
  });

  unordered_map<int, int> counts;
  for (int result : results) {
    ++counts[result];
  }
  for (int i = 0; i < values.size(); ++i) {
    const int v = values[i];
    const double p = probabilities[i];
    if (kN * p < 50 || kN * (1.0 - p) < 50) {
      continue;
    }
    const double sigma = sqrt(kN * p * (1.0 - p));
    if (abs(counts[v] - (p * kN)) > 5 * sigma) {
      return false;
    }
  }
  return true;
}

void NonuniformRandomNumberGenerationWrapper(
    TimedExecutor &executor, const vector<int> &values,
    const vector<double> &probabilities) {
  RunFuncWithRetries(bind(NonuniformRandomNumberGenerationRunner,
                          std::ref(executor), std::cref(values),
                          std::cref(probabilities)));
}

int main(int argc, char *argv[]) {
  std::vector<std::string> args{argv + 1, argv + argc};
  std::vector<std::string> param_names{"executor", "values", "probabilities"};
  return GenericTestMain(args, "nonuniform_random_number.cc",
                         "nonuniform_random_number.tsv",
                         &NonuniformRandomNumberGenerationWrapper,
                         DefaultComparator{}, param_names);
}
