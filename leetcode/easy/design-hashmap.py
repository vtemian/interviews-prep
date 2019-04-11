class MyHashMap(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """

        self.store = []

        self.size = 32
        for _ in range(self.size):
            self.store.append([])

        self.count = 0

    def hash(self, key):
        return key % self.size

    def _resize(self):
        self._current_store = [
            mark
            for buckets in self.store
            for mark in buckets
        ]

        self.store = []
        self.size *= 32
        for _ in range(self.size):
            self.store.append([])

        for mark in self._current_store:
            self.put(*mark)

    def put(self, key, value):
        """
        value will always be non-negative.
        :type key: int
        :type value: int
        :rtype: None
        """

        mark = self._get_pair(key)
        bucket = self.store[self.hash(key)]

        if mark:
            self.count -= 1
            bucket.remove(mark)

        bucket.append((key, value))
        self.count += 1

        if self.count > self.size:
            self._resize()

    def _get_pair(self, key):
        hash = self.hash(key)
        bucket = self.store[hash]

        mark = None
        for k, v in bucket:
            if k == key:
                mark = (k, v)
                break

        return mark

    def get(self, key):
        """
        Returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key
        :type key: int
        :rtype: int
        """

        mark = self._get_pair(key)
        return mark[1] if mark else -1

    def remove(self, key):
        """
        Removes the mapping of the specified value key if this map contains a mapping for the key
        :type key: int
        :rtype: None
        """

        mark = self._get_pair(key)
        if not mark:
            return

        bucket = self.store[self.hash(key)]
        bucket.remove(mark)

        self.count -= 1


obj = MyHashMap()
obj.put(1, 2)

param_2 = obj.get(1)
obj.remove(1)

print(param_2)
