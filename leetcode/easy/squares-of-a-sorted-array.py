"""
Given an array of integers A sorted in non-decreasing order, return an array of the squares of each number, also in sorted non-decreasing order.



Example 1:

Input: [-4,-1,0,3,10]
Output: [0,1,9,16,100]
Example 2:

Input: [-7,-3,2,3,11]
Output: [4,9,9,49,121]


Note:

1 <= A.length <= 10000
-10000 <= A[i] <= 10000
A is sorted in non-decreasing order.
"""


class Solution:
    def sortedSquares(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """

        negatives_index = 0
        negatives = []
        result = []

        for element in A:
            squared = element ** 2

            if element < 0:
                negatives.append(squared)
                negatives_index += 1
            else:
                while negatives_index > 0 and negatives[negatives_index - 1] < squared:
                    result.append(negatives[negatives_index - 1])
                    negatives_index -= 1
                result.append(squared)

        while negatives_index > 0:
            result.append(negatives[negatives_index - 1])
            negatives_index -= 1

        return result


result = Solution().sortedSquares([-4, -3, -2, -1, 0])
print(result)
