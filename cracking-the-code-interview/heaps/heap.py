from typing import Union


class Heap:
    def __init__(self, size: int = 100):
        self.size = size
        self.store = []

    def insert(self, item: int) -> bool:
        if len(self.store) == self.size:
            return False

        self.store.append(item)
        self._swap_up()

    @property
    def peek(self) -> Union[int, None]:
        if not self.store:
            return None

        return self.store[0]

    def compare(self, current: int, parent: int) -> bool:
        raise NotImplementedError()

    def _swap_up(self):
        idx = len(self.store) - 1

        while idx != 0:
            parent = idx // 2

            if not self.compare(self.store[idx], self.store[parent]):
                return

            self.store[idx], self.store[parent] = self.store[parent], self.store[idx]
            idx = parent

    def __str__(self) -> str:
        return str(self.store)


class MinHeap(Heap):
    def compare(self, current: int, parent: int) -> bool:
        return current < parent


class MaxHeap(Heap):
    def compare(self, current: int, parent: int) -> bool:
        return current > parent


for use_case, expected_result in [
        ((MinHeap, 4, [4, 1, 2, 3]), 1),
        ((MaxHeap, 4, [0, 1, 2, 3]), 3),
]:
    heap_cls, size, elements = use_case
    heap = heap_cls(size)

    for element in elements:
        heap.insert(element)

    assert heap.peek == expected_result, "{} != {}".format(heap.peek, expected_result)
