import functools
from typing import List

from test_framework import generic_test
from test_framework.test_utils import enable_executor_hook


class GraphVertex:
    def __init__(self) -> None:
        self.edges: List['GraphVertex'] = []


def is_deadlocked(graph: List[GraphVertex]) -> bool:

    def back_edge(node, seen):
        for n in node.edges:
            if n in seen:
                return True
            seen.append(n)
            if back_edge(n, seen):
                return True
        return False

    for node in graph:
        seen = [node]
        if back_edge(node, seen):
            return True
    return False
        
        

@enable_executor_hook
def is_deadlocked_wrapper(executor, num_nodes, edges):
    if num_nodes <= 0:
        raise RuntimeError('Invalid num_nodes value')
    graph = [GraphVertex() for _ in range(num_nodes)]

    for (fr, to) in edges:
        if fr < 0 or fr >= num_nodes or to < 0 or to >= num_nodes:
            raise RuntimeError('Invalid vertex index')
        graph[fr].edges.append(graph[to])

    return executor.run(functools.partial(is_deadlocked, graph))


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('deadlock_detection.py',
                                       'deadlock_detection.tsv',
                                       is_deadlocked_wrapper))
