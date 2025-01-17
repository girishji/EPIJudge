from test_framework import generic_test


def gcd(x: int, y: int) -> int:
    (x, y) = (x, y) if x > y else (y, x)
    return x if y == 0 else gcd(y, x % y)


if __name__ == '__main__':
    exit(generic_test.generic_test_main('euclidean_gcd.py', 'gcd.tsv', gcd))
