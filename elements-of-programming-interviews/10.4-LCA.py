from typing import List, Tuple, Optional


class Node:
    def __init__(self, val: int, left: 'Node' = None, right: 'Node' = None, parent: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.parent = parent

    def __eq__(self, friend: 'Node') -> bool:
        if not friend:
            return False

        return self.val == friend.val

    def __str__(self) -> str:
        return str(self.val)


def depth(tree: Node, needle: Node) -> int:
    def _depth(current_node: Node, depth: int = 0) -> Tuple[int, bool]:
        if not current_node:
            return depth + 1, False

        if current_node == needle:
            return depth + 1, True

        left, ok = _depth(current_node.left, depth + 1)
        if ok:
            return left, True

        right, ok = _depth(current_node.right, depth + 1)
        if ok:
            return right, True

        return max(left, right), False

    return _depth(tree)[0]


def lca(tree: Node, first: Node, second: Node) -> Node:
    depth_first = depth(tree, first)
    depth_second = depth(tree, second)
    min_depth = min(depth_first, depth_second)

    if depth_second < depth_first:
        depth_second, depth_first = depth_first, depth_second

    while depth_second > min_depth:
        second = second.parent
        depth_second -= 1

    while second != first:
        second = second.parent
        first = first.parent

    return first


def debug(node: Node, lvl: int = 0) -> str:
    if not node:
        return ''

    output = '\n' + '|  ' * lvl
    if lvl == 0:
        output += '--' + str(node)
    else:
        output += '|--' + str(node)

    output += debug(node.left, lvl + 1)
    output += debug(node.right, lvl + 1)

    return output


def create_tree(numbers: List[int], parent: Node = None, root_idx: int = 0, lvl: int = 0) -> Node:
    if not numbers:
        return None

    current = Node(numbers[root_idx], parent=parent)

    # 1, 3, 7
    left_idx = root_idx * 2 + 1
    if len(numbers) > left_idx:
        current.left = create_tree(numbers, current, left_idx, lvl + 1)

    # 2, 6
    right_idx = root_idx * 2 + 2
    if len(numbers) > right_idx:
        current.right = create_tree(numbers, current, right_idx, lvl + 1)

    return current


def find_node(current_node: Node, needle: int) -> Node:
    if not current_node:
        return None

    if current_node.val == needle:
        return current_node

    return find_node(current_node.left, needle) or find_node(current_node.right, needle)


tree = create_tree([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

first = find_node(tree, 9)
second = find_node(tree, 8)

print(lca(tree, first, second))
