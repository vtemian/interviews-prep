# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):

class Solution:
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """

        start = 0
        end = n

        while start <= end:
            avg = (start + end) // 2

            bad = isBadVersion(avg)
            if bad:
                end = avg - 1
            else:
                start = avg + 1

        return start
