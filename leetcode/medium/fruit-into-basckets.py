from collections import Counter


class Solution:
    def totalFruit(self, tree: List[int]) -> int:
        result = start = 0
        store = Counter()

        for idx, value in enumerate(tree):
            store[value] += 1

            while len(store) >= 3:
                store[tree[start]] -= 1

                if store[tree[start]] == 0:
                    del store[tree[start]]

                start += 1

            result = max(result, idx - start + 1)

        return result
