class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        store = set()

        for num in nums:
            if num in store:
                return True

            store.add(num)

        return False
