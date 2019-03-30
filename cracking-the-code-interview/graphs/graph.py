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
from typing import Union, Tuple, List, Callable


class Graph:
    class Kind:
        LIST = 'list'
        MATRIX = 'matrix'

    def __init__(self, store: dict = None):
        self.store = store or {}

    @staticmethod
    def build(kind: str, store: List[Tuple[int, int, int]]) -> Union['GraphList', 'GraphMatrix']:
        if kind == Graph.Kind.LIST:
            return GraphList.build(store)
        elif kind == Graph.Kind.MATRIX:
            return GraphMatrix.build(store)
        else:
            raise ValueError("Invalid stored value.")

    def has_connection(self, top: int, bottom: int) -> bool:
        raise NotImplementedError()

    def find_route(self, top: int, bottom: int) -> str:
        raise NotImplementedError()

    def bfs(self, start: int, visit: Callable):
        raise NotImplementedError()

    def dfs(self, start: int, visit: Callable):
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

    def bfs(self, start: int, visit: Callable):
        """
            0: [1]
            1: [0, 2]
            2: [1, 3]
            3: [2]

            0, 1, 2, 3
        """

        if start not in self.store:
            return

        visited = []
        queue = [
            {
                'from': start,
                'to': node,
                'value': val
            } for node, val in self.store[start].items()
        ]

        while queue:
            _next = queue.pop(0)

            if (_next['to'], _next['from']) in visited or (_next['from'], _next['to']) in visited:
                continue

            visit(_next)
            visited.append((_next['to'], _next['from']))

            for node, value in self.store[_next['to']].items():
                queue.append({
                    'from': _next['to'],
                    'to': node,
                    'value': value,
                })

        return

    def dfs(self, start: int, visit: Callable):
        visited = []

        def _dfs(node: int, _from: int = None):
            if node not in self.store or ((node, _from) in visited or (_from, node) in visited):
                return

            visited.append((node, _from))

            for _next, value in self.store[node].items():
                if (_next, node) in visited or (node, _next) in visited:
                    continue

                visit({
                    'from': node,
                    'to': _next,
                    'value': value
                })

                _dfs(_next, node)

        _dfs(start)

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
        count = 0
        while count < max_node:
            graph.append([None] * max_node)
            count += 1

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

    def bfs(self, start: int, visit: Callable):
        if start >= len(self.store):
            return

        start -= 1

        visited = []
        queue = [
            {
                'from': start,
                'to': node,
                'value': val
            } for node, val in enumerate(self.store[start])
            if val is not None
        ]

        while queue:
            _next = queue.pop(0)

            if (_next['to'], _next['from']) in visited or (_next['from'], _next['to']) in visited:
                continue

            visit({
                'from': _next['from'] + 1,
                'to': _next['to'] + 1,
                'value': _next['value']
            })

            visited.append((_next['to'], _next['from']))

            for node, value in enumerate(self.store[_next['to']]):
                if value is None:
                    continue

                queue.append({
                    'from': _next['to'],
                    'to': node,
                    'value': value,
                })

        return

    def dfs(self, start: int, visit: Callable):
        visited = []

        def _dfs(node: int, _from: int = None):
            if node >= len(self.store) or ((node, _from) in visited or (_from, node) in visited):
                return

            visited.append((node, _from))

            for _next, value in enumerate(self.store[node]):
                if value is None or (_next, node) in visited or (node, _next) in visited:
                    continue

                visit({
                    'from': node + 1,
                    'to': _next + 1,
                    'value': value
                })

                _dfs(_next, node)

        _dfs(start - 1)

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
HAIRY_GRAPH = [(1, 2, 3), (1, 3, 2), (2, 3, 5), (3, 5, 1), (5, 1, 6)]


# test build
for use_case, expected_result in [
        [
            SIMPLE_GRAPH,
            """1: ['2:3', '3:2']
2: ['1:3']
3: ['1:2']"""
        ]
]:

    list_graph = Graph.build(Graph.Kind.LIST, use_case)
    assert str(list_graph) == expected_result, "{} != {}".format(list_graph, expected_result)

    matrix_graph = Graph.build(Graph.Kind.MATRIX, use_case)
    assert str(matrix_graph) == expected_result, "{} != {}".format(matrix_graph, expected_result)


# test connection
for use_case, expected_result in [
        [[1, 2], True],
        [[1, 3], True],
        [[2, 3], False],
        [[-1, -3], False],
]:
    graph = Graph.build(Graph.Kind.LIST, SIMPLE_GRAPH)
    result = graph.has_connection(*use_case)

    assert result == expected_result, "{} != {}".format(result, expected_result)

    graph = Graph.build('matrix', SIMPLE_GRAPH)
    result = graph.has_connection(*use_case)

    assert result == expected_result, "{} != {}".format(result, expected_result)


# test bfs
for graph_type in [Graph.Kind.LIST, Graph.Kind.MATRIX]:
    graph = Graph.build(graph_type, HAIRY_GRAPH)

    def visit(node: dict):
        output.append("{} -> {} [{}]".format(node['from'], node['to'], node['value']))

    output = []
    graph.bfs(HAIRY_GRAPH[0][0], visit)
    result = " ; ".join(output)

    expected_result = "1 -> 2 [3] ; 1 -> 3 [2] ; 1 -> 5 [6] ; 2 -> 3 [5] ; 3 -> 5 [1]"
    assert result == expected_result, "{} != {}".format(result, expected_result)

    output = []
    graph.dfs(HAIRY_GRAPH[0][0], visit)
    result = " ; ".join(output)

    expected_result = "1 -> 2 [3] ; 2 -> 3 [5] ; 3 -> 1 [2] ; 1 -> 5 [6] ; 5 -> 3 [1]"
    assert result == expected_result, "{} != {}".format(result, expected_result)
