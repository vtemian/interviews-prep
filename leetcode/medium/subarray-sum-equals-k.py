class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        if not nums:
            return 0
        
        result = 0
        current = 0
        sums = {0: 1}
        
        for num in nums:
            current += num
            
            if current - k in sums:
                result += sums[current - k]
            
            sums[current] = sums.get(current, 0) + 1
            
        return result
