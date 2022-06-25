from typing import List

from test_framework import generic_test


def find_closest_elements_in_sorted_arrays(sorted_arrays: List[List[int]]) -> int:
    size = len(sorted_arrays)
    idx = [0] * size
    inter = float('inf')
    # import sortedcontainers
    # sorted containers do not allow duplicates
    # elems = sortedcontainers.SortedDict()
    # elems.update([(sorted_arrays[i][0], i) for i in range(size)])
    # if all(idx[i] < len(sorted_arrays[i]) for i in range(size)):
    #     minidx = 0
    #     while idx[minidx] < len(sorted_arrays[minidx]):
    #         elems[sorted_arrays[minidx][idx[minidx]]] = minidx
    #         print("--")
    #         print("idx[]", idx)
    #         print("maxidx", [len(sorted_arrays[i]) for i in range(size)])
    #         print(elems)
    #         inter = min(inter, elems.peekitem()[0] - elems.peekitem(0)[0])
    #         minidx = elems.popitem(0)[1]
    #         print("minidx", minidx)
    #         idx[minidx] += 1

    # elems = [sorted_arrays[i][0] for i in range(size)]
    while all(idx[i] < len(sorted_arrays[i]) for i in range(size)):
        elems = [sorted_arrays[i][idx[i]] for i in range(size)]
        minelem = min(elems)
        idx[elems.index(minelem)] += 1
        inter = min(inter, max(elems) - minelem)
    return inter


if __name__ == "__main__":
    exit(
        generic_test.generic_test_main(
            "minimum_distance_3_sorted_arrays.py",
            "minimum_distance_3_sorted_arrays.tsv",
            find_closest_elements_in_sorted_arrays,
        )
    )
