from typing import List

from test_framework import generic_test, test_utils


def phone_mnemonic(phone_number: str) -> List[str]:
    mapping = {
        '0': ["0"],
        '1': ["1"],
        '2': ["A", "B", "C"],
        '3': ["D", "E", "F"],
        '4': ["G", "H", "I"],
        '5': ["J", "K", "L"],
        '6': ["M", "N", "O"],
        '7': ["P", "Q", "R", "S"],
        '8': ["T", "U", "V"],
        '9': ["W", "X", "Y", "Z"],
    }

    def buildm(num):
        nonlocal mapping
        if len(num) == 1:
            return mapping[num[0]]
        mnemonics = buildm(num[1:])
        res = []
        for c in mapping[num[0]]:
            for m in mnemonics:
                res.append(c + m)
        return res

    return buildm(phone_number)


# phone_mnemonic('2276696')

if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            'phone_number_mnemonic.py',
            'phone_number_mnemonic.tsv',
            phone_mnemonic,
            comparator=test_utils.unordered_compare))
