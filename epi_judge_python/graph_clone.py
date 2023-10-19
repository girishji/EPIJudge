import collections
from typing import List

from test_framework import generic_test
from test_framework.test_failure import TestFailure


class GraphVertex:
    def __init__(self, label: int) -> None:
        self.label = label
        self.edges: List["GraphVertex"] = []

    # def __hash__(self) -> int:
    #     return self.label
    #
    # def __eq__(self, __o: object) -> bool:
    #     if isinstance(__o, GraphVertex):
    #         return self.label == __o.label
    #     return False
    #
    def __repr__(self) -> str:
        return (
            "label: "
            + str(self.label)
            + "; "
            + ",".join(str(edge.label) for edge in self.edges)
        )


def clone_graph(graph: GraphVertex) -> GraphVertex:

    que = collections.deque()
    mapping = {graph: GraphVertex(graph.label)}
    que.append(graph)

    while que:
        node = que.popleft()
        node_cl = mapping[node]
        for edge in node.edges:
            edge_cl = mapping[edge] if edge in mapping else GraphVertex(edge.label)
            if edge_cl in node_cl.edges:
                continue
            mapping[edge] = edge_cl
            node_cl.edges.append(edge_cl)
            if edge not in que:
                que.append(edge)

    return mapping[graph]

    # clones = {}
    #
    # def dfs(node):
    #     clone = clones[node]
    #     for n in node.edges:
    #         n_clone = clones[n] if n in clones else GraphVertex(n.label)
    #         if n_clone not in clone.edges:
    #             clone.edges.append(n_clone)
    #             clones[n] = n_clone
    #             dfs(n)
    #
    # cloned = GraphVertex(graph.label)
    # clones[graph] = cloned
    # dfs(graph)
    # return cloned


def copy_labels(edges):
    return [e.label for e in edges]


def check_graph(node, graph):
    if node is None:
        raise TestFailure("Graph was not copied")

    vertex_set = set()
    q = collections.deque()
    q.append(node)
    vertex_set.add(node)
    while q:
        vertex = q.popleft()
        if vertex.label >= len(graph):
            raise TestFailure("Invalid vertex label")
        label1 = copy_labels(vertex.edges)
        label2 = copy_labels(graph[vertex.label].edges)
        if sorted(label1) != sorted(label2):
            raise TestFailure("Edges mismatch")
        for e in vertex.edges:
            if e not in vertex_set:
                vertex_set.add(e)
                q.append(e)


def clone_graph_test(k, edges):
    if k <= 0:
        raise RuntimeError("Invalid k value")
    graph = [GraphVertex(i) for i in range(k)]

    for (fr, to) in edges:
        if fr < 0 or fr >= k or to < 0 or to >= k:
            raise RuntimeError("Invalid vertex index")
        graph[fr].edges.append(graph[to])

    result = clone_graph(graph[0])
    check_graph(result, graph)


if __name__ == "__main__":
    exit(
        generic_test.generic_test_main(
            "graph_clone.py", "graph_clone.tsv", clone_graph_test
        )
    )
