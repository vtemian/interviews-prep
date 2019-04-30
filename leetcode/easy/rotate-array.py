class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        k = k % n

        start = 0
        count = 0

        while count < n:
            current = start
            prev = nums[current]

            next = (current + k) % n
            temp = nums[next]
            nums[next], prev = prev, nums[next]
            current = next
            prev = temp
            count += 1


            while start != current:
                next = (current + k) % n
                temp = nums[next]
                nums[next], prev = prev, nums[next]
                current = next
                prev = temp

                count += 1

            start += 1
