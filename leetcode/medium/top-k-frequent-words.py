from collections import Counter


class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        if not words:
            return words

        if not k:
            return []

        index = sorted(Counter(words).items(), key=lambda word: (-word[1], word[0]))

        return [
            word[0]
            for word in index[:k]
        ]
