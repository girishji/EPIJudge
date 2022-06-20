from typing import Iterator, List

from test_framework import generic_test
import heapq


def online_median(sequence: Iterator[int]) -> List[float]:
    minh = []
    maxh = []
    res = []
    for s in sequence:
        if not minh:
            minh.append(s)
        if not maxh:
            maxh.append(-s)
        if -s <= maxh[0]:
            heapq.heappush(minh, -s)
        else:
            heapq.heappush(maxh, s)
        if abs(len(minh) - len(maxh)) == 2:
            if len(minh) > len(maxh):
                el = heapq.heappop(minh)
                heapq.heappush(maxh, -el)
            else:
                el = heapq.heappop(maxh)
                heapq.heappush(minh, -el)
        if len(minh) == len(maxh):
            res.append((minh[0] - maxh[0]) / 2)
        else:
            res.append(minh[0] if len(minh) > len(maxh) else -maxh[0])

        # heapq.heappush(minh, s)
        # sorted_seq = heapq.nsmallest(len(minh) // 2 + 1, minh)
        # if len(minh) % 2 == 0:
        #     res.append(sum(sorted_seq[-2:]) / 2)
        # else:
        #     res.append(sorted_seq[-1])

    return res


def online_median_wrapper(sequence):
    return online_median(iter(sequence))


if __name__ == "__main__":
    exit(
        generic_test.generic_test_main(
            "online_median.py", "online_median.tsv", online_median_wrapper
        )
    )
