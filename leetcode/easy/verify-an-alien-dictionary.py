class Solution:
    def compute_hash(self, word, order):
        if not word:
            return []

        return [order[letter] for letter in word]

    def isAlienSorted(self, words: List[str], order: str) -> bool:
        index = {
            letter: index
            for index, letter in enumerate(order)
        }

        hashed_words = [
            self.compute_hash(word, index) for word in words
        ]

        return sorted(hashed_words) == hashed_words
