class MyHashSet:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.store = {}

    def add(self, key: int) -> None:
        self.store[key] = True

    def remove(self, key: int) -> None:
        if key not in self.store:
            return

        self.store[key] = False

    def contains(self, key: int) -> bool:
        """
        Returns true if this set contains the specified element
        """

        return key in self.store and self.store[key]


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)
