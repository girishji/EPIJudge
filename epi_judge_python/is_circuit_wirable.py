import functools
from typing import List
import collections

from test_framework import generic_test
from test_framework.test_utils import enable_executor_hook


class GraphVertex:
    def __init__(self) -> None:
        self.d = -1
        self.edges: List[GraphVertex] = []
        self.color = 0


def is_any_placement_feasible(graph: List[GraphVertex]) -> bool:
    que = collections.deque()
    BLACK, WHITE = range(1, 3)

    def bfs():
        if not que:
            return True
        node = que.popleft()
        other = BLACK if node.color == WHITE else WHITE
        for edge in node.edges:
            if edge.color:
                if edge.color != other:
                    return False
            else:
                edge.color = other
                que.append(edge)
        return bfs()

    for node in graph:
        if not node.color:
            node.color = WHITE
            que.append(node)
            if not bfs():
                return False

    return True


@enable_executor_hook
def is_any_placement_feasible_wrapper(executor, k, edges):
    if k <= 0:
        raise RuntimeError('Invalid k value')
    graph = [GraphVertex() for _ in range(k)]

    for (fr, to) in edges:
        if fr < 0 or fr >= k or to < 0 or to >= k:
            raise RuntimeError('Invalid vertex index')
        graph[fr].edges.append(graph[to])

    return executor.run(functools.partial(is_any_placement_feasible, graph))


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('is_circuit_wirable.py',
                                       'is_circuit_wirable.tsv',
                                       is_any_placement_feasible_wrapper))
