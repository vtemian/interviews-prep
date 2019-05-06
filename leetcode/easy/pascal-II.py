class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        if not rowIndex:
            return [1]

        if rowIndex == 1:
            return [1, 1]

        result = [1, rowIndex]

        down = 2
        downIdx = 2
        n = rowIndex

        up = n
        x = (up * (n - 1)) // down

        while n - 1:
            result.append(x)

            downIdx += 1
            down *= downIdx

            n -= 1
            up *= n

            x = (up * (n - 1)) // down

        return result
