#include <memory>
#include <queue>
#include <utility>
#include <vector>

#include "binary_tree_node.h"
#include "test_framework/generic_test.h"
using std::unique_ptr;
using std::vector;

vector<vector<int>>
BinaryTreeDepthOrder(const unique_ptr<BinaryTreeNode<int>> &tree) {
  // using QueElem = std::pair<int, int>; // <data, level>
  std::queue<const BinaryTreeNode<int>*> que;
  // int cur_level = 0;
  vector<vector<int>> result;
  vector<int> nodes;
  const BinaryTreeNode<int> Sentinel(0);
  for (que.push(tree.get()), que.push(&Sentinel); !que.empty();) {
    if (que.front() == &Sentinel) {
      result.push_back(nodes);
      nodes.clear();
      que.pop();
      if (!que.empty()) {
        que.push(&Sentinel);
      }
    } else {
      nodes.push_back(que.front()->data);
      if (que.front()->left) {
        que.push(que.front()->left.get());
      }
      if (que.front()->right) {
        que.push(que.front()->right.get());
      }
      que.pop();
    }
  }

  // auto [data, level] = que.front();
  //   que.pop();
  //   if (level != cur_level) {
  //     result.emplace_back(nodes);
  //     nodes.clear();
  //     cur_level = level;
  //   }
  //   nodes.push_back(data);
  // }
  if (!nodes.empty()) {
    result.push_back(nodes);
  }
  return result;
}

int main(int argc, char *argv[]) {
  std::vector<std::string> args{argv + 1, argv + argc};
  std::vector<std::string> param_names{"tree"};
  return GenericTestMain(args, "tree_level_order.cc", "tree_level_order.tsv",
                         &BinaryTreeDepthOrder, DefaultComparator{},
                         param_names);
}
