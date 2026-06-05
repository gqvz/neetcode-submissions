class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        s = 0
        ms = 0
        for num in nums:
            s += num
            if s < 0: 
                s = 0
            ms = max(ms,s)
        return ms if ms != 0 else max(nums)
