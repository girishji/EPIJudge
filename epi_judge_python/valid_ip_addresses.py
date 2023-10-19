from typing import List

from test_framework import generic_test


def get_valid_ip_address(s: str) -> List[str]:
    if len(s) < 4:
        return []
    res = []
    for i in range(3):
        if int(s[: i + 1]) < 256 and len(s[i + 1 :]) >= 3:
            fi = s[: i + 1]
            for j in range(-min(3, len(s[i + 3 :])), 0):
                fo = s[j:]
                if int(s[j:]) < 256 and len(s[i + 1 : j]) >= 2:
                    rem = s[i + 1 : j]
                    for k in range(len(rem) - 1):
                        se = rem[: k + 1]
                        th = rem[k + 1 :]
                        addr = [fi, se, th, fo]
                        if all([int(x) < 256 for x in addr]) and not any(
                            [len(x) > 1 and x.startswith('0') for x in addr]
                        ):
                            res.append(fi + "." + se + "." + th + "." + fo)
    return res


# comment here

def comp(a, b):
    return sorted(a) == sorted(b)


if __name__ == "__main__":
    exit(
        generic_test.generic_test_main(
            "valid_ip_addresses.py",
            "valid_ip_addresses.tsv",
            get_valid_ip_address,
            comparator=comp,
        )
    )
