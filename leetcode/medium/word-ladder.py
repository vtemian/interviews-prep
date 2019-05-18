from collections import defaultdict


class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if not beginWord or not endWord or endWord not in wordList:
            return 0

        store = defaultdict(list)

        for word in wordList:
            for idx in range(len(beginWord)):
                store[word[:idx] + '*' + word[idx + 1:]].append(word)

        queue = [(beginWord, 1)]
        visited = set([beginWord])

        while queue:
            word, level = queue.pop(0)

            for idx in range(len(word)):
                mid_word = word[:idx] + '*' + word[idx + 1:]

                for w in store[mid_word]:
                    if w == endWord:
                        return level + 1

                    if w not in visited:
                        visited.add(w)
                        queue.append((w, level + 1))

                store[mid_word] = []

        return 0
