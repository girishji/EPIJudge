from test_framework import generic_test


def levenshtein_distance(A: str, B: str) -> int:
    def solve(a, b):
        i = 0
        if i >= len(A) - a:
            return len(B) - b + 1
        if i >= len(B) - b:
            return len(A) - a + 1
        if distance[a][b] == -1:
            if A[i + a] == B[i + b]:
                distance[a][b] = solve(a + 1, b + 1)
            else:
                distance[a][b] = (
                    min(
                        solve(a + i + 1, b + i + 1),
                        solve(a + i, b + i + 1),
                        solve(a + i + 1, b + i),
                    )
                    + 1
                )
        return distance[a][b]

    distance = [[-1] * (len(B) + 1) for _ in range(len(A) + 1)]
    return solve(0, 0)


if __name__ == "__main__":
    exit(
        generic_test.generic_test_main(
            "levenshtein_distance.py", "levenshtein_distance.tsv", levenshtein_distance
        )
    )
