"""
Let's call an array A a mountain if the following properties hold:

A.length >= 3
There exists some 0 < i < A.length - 1 such that A[0] < A[1] < ... A[i-1] < A[i] > A[i+1] > ... > A[A.length - 1]
Given an array that is definitely a mountain, return any i such that
A[0] < A[1] < ... A[i-1] < A[i] > A[i+1] > ... > A[A.length - 1].

Example 1:

Input: [0,1,0]
Output: 1
Example 2:

Input: [0,2,1,0]
Output: 1
Note:

3 <= A.length <= 10000
0 <= A[i] <= 10^6
A is a mountain, as defined above.
"""


class Solution:
    def peakIndexInMountainArray(self, A):
        """
        :type A: List[int]
        :rtype: int
        """


        if len(A) < 3:
            return 0

        current_peak = peak = 1
        max_peak = A[peak]

        while current_peak < len(A) - 1:
            if A[current_peak - 1] < A[current_peak] and A[current_peak + 1] < A[current_peak]:

                if max_peak < A[current_peak]:
                    max_peak = A[current_peak]
                    peak = current_peak

            current_peak += 1

        return peak


result = Solution().peakIndexInMountainArray([3,4,5,1])
print(result)
