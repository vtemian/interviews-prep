"""
3

1
2
4
5

3  2
4  1
5
"""

from typing import Union


class Stack:
    def __init__(self, size: int = 100):
        self.size = size
        self.store = []

    def pop(self) -> Union[int, None]:
        if self.is_empty:
            return None

        return self.store.pop()

    def peek(self) -> Union[int, None]:
        if self.is_empty:
            return None

        return self.store[-1]

    def push(self, item: int) -> bool:
        if len(self.store) == self.size:
            return False

        self.store.append(item)

        return True

    @property
    def is_empty(self) -> bool:
        return len(self.store) == 0

    @property
    def is_full(self) -> bool:
        return len(self.store) == self.size

    def __str__(self) -> str:
        return str(self.store)


class SortStack:
    def __init__(self, size: int = 100):
        self.temp = Stack(size)
        self.sorted = Stack(size)

        self.size = size

    def pop(self) -> Union[int, None]:
        if self.is_empty:
            return None

        return self.sorted.pop()

    def peek(self) -> Union[int, None]:
        if self.is_empty:
            return None

        return self.sorted.peek()

    def push(self, item: int) -> bool:
        if self.sorted.is_full:
            return False

        while self.sorted.peek() and self.sorted.peek() < item:
            self.temp.push(self.sorted.pop())

        self.sorted.push(item)

        while not self.temp.is_empty:
            self.sorted.push(self.temp.pop())

        return True

    @property
    def is_empty(self) -> bool:
        return self.sorted.is_empty

    @property
    def is_full(self) -> bool:
        return self.sorted.is_full

    def __str__(self) -> str:
        return str(self.sorted)


for use_case, expected_result in [
        (
            [('push', 3), ('push', 1), ('push', 2), ('pop', ), ('pop', ), ('pop', )],
            [True, True, True, 1, 2, 3]
        ),
        (
            [('push', 99), ('push', 98), ('push', 97), ('pop', ), ('pop', ), ('pop', )],
            [True, True, True, 97, 98, 99]
        ),
]:
    stack = SortStack()

    result = [
        getattr(stack, method)(*arguments)
        for method, *arguments in use_case
    ]
    assert result == expected_result, "{} != {}".format(result, expected_result)
