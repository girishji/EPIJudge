from test_framework import generic_test
from itertools import groupby


def look_and_say(n: int) -> str:
    # res = "1"
    # for _ in range(n - 1):
    #     temp = ""
    #     digit = res[0]
    #     count = 0
    #     for c in res:
    #         if c == digit:
    #             count += 1
    #         else:
    #             temp += str(count) + digit
    #             count = 1
    #             digit = c
    #     temp += str(count) + digit
    #     res = temp
    # return res
    res = "1"
    for _ in range(n - 1):
        temp = ""
        for k, g in groupby(res):
            temp += str(len(list(g))) + k
        res = temp
    return res


if __name__ == "__main__":
    exit(
        generic_test.generic_test_main(
            "look_and_say.py", "look_and_say.tsv", look_and_say
        )
    )
