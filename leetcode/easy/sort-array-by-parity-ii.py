"""
Given an array A of non-negative integers, half of the integers in A are odd, and half of the integers are even.

Sort the array so that whenever A[i] is odd, i is odd; and whenever A[i] is even, i is even.

You may return any answer array that satisfies this condition.



Example 1:

Input: [4,2,5,7]
Output: [4,5,2,7]
Explanation: [4,7,2,5], [2,5,4,7], [2,7,4,5] would also have been accepted.


Note:

2 <= A.length <= 20000
A.length % 2 == 0
"""


class Solution:
    def sortArrayByParityII(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """

        is_even = lambda x: x % 2 == 0

        odd = 0
        while odd < len(A):
            if is_even(A[odd]):
                odd += 1
                continue

            if is_even(odd):
                break

            odd += 1

        even = 0
        while even < len(A):
            if not is_even(A[even]):
                even += 1
                continue

            if not is_even(even):
                break

            even += 1

        start = 0
        while start < len(A):
            if start % 2 != A[start] % 2:
                A[even], A[odd] = A[odd], A[even]

                while odd < len(A):
                    if is_even(A[odd]):
                        odd += 1
                        continue

                    if is_even(odd):
                        break

                    odd += 1

                while even < len(A):
                    if not is_even(A[even]):
                        even += 1
                        continue

                    if not is_even(even):
                        break

                    even += 1

            start += 1

        return A


result = Solution().sortArrayByParityII([4,1,1,0,1,0])
print(result)
