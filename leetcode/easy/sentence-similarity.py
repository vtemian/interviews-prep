class Solution(object):
    def areSentencesSimilar(self, words1, words2, pairs):
        """
        :type words1: List[str]
        :type words2: List[str]
        :type pairs: List[List[str]]
        :rtype: bool
        """

        if len(words1) != len(words2):
            return False

        pairs_in = {}
        pairs_re = {}

        for word in pairs:
            if word[0] not in pairs_in:
                pairs_in[word[0]] = set()

            if word[1] not in pairs_re:
                pairs_re[word[1]] = set()

            pairs_in[word[0]].add(word[1])
            pairs_re[word[1]].add(word[0])

        for idx, word in enumerate(words1):
            if words2[idx] == word:
                continue

            if words2[idx] in pairs_in.get(word, set()):
                continue

            if words2[idx] in pairs_re.get(word, set()):
                continue

            return False

        return True
