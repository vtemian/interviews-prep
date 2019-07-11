class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """

        end = m + n - 1
        m -= 1
        n -= 1

        while end >= 0:
            if n < 0:
                break

            if m < 0 or nums2[n] >= nums1[m]:
                nums1[end] = nums2[n]
                n -= 1
            else:
                nums1[end] = nums1[m]
                m -= 1

            end -= 1
