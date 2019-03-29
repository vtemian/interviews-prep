"""
0: [1, 2, 3]
1: [0]
2: [0, 3]
3: [0, 2]
"""

"""
    0 1 2 3
------------
0 | 0 1 1 1
1 | 1 0 0 0
2 | 1 0 0 1
3 | 1 0 1 0
"""
from typing import Union, Tuple, List


class Graph:
    def __init__(self, store: dict = None):
        self.store = store or {}

    @staticmethod
    def build(kind: str, store: List[Tuple[int, int, int]]) -> Union['GraphList', 'GraphMatrix']:
        if kind == 'list':
            return GraphList.build(store)
        elif kind == 'matrix':
            return GraphMatrix.build(store)
        else:
            raise ValueError("Invalid stored value.")

    def has_connection(self, top: int, bottom: int) -> bool:
        raise NotImplementedError()

    def find_route(self, top: int, bottom: int) -> str:
        raise NotImplementedError()

    def bfs(self, start: int) -> str:
        raise NotImplementedError()

    def dfs(self, start: int) -> str:
        raise NotImplementedError()


class GraphList(Graph):
    def build(store: List[Tuple[int, int, int]]) -> 'GraphList':
        graph = {}

        for node in store:
            _from, _to, val = node

            if _from not in graph:
                graph[_from] = {}

            if _to not in graph:
                graph[_to] = {}

            graph[_from][_to] = val
            graph[_to][_from] = val

        return GraphList(graph)

    def has_connection(self, _from: int, _to: int) -> bool:
        return _from in self.store and _to in self.store[_from]

    def __str__(self) -> str:
        output = []
        for _from, neighbours in self.store.items():
            output.append("{}: {}".format(_from,
                                          ["{}:{}".format(neighbour, val)
                                           for neighbour, val in neighbours.items()]))
        return '\n'.join(output)


class GraphMatrix(Graph):
    def build(store: List[Tuple[int, int, int]]) -> 'GraphList':
        max_node = -1

        for node in store:
            _from, _to, _ = node
            max_node = max(_from, _to, max_node)

        graph = []
        while max_node:
            graph.append([None] * max_node)
            max_node -= 1

        for node in store:
            _from, _to, val = node
            graph[_from - 1][_to - 1] = val
            graph[_to - 1][_from - 1] = val

        return GraphMatrix(graph)

    def has_connection(self, _from: int, _to: int) -> bool:
        if _from < 0 or _to < 0:
            return False

        _from -= 1
        _to -= 1

        if len(self.store) <= _from:
            return False

        if len(self.store[_from]) <= _to:
            return False

        return self.store[_to][_from] is not None

    def __str__(self) -> str:
        output = []

        for line_idx, line in enumerate(self.store):
            line_out = []

            for col_idx, val in enumerate(line):
                if val is not None:
                    line_out.append("{}:{}".format(col_idx + 1, val))

            if line_out:
                output.append("{}: {}".format(line_idx + 1, line_out))

        return '\n'.join(output)


SIMPLE_GRAPH = [(1, 2, 3), (1, 3, 2), (1, 3, 2), (1, 2, 3)]


for use_case, expected_result in [
        [
            SIMPLE_GRAPH,
            """1: ['2:3', '3:2']
2: ['1:3']
3: ['1:2']"""
        ]
]:

    list_graph = Graph.build('list', use_case)
    assert str(list_graph) == expected_result, "{} != {}".format(list_graph, expected_result)

    matrix_graph = Graph.build('matrix', use_case)
    assert str(matrix_graph) == expected_result, "{} != {}".format(matrix_graph, expected_result)


for use_case, expected_result in [
        [[1, 2], True],
        [[1, 3], True],
        [[2, 3], False],
        [[-1, -3], False],
]:
    graph = Graph.build('list', SIMPLE_GRAPH)
    result = graph.has_connection(*use_case)

    assert result == expected_result, "{} != {}".format(result, expected_result)

    graph = Graph.build('matrix', SIMPLE_GRAPH)
    result = graph.has_connection(*use_case)

    assert result == expected_result, "{} != {}".format(result, expected_result)
