class Solution(object):
    def licenseKeyFormatting(self, S, K):
        """
        :type S: str
        :type K: int
        :rtype: str
        """

        S = S.upper()
        key = ''.join(S.split('-'))

        def chunks(word, chunks):
            result = []
            end = len(word)

            while end - chunks >= 0:
                result.append(word[end - chunks: end])
                end -= chunks

            if end != 0:
                result.append(word[:end])

            return result[::-1]

        return '-'.join(chunks(''.join(key), K))


result = Solution().licenseKeyFormatting('5F3Z-2e-9-w', 4)
print(result)
