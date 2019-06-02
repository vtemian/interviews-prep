class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """

        rows = [
            [] for _ in range(numRows)
        ]
        row = 0

        down = 1

        for idx, char in enumerate(s):
            rows[row].append(char)

            if numRows <= 1:
                continue

            row += down

            if row == 0 or row == numRows - 1:
                down *= -1

        result = [
            "".join(row) for row in rows
        ]
        return "".join(result)
