import collections
import functools
from typing import List

from test_framework import generic_test
from test_framework.test_utils import enable_executor_hook
import bisect

# Event is a tuple (start_time, end_time)
Event = collections.namedtuple("Event", ("start", "finish"))


def find_max_simultaneous_events(A: List[Event]) -> int:
    endp = []
    for a in A:
        endp.append((a.start, True))
        endp.append((a.finish, False))
    endp.sort(key=lambda a: (a[0], not a[1]))
    count, res = 0, 0
    for p in endp:
        count = count + 1 if p[1] else count - 1
        res = max(res, count)

    return res


@enable_executor_hook
def find_max_simultaneous_events_wrapper(executor, events):
    events = [Event(*x) for x in events]
    return executor.run(functools.partial(find_max_simultaneous_events, events))


if __name__ == "__main__":
    exit(
        generic_test.generic_test_main(
            "calendar_rendering.py",
            "calendar_rendering.tsv",
            find_max_simultaneous_events_wrapper,
        )
    )
