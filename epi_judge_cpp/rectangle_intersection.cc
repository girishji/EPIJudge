#include <tuple>
#include <utility>

#include "test_framework/fmt_print.h"
#include "test_framework/generic_test.h"
#include "test_framework/serialization_traits.h"
struct Rect {
  int x, y, width, height;
};

using Segment = std::pair<int, int>;

std::optional<Segment> overlap(const Segment &seg1, const Segment &seg2) {

  auto [x1, w1] = (seg1.first <= seg2.first) ? seg1 : seg2;
  auto [x2, w2] = (seg1.first <= seg2.first) ? seg2 : seg1;

  if (x2 <= x1 + w1) {
    if (x2 + w2 <= x1 + w1) {
      return std::make_pair(x2, w2);
    }
    return std::make_pair(x2, x1 + w1 - x2);
  }
  return {};
}

Rect IntersectRectangle(const Rect &r1, const Rect &r2) {
  // TODO - you fill in here.
  // return {0, 0, 0, 0};

  if (auto ovx = overlap(std::make_pair(r1.x, r1.width),
                         std::make_pair(r2.x, r2.width))) {
    if (auto ovy = overlap(std::make_pair(r1.y, r1.height),
                           std::make_pair(r2.y, r2.height))) {
      return Rect{ovx->first, ovy->first, ovx->second, ovy->second};
    }
  }
  return {0, 0, -1, -1};
}
bool operator==(const Rect &r1, const Rect &r2) {
  return std::tie(r1.x, r1.y, r1.width, r1.height) ==
         std::tie(r2.x, r2.y, r2.width, r2.height);
}

namespace test_framework {
template <>
struct SerializationTrait<Rect> : UserSerTrait<Rect, int, int, int, int> {
  static std::vector<std::string> GetMetricNames(const std::string &arg_name) {
    return {FmtStr("height({})", arg_name), FmtStr("width({})", arg_name)};
  }

  static std::vector<int> GetMetrics(const Rect &x) {
    return {x.height, x.width};
  }
};
} // namespace test_framework

std::ostream &operator<<(std::ostream &out, const Rect &r) {
  return PrintTo(out, std::make_tuple(r.x, r.y, r.width, r.height));
}

int main(int argc, char *argv[]) {
  std::vector<std::string> args{argv + 1, argv + argc};
  std::vector<std::string> param_names{"r1", "r2"};
  return GenericTestMain(args, "rectangle_intersection.cc",
                         "rectangle_intersection.tsv", &IntersectRectangle,
                         DefaultComparator{}, param_names);
}
