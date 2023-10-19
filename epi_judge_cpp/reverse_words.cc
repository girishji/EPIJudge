#include <deque>
#include <fstream>
#include <iterator>
#include <optional>
#include <string>
#include <type_traits>

#include "test_framework/generic_test.h"
#include "test_framework/timed_executor.h"
using std::string;

std::optional<string> GetWord(string::iterator &it) { return {}; }

void ReverseWords(string *s_ptr) {
  auto &s{*s_ptr};
  string cache, word;
  for (auto it = s.rbegin(); it != s.rend(); it++) {
    if (*it != ' ') {
      word.insert(0, 1, *it);
      if (it != (s.rend() - 1)) {
        continue;
      }
    }
    cache += word + ' ';
    word.clear();
  }
  if (s[0] != ' ') {
    cache.pop_back();
  }
  s.swap(cache);
  return;
}
string ReverseWordsWrapper(TimedExecutor &executor, string s) {
  string s_copy = s;

  executor.Run([&] { ReverseWords(&s_copy); });

  return s_copy;
}

int main(int argc, char *argv[]) {
  std::vector<std::string> args{argv + 1, argv + argc};
  std::vector<std::string> param_names{"executor", "s"};
  return GenericTestMain(args, "reverse_words.cc", "reverse_words.tsv",
                         &ReverseWordsWrapper, DefaultComparator{},
                         param_names);
}
