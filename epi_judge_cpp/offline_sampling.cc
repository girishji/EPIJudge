#include <algorithm>
#include <functional>
#include <iterator>
#include <random>
#include <type_traits>
#include <vector>

#include "test_framework/generic_test.h"
#include "test_framework/random_sequence_checker.h"
#include "test_framework/timed_executor.h"
using std::bind;
using std::mt19937;
using std::vector;

int generate(int min, int max) {
  std::random_device seed;
  mt19937 gen{seed()};                        // seed the generator
  std::uniform_int_distribution dist{min, max}; // set min and max
  int guess = dist(gen); // generate number
  return guess;
}
void RandomSampling(int k, vector<int>* A_ptr) {
  // TODO - you fill in here.
  auto &A{*A_ptr};
  if (A.size() == k) {
    return;
  }
  for (auto i = 0; i < k; i++) {
    auto rn = generate(i, A.size() - 1);
    std::swap(A[i], A[rn]);
  }
  return;
}
bool RandomSamplingRunner(TimedExecutor& executor, int k, vector<int> A) {
  using namespace test_framework;
  vector<vector<int>> results;

  executor.Run([&] {
    for (int i = 0; i < 100000; ++i) {
      RandomSampling(k, &A);
      results.emplace_back(begin(A), begin(A) + k);
    }
  });

  int total_possible_outcomes = BinomialCoefficient(A.size(), k);
  sort(begin(A), end(A));
  vector<vector<int>> combinations;
  for (int i = 0; i < BinomialCoefficient(A.size(), k); ++i) {
    combinations.emplace_back(ComputeCombinationIdx(A, A.size(), k, i));
  }
  vector<int> sequence;
  for (vector<int> result : results) {
    sort(begin(result), end(result));
    sequence.emplace_back(
        distance(begin(combinations),
                 find(begin(combinations), end(combinations), result)));
  }
  return CheckSequenceIsUniformlyRandom(sequence, total_possible_outcomes,
                                        0.01);
}

void RandomSamplingWrapper(TimedExecutor& executor, int k,
                           const vector<int>& A) {
  RunFuncWithRetries(
      bind(RandomSamplingRunner, std::ref(executor), k, std::cref(A)));
}

int main(int argc, char* argv[]) {
  std::vector<std::string> args{argv + 1, argv + argc};
  std::vector<std::string> param_names{"executor", "k", "A"};
  return GenericTestMain(args, "offline_sampling.cc", "offline_sampling.tsv",
                         &RandomSamplingWrapper, DefaultComparator{},
                         param_names);
}
