from typing import Tuple, List


def compute_build_order(projects: List[str], dependencies: List[Tuple[str, str]]) -> List[str]:
    store = {
        project: []
        for project in projects
    }

    for parent, kid in dependencies:
        store[kid].append(parent)

    order = []
    built_projects = set()

    def _find_deps(project: str) -> List[str]:
        if project in built_projects:
            return []

        if project in visited:
            raise ValueError()

        visited.add(project)

        if not store[project]:
            return [project]

        result = []
        for kid in store[project]:
            result += _find_deps(kid)

        return result + [project]

    for project in projects:
        if project in built_projects:
            continue

        try:
            visited = set()
            result = _find_deps(project)
        except ValueError as exc:
            return []

        for dep in result:
            built_projects.add(dep)

        order += result

    return order


for use_case, expected_result in [
        [
            [('a', 'b', 'c', 'd', 'e', 'f'),
             [('a', 'd'), ('f', 'b'), ('b', 'd'), ('f', 'a'), ('d', 'c')]],
            ['f', 'a', 'b', 'd', 'c', 'e']
        ],
        [
            [('a', 'b', 'c', 'd', 'e', 'f'),
             [('a', 'd'), ('f', 'b'), ('b', 'd'), ('f', 'a'), ('d', 'c'), ('d', 'f')]],
            []
        ]
]:
    result = compute_build_order(*use_case)
    assert result == expected_result, "{} != {}".format(result, expected_result)
