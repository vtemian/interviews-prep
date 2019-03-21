from collections import Counter


class Solution:
    def canPermutePalindrome(self, s):
        store = Counter(s)

        is_odd = False
        for no_letter in store.values():
            if no_letter % 2 == 1:
                if is_odd:
                    return False
                is_odd = True
        return True
