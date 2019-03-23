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


class MyQueue:
    def __init__(self):
        self.top = Stack()
        self.bottom = Stack()

    def shift(self):
        if not self.bottom.is_empty:
            return

        while not self.top.is_empty:
            self.bottom.push(self.top.pop())

    def add(self, item: int) -> Union[None, int]:
        return self.top.push(item)

    @property
    def is_empty(self) -> bool:
        return self.top.is_empty and self.bottom.is_empty

    def remove(self) -> Union[None, int]:
        self.shift()
        return self.bottom.pop()

    def peek(self) -> Union[None, int]:
        self.shift()
        return self.bottom.peek()


for use_case, expected_result in [
        (
            [('add', 1), ('add', 2), ('remove', )],
            [True, True, 1]
        )
]:
    queue = MyQueue()

    result = [
        getattr(queue, method)(*arguments)
        for method, *arguments in use_case
    ]
    assert result == expected_result, "{} != {}".format(result, expected_result)
