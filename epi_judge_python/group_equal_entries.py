import collections
import functools
from typing import List

from test_framework import generic_test
from test_framework.test_failure import TestFailure
from test_framework.test_utils import enable_executor_hook

Person = collections.namedtuple("Person", ("age", "name"))


def group_by_age(people: List[Person]) -> None:
    count, start = {}, {}
    for p in people:
        count[p.age] = 1 if p.age not in count else count[p.age] + 1
    sta = 0
    pos = {}
    for age, cnt in count.items():
        start[age] = sta
        pos[age] = sta
        sta += cnt
    for i in range(len(people)):
        p = people[i]
        while i < start[p.age] or i >= (start[p.age] + count[p.age]):
            dest = pos[p.age]
            people[dest], people[i] = people[i], people[dest]
            pos[p.age] += 1
            p = people[i]

    return


@enable_executor_hook
def group_by_age_wrapper(executor, people):
    if not people:
        return
    people = [Person(*x) for x in people]
    values = collections.Counter()
    values.update(people)

    executor.run(functools.partial(group_by_age, people))

    if not people:
        raise TestFailure("Empty result")

    new_values = collections.Counter()
    new_values.update(people)
    if new_values != values:
        raise TestFailure("Entry set changed")

    ages = set()
    last_age = people[0].age

    for x in people:
        if x.age in ages:
            raise TestFailure("Entries are not grouped by age")
        if last_age != x.age:
            ages.add(last_age)
            last_age = x.age


if __name__ == "__main__":
    exit(
        generic_test.generic_test_main(
            "group_equal_entries.py", "group_equal_entries.tsv", group_by_age_wrapper
        )
    )
