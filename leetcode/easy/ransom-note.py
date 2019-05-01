from collections import Counter


class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        magazine = Counter(magazine)

        for letter in ransomNote:
            if not magazine.get(letter):
                return False

            magazine[letter] -= 1

        return True

