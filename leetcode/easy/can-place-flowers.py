class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        result = 0
        idx = 0
        r = len(flowerbed)

        while idx < r:
            if flowerbed[idx] == 0 and (idx == 0 or flowerbed[idx - 1] == 0) and (idx == r - 1 or flowerbed[idx + 1] == 0):
                flowerbed[idx] = 1
                result += 1

            if result >= n:
                return True

            idx += 1

        return result >= n
