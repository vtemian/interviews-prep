"""
    stack: [4, 5, 1, 2, 7]
    min: 1
"""

from typing import Union


class Stack:
    def __init__(self, size: int = 100):
        self.size = size
        self.store = []

    def pop(self) -> Union[int, None]:
        if self.is_empty():
            return None

        return self.store.pop()[0]

    def peek(self) -> Union[int, None]:
        if self.is_empty():
            return None

        return self.store[-1][0]

    def push(self, item: int) -> bool:
        if len(self.store) == self.size:
            return False

        current_min = item
        top = self.store[-1] if not self.is_empty() else None

        if top:
            current_min = min(current_min, top[1])

        self.store.append((item, current_min))

        return True

    def is_empty(self) -> bool:
        return len(self.store) == 0

    def min(self) -> Union[int, None]:
        top = self.store[-1] if not self.is_empty() else None
        return top[1] if top else None


for use_case, expected_result in [
        (
            [('push', 4), ('push', 5), ('min', ), ('push', 1), ('min', )],
            [True, True, 4, True, 1]
        )
]:
    stack = Stack()

    result = [
        getattr(stack, method)(*arguments)
        for method, *arguments in use_case
    ]
    assert result == expected_result, "{} != {}".format(result, expected_result)
