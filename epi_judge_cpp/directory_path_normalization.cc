#include <sstream>
#include <string>

#include "test_framework/generic_test.h"
using std::string;
string ShortestEquivalentPath(const string &path) {
  auto ss = std::stringstream(path);
  std::string token;
  std::stack<string> lifo;
  bool root = path.front() == '/';

  while (getline(ss, token, '/')) {
    if (token == "..") {
      if (lifo.empty() || lifo.top() == "..") {
        lifo.push(token);
      } else {
        lifo.pop();
      }
    } else if (!token.empty() && token != ".") {
      lifo.push(token);
    }
  }

  string spath;
  while (!lifo.empty()) {
    spath = spath.empty() ? lifo.top() : lifo.top() + "/" + spath;
    lifo.pop();
  }
  if (root) {
    spath = "/" + spath;
  }
  return spath.empty() ? "/" : spath;
}

int main(int argc, char *argv[]) {
  std::vector<std::string> args{argv + 1, argv + argc};
  std::vector<std::string> param_names{"path"};
  return GenericTestMain(args, "directory_path_normalization.cc",
                         "directory_path_normalization.tsv",
                         &ShortestEquivalentPath, DefaultComparator{},
                         param_names);
}
