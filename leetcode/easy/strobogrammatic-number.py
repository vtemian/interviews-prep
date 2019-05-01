class Solution:
    def isStrobogrammatic(self, num: str) -> bool:
        strobogrammatic = {
            '1': '1',
            '0': '0',
            '6': '9',
            '9': '6',
            '8': '8'
        }

        for idx, digit in enumerate(num):
            if digit not in strobogrammatic or strobogrammatic[digit] != num[len(num) - idx -1]:
                return False

        return True
