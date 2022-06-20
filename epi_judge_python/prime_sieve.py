from typing import List
import math

from test_framework import generic_test


# Given n, return all primes up to and including n.
def generate_primes(n: int) -> List[int]:
    # result = []
    # for i in range(2, n + 1):
    #     lim = math.floor(math.sqrt(i))
    #     prime = True
    #     for j in range(2, lim + 1):
    #         if i % j == 0:
    #             prime = False
    #     if prime:
    #         result.append(i)
    # return result
    primes = [False, False] + [True] * (n - 1)
    for i in range(n + 1):
        if primes[i]:
            m = 2
            while m * i <= n:
                primes[m * i] = False
                m += 1
    return [i for i in range(n + 1) if primes[i]]


if __name__ == "__main__":
    exit(
        generic_test.generic_test_main(
            "prime_sieve.py", "prime_sieve.tsv", generate_primes
        )
    )
