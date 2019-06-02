class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        if not s or not wordDict:
            return False

        wordDict = set(wordDict)

        queue = [0]
        visited = [False] * len(s)

        while queue:
            current = queue.pop(0)
            if visited[current]:
                continue

            start = current
            while start < len(s):

                if s[current: start + 1] in wordDict:

                    if start + 1 == len(s):
                        return True

                    queue.append(start + 1)

                start += 1

            visited[current] = True

        return False
