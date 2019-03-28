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

    def extract(self) -> Union[int, None]:
        if self.peek is None:
            return None

        item = self.store[0]

        if len(self.store) == 1:
            return item

        self.store[0] = self.store[-1]
        self.store = self.store[:-1]

        self._swap_down()

        return item

    def compare(self, current: int, parent: int) -> bool:
        raise NotImplementedError()

    def _swap_down(self):
        idx = 0

        """
        0 1 2 3 4 5 6 7 8
        """

        while 2 * idx < len(self.store):
            left = right = None

            if 2 * idx + 1 < len(self.store):
                left = self.store[2 * idx + 1]
            if 2 * idx + 2 < len(self.store):
                right = self.store[2 * idx + 2]

            if left is None and right is None:
                return True

            if left and self.compare(left, self.store[idx]):
                self.store[idx], self.store[2 * idx + 1] = self.store[2 * idx + 1], self.store[idx]
                idx = 2 * idx + 1
            elif right and self.compare(right, self.store[idx]):
                self.store[idx], self.store[2 * idx + 2] = self.store[2 * idx + 2], self.store[idx]
                idx = 2 * idx + 2
            else:
                return True

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
        ((MinHeap, 4, [4, 1, 2, 3]), [1, 2, 3, 4]),
        ((MaxHeap, 4, [0, 1, 2, 3]), [3, 2, 1, 0]),
]:
    heap_cls, size, elements = use_case
    heap = heap_cls(size)

    for element in elements:
        heap.insert(element)

    sorted_items = [heap.extract() for _ in range(size)]
    assert sorted_items == expected_result, "{} != {}".format(sorted_items, expected_result)
