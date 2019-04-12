class Solution:
    def isMonotonic(self, A: List[int]) -> bool:
        if len(A) < 2:
            return True

        up = A[1] - A[0]
        idx = 2

        while idx < len(A):
            direction = A[idx] - A[idx - 1]
            if not up:
                up = direction

            if direction > 0 and up < 0:
                return False
            elif direction < 0 and up > 0:
                return False

            idx += 1

        return True
