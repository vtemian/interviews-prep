class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = {}

        for str in strs:
            key = ''.join(sorted(str))

            if key not in anagrams:
                anagrams[key] = []

            anagrams[key].append(str)

        return list(anagrams.values())
