from test_framework import generic_test


def compute_binomial_coefficient(n: int, k: int) -> int:
    res, dr = 1, 1
    for nr in range(n - k + 1, n + 1):
        if nr == 0:
            break
        res *= nr
        if dr <= k and res % dr == 0:
            res //= dr
            dr += 1

    return res


if __name__ == "__main__":
    exit(
        generic_test.generic_test_main(
            "binomial_coefficients.py",
            "binomial_coefficients.tsv",
            compute_binomial_coefficient,
        )
    )
