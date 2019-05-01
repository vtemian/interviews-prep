class TwoSum:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.store = {}

    def add(self, number: int) -> None:
        """
        Add the number to an internal data structure..
        """

        if number in self.store:
            self.store[number] += 1
        else:
            self.store[number] = 1

    def find(self, value: int) -> bool:
        """
        Find if there exists any pair of numbers which sum is equal to the value.
        """

        for nr in self.store:
            rest = value - nr
            if rest in self.store and (rest != nr or self.store[rest] > 1):
                return True

        return False


# Your TwoSum object will be instantiated and called as such:
# obj = TwoSum()
# obj.add(number)
# param_2 = obj.find(value)
