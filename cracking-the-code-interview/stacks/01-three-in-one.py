"""
[
    -> [1 ........................ n / 3),
    -> [n / 3 .................... 2 * n / 3),
    -> [2 * n / 3 ................ n)
]

[
    ->  . . . . . . . . .
    ->  1 2 3 4 5 6 7 8 9
]
"""
from random import choice
from typing import Union, List


class Stack:
    def __init__(self, store: List[int], start: int, end: int):
        self.store = store

        self.start = start
        self.current = start - 1
        self.end = end

    def push(self, item: int) -> bool:
        if self.is_empty:
            return False

        self.store[self.current + 1] = item
        self.current += 1

        return True

    def pop(self) -> Union[int, None]:
        if self.current == self.start - 1:
            return None

        result = self.store[self.current]
        self.current -= 1

        return result

    def peek(self) -> Union[int, None]:
        if self.current == self.start - 1:
            return None

        return self.store[self.current]

    @property
    def is_empty(self) -> bool:
        return self.current + 1 == self.end


class StackHub:
    def __init__(self, size: int = 100, no_stacks: int = 3):
        self.store = [0] * size

        stack_size = size // no_stacks
        self.stacks = [Stack(self.store, stack_no * stack_size,
                             (stack_no + 1) * stack_size)
                       for stack_no in range(no_stacks)]

    def push(self, item: int, stack_no: int = None) -> bool:
        stack = self.stacks[stack_no] if stack_no is not None else choice(self.stacks)
        return stack.push(item)

    def pop(self, stack_no: int = None) -> Union[int, None]:
        stack = self.stacks[stack_no] if stack_no is not None else choice(self.stacks)
        return stack.pop()

    def peek(self, stack_no: int = None) -> Union[int, None]:
        stack = self.stacks[stack_no] if stack_no is not None else choice(self.stacks)
        return stack.peek()

    def is_empty(self, stack_no: int = None) -> bool:
        stack = self.stacks[stack_no] if stack_no is not None else choice(self.stacks)
        return stack.is_empty()


for use_case in [
        (1, 1, [('push', 1, 0), ('push', 2, 0), ('push', 3, 0), ('peek', 0), ('pop', 0), ('push', 0, 0), ('peek', 0)],
         [True, False, False, 1, 1, True, 0]),
        (10, 3, [('push', 1, 0), ('push', 2, 1), ('push', 3, 2),
                 ('peek', 0), ('peek', 1), ('peek', 2),
                 ('pop', 0), ('push', 0, 0), ('peek', 0)],
         [True, True, True, 1, 2, 3, 1, True, 0]),
]:

    hub_size, no_stacks, calls, expected_results = use_case
    hub = StackHub(hub_size, no_stacks)

    result = [
        getattr(hub, method)(*arguments)
        for method, *arguments in calls
    ]

    assert result == expected_results, "{} != {}".format(result, expected_results)
