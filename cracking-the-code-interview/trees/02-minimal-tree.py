from typing import List


class BST:
    def __init__(self, val: int, left: 'BST', right: 'BST'):
        self.val = val
        self.left = left
        self.right = right

    def __str__(self) -> str:
        if not self.val:
            return ""

        return " {} {} {} ".format(self.left, self.val, self.right)


def _height(node: BST):
    if not node:
        return 0

    return 1 + max(_height(node.left), _height(node.right))


def build(nodes: List[int]) -> BST:
    def _build(start: int, end: int):
        if start > end:
            return

        mid = (start + end) // 2
        return BST(nodes[mid], _build(start, mid - 1), _build(mid + 1, end))

    return _build(0, len(nodes) - 1)


for use_case, expected_result in [
        [[1, 2, 3, 4, 5, 6, 7, 8], 4],
        [[1], 1],
        [[1, 2, 3], 2],
        [[1, 2, 3, 5], 3],
]:
    bst = build(use_case)
    assert _height(bst) == expected_result
