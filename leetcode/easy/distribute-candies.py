from collections import Counter


class Solution:
    def distributeCandies(self, candies):
        store = Counter(candies)
        return min(len(store.values()), len(candies) // 2)


for test in [[1,1,2,2,3,3], [1,1,2,3]]:
    result = Solution().distributeCandies(test)
    print(result)
