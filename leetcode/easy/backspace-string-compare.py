class Solution(object):
    def backspaceCompare(self, S, T):
        """
        :type S: str
        :type T: str
        :rtype: bool
        """

        def clean(string):
            result = []
            idx = 0

            for letter in string:
                if letter == '#':
                    idx = max(0, idx - 1)
                else:
                    if idx == len(result):
                        idx += 1
                        result.append(letter)
                    else:
                        result[idx] = letter
                        idx += 1
            return ''.join(result[:idx])

        return clean(S) == clean(T)
