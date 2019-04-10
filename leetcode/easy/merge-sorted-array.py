class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """

        k = m + n - 1
        m -= 1
        n -= 1

        while m >= 0 and n >= 0:
            _next = None

            if nums1[m] > nums2[n]:
                _next = nums1[m]
                m -= 1
            else:
                _next = nums2[n]
                n -= 1

            nums1[k] = _next

            k -= 1

        while n >= 0:
            nums1[k] = nums2[n]
            k -= 1
            n -= 1
