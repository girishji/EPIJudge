from test_framework import generic_test


def test_collatz_conjecture(n: int) -> bool:
    collatz = {1}

    def check(n):
        nonlocal collatz
        if n in collatz:
            return True
        n = n // 2 if n % 2 == 0 else 3 * n + 1
        if check(n):
            collatz.add(n)
            return True
        return False

    for i in range(1, n + 1):
        if not check(i):
            return False
    return True


if __name__ == "__main__":
    exit(
        generic_test.generic_test_main(
            "collatz_checker.py", "collatz_checker.tsv", test_collatz_conjecture
        )
    )
