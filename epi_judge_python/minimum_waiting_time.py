from typing import List

from test_framework import generic_test


def minimum_total_waiting_time(service_times: List[int]) -> int:
    service_times.sort()
    if not service_times:
        return 0
    minwt, prev = 0, 0
    for i in range(len(service_times) - 1):
        prev += service_times[i]
        minwt += prev
    return minwt


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('minimum_waiting_time.py',
                                       'minimum_waiting_time.tsv',
                                       minimum_total_waiting_time))
