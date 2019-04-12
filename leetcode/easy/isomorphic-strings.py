class Solution:
    def isIsomorphic(self, s: 'str', t: 'str') -> 'bool':
        mapping_s = {}
        mapping_t = {}

        if len(s) != len(t):
            return False

        idx = 0

        while idx < len(s):
            l_s = s[idx]
            l_t = t[idx]

            if l_s not in mapping_s:
                if l_t in mapping_t:
                    return False

                mapping_s[l_s] = l_t
                mapping_t[l_t] = l_s

            elif mapping_s[l_s] != l_t:
                return False

            idx += 1

        return True
