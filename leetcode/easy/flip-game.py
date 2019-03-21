class Solution:
    def generatePossibleNextMoves(self, s: 'str') -> 'List[str]':
        results = []
        index = 0

        while index + 1 < len(s):
            if s[index] == s[index + 1] == '+':
                results.append(s[:index] + '--' + s[index + 2:])
            index += 1

        return results
