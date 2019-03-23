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


class MegaStack:

    def __init__(self, stack_size: int = 100):
        self.stacks = []
        self.current_stack_index = 0

        self.stack_size = stack_size

        self._extend_stacks()

    def _extend_stacks(self):
        self.stacks.append(Stack(self.stack_size))
        self.current_stack_index = len(self.stacks) - 1

    @property
    def _current(self) -> Stack:
        return self.stacks[self.current_stack_index]

    def pop(self) -> Union[int, None]:
        if not self.stacks:
            return None

        item = self._current.pop()
        if self._current.is_empty and self.current_stack_index != 0:
            self.stacks.pop(self.current_stack_index)
            self.current_stack_index -= 1

        return item

    def peek(self) -> Union[int, None]:
        if not self.stacks:
            return None

        return self._current.peek()

    def push(self, item: int) -> bool:
        if not self.stacks:
            return None

        if self._current.is_full:
            self._extend_stacks()

        return self._current.push(item)

    def is_empty(self) -> bool:
        if not self.stacks:
            return None

        return self.stacks[0].is_empty

    def pop_at(self, index: int) -> Union[None, int]:
        """
            stacks:    [1, 2, 3] [4, 5, 6] [7, 8]
            pop_at(1)
            stacks:    [1, 2, 3] [4, 5, 7] [8]
        """

        if index > len(self.stacks) - 1 or index < 0:
            return None

        if index == self.current_stack_index:
            return self.pop()

        def left_shift(index: int):
            if index + 2 > len(self.stacks):
                return

            temp_stack = Stack(self.stack_size)
            stack = self.stacks[index + 1]

            while not stack.is_empty:
                temp_stack.push(stack.pop())

            self._current.push(temp_stack.pop())

            while not temp_stack.is_empty:
                stack.push(temp_stack.pop())

            return left_shift(index + 1)

        item = self.stacks[index].pop()

        left_shift(index)

        return item

for use_case, expected_result in [
        (
            [('push', 4), ('push', 5), ('push', 1), ('peek', ), ('pop', ), ('pop', ), ('pop', )],
            [True, True, True, 1, 1, 5, 4]
        ),
        (
            [('push', 4), ('push', 1), ('peek', ), ('pop', ), ('pop', ), ('pop', ), ('peek', )],
            [True, True, 1, 1, 4, None, None]
        ),
        (
            [('push', 1), ('push', 2), ('push', 3), ('pop_at', 1), ('push', 2), ('peek', )],
            [True, True, True, 2, True, 2]
        ),
]:
    stack = MegaStack(1)
    result = [
        getattr(stack, method)(*arguments)
        for method, *arguments in use_case
    ]
    assert result == expected_result, "{} != {}".format(result, expected_result)
