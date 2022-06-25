from typing import List

from test_framework import generic_test
import collections


def find_all_substrings(s: str, words: List[str]) -> List[int]:
    wlen = len(words[0]) if words else 0
    wcount = collections.Counter(words)
    i = 0
    res = []
    while i <= (len(s) - wlen):
        w = s[i:i + wlen]
        if w in wcount:
            ti = i
            while ti <= (len(s) - wlen):
                w2 = s[ti:ti + wlen]
                if w2 in wcount:
                    if wcount[w2] > 1:
                        wcount[w2] -= 1
                    else:
                        del wcount[w2]
                    ti += wlen
                else:
                    break
            if not wcount:
                res.append(i)
            wcount = collections.Counter(words)
        i += 1
    return res


if __name__ == "__main__":
    exit(
        generic_test.generic_test_main(
            "string_decompositions_into_dictionary_words.py",
            "string_decompositions_into_dictionary_words.tsv",
            find_all_substrings,
        )
    )
