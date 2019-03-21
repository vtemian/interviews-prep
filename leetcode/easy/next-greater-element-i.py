class Solution:
    def nextGreaterElement(self, nums1: 'List[int]', nums2: 'List[int]') -> 'List[int]':
        stack = []
        next_greatest = {}

        for number in nums2:
            while stack and stack[-1] < number:
                next_greatest[stack.pop()] = number
            stack.append(number)

        while stack:
            next_greatest[stack.pop()] = -1

        return [
            next_greatest[number]
            for number in nums1
        ]
