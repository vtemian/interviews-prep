class Stack:
    def __init__(self):
        self.stack = []

    def push(self, number: int) -> None:
        if not self.stack:
            self.stack.append((number, number))
        else:
            self.stack.append((number, max(self.stack[-1][1], number)))

    def pop(self) -> int:
        if not self.stack:
            return -1

        return self.stack.pop()[0]

    def max(self) -> int:
        if not self.stack:
            return -1

        return self.stack[-1][1]

    def top(self) -> int:
        if not self.stack:
            return -1

        return self.stack[-1][0]


stack = Stack()
stack.push(1)
stack.push(2)
stack.push(0)

assert stack.max() == 2
assert stack.top() == 0
assert stack.pop() == 0
assert stack.top() == 2
assert stack.pop() == 2
assert stack.max() == stack.top() == 1
