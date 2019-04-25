class Solution:
    def shortestDistance(self, words: List[str], word1: str, word2: str) -> int:
        min_distance = len(words)
        w_1_idx = w_2_idx = len(words)

        for idx, word in enumerate(words):
            if word == word1:
                w_1_idx = idx
                min_distance = min(min_distance, abs(idx - w_2_idx))
            if word == word2:
                w_2_idx = idx
                min_distance = min(min_distance, abs(idx - w_1_idx))

        return min_distance
