class Solution:
    def intervalIntersection(self, A: List[List[int]], B: List[List[int]]) -> List[List[int]]:
        if not A or not B:
            return []

        i = j = 0
        result = []

        while i < len(A) and j < len(B):
            a_s, a_e = A[i]
            b_s, b_e = B[j]

            lo = max(a_s, b_s)
            hi = min(a_e, b_e)

            if lo <= hi:
                result.append([lo, hi])

            if a_e < b_e:
                i += 1
            else:
                j += 1

        return result
