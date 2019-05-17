from random import randint


class RandomizedSet:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.store = {}
        self.random_set = set()
        self.random_store = {}
        self.count = 1

    def insert(self, val: int) -> bool:
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        """
        if self.store.get(val):
            return False

        self.store[val] = self.count
        self.random_store[self.count] = val
        self.count += 1
        return True

    def remove(self, val: int) -> bool:
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        """
        if not val in self.store:
            return False

        count = self.store[val]
        del self.store[val]
        del self.random_store[count]
        return True

    def getRandom(self) -> int:
        """
        Get a random element from the set.
        """

        key = randint(1, self.count)
        while key not in self.random_store:
            key = randint(1, self.count)

        return self.random_store[key]


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
