from test_framework import generic_test


def number_of_ways(n: int, m: int) -> int:
    def solve(i, j):
        if i == n or j == m:
            return 0
        if ways[i][j] == -1:
            ways[i][j] = 0
            if i < n:
                ways[i][j] += solve(i + 1, j)
            if j < m:
                ways[i][j] += solve(i, j + 1)
        return ways[i][j]
        
    ways = [[-1] * m for _ in range(n)]
    ways[n - 1][m - 1] = 1
    return solve(0, 0)


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('number_of_traversals_matrix.py',
                                       'number_of_traversals_matrix.tsv',
                                       number_of_ways))
