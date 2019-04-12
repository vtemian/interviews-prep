class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1

        nums1 = sorted(nums1)
        nums2 = sorted(nums2)

        i = j = 0
        results = []

        while j < len(nums2) and i < len(nums1):
            if nums2[j] == nums1[i]:
                results.append(nums1[i])
                i += 1
                j += 1
            elif nums1[i] > nums2[j]:
                j += 1
            else:
                i += 1

        return results
