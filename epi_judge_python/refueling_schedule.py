import functools
from typing import List

from test_framework import generic_test
from test_framework.test_failure import TestFailure
from test_framework.test_utils import enable_executor_hook
import collections
import itertools

MPG = 20


# gallons[i] is the amount of gas in city i, and distances[i] is the
# distance city i to the next city.
def find_ample_city(gallons: List[int], distances: List[int]) -> int:
    head, tail = 0, len(gallons) - 1
    surplus = 0
    while head <= tail:
        if surplus >= 0:
            surplus += gallons[head] * MPG - distances[head]
            head += 1
        else:
            surplus += gallons[tail] * MPG - distances[tail]
            tail -= 1
    return (tail + 1) % len(gallons)

    # Item = collections.namedtuple("Item", ["i", "gas", "dist"])
    # cand = [Item(i, gas, dist) for i, (gas, dist) in enumerate(zip(gallons, distances))]
    # cand.sort(reverse=True, key=lambda item: item.gas * MPG - item.dist)
    #
    # def verify(start):
    #     excess = 0
    #     for i in range(start, start + len(gallons)):
    #         i %= len(gallons)
    #         excess += gallons[i] * MPG - distances[i]
    #         if excess < 0:
    #             return False
    #     return True
    #
    # for candidate in cand:
    #     if verify(candidate.i):
    #         return candidate.i
    # return -1


@enable_executor_hook
def find_ample_city_wrapper(executor, gallons, distances):
    result = executor.run(functools.partial(find_ample_city, gallons, distances))
    num_cities = len(gallons)
    tank = 0
    for i in range(num_cities):
        city = (result + i) % num_cities
        tank += gallons[city] * MPG - distances[city]
        if tank < 0:
            raise TestFailure("Out of gas on city {}".format(i))


if __name__ == "__main__":
    exit(
        generic_test.generic_test_main(
            "refueling_schedule.py", "refueling_schedule.tsv", find_ample_city_wrapper
        )
    )
