from collections import Counter


class Solution:
    def mostCommonWord(self, paragraph : str, banned: List[str]) -> str:
        paragraph = paragraph.lower()
        banned = set(banned)

        for letter in "!?',;.":
            paragraph = paragraph.replace(letter, " ")

        indecies = sorted(list(Counter(paragraph.split()).items()), key=lambda x: -x[1])
        for word in indecies:
            if word[0] not in banned:
                return word[0]

        return ""
