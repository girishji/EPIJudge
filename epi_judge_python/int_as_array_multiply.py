from typing import List

from test_framework import generic_test
from itertools import zip_longest


def md(d1, d2):
    m = d1 * d2
    return (m / 10, m % 10)


def multiply(num1: List[int], num2: List[int]) -> List[int]:
    base = 0
    result = None
    n1neg = True if num1[0] < 0 else False
    n2neg = True if num2[0] < 0 else False
    if n1neg:
        num1[0] = -num1[0]
    if n2neg:
        num2[0] = -num2[0]
    for d in num2[::-1]:
        r = 0
        ir = []
        for n in num1[::-1]:
            m = n * d + r
            ir.insert(0, m % 10)
            r = int(m / 10)
        if r > 0:
            ir.insert(0, r)
        for _ in range(base):
            ir.append(0)
        # print("ir", ir)
        base += 1
        #
        if not result:
            result = ir
        else:
            r = 0
            su = []
            for i, j in zip_longest(ir[::-1], result[::-1], fillvalue=0):
                s = i + j + r
                # print("s", s)
                su.insert(0, s % 10)
                r = int(s / 10)
            if r > 0:
                su.insert(0, r)
            result = su
            # print("su", result)

    if result:
        allzero = True
        for k in result:
            if k > 0:
                allzero = False
        if allzero:
            return [0]
        if (n1neg and not n2neg) or (n2neg and not n1neg):
            result[0] = -result[0]
        return result
    return []


if __name__ == "__main__":
    exit(
        generic_test.generic_test_main(
            "int_as_array_multiply.py", "int_as_array_multiply.tsv", multiply
        )
    )
