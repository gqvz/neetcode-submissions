class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp = [()]*len(nums)
        dp[0] = (nums[0], 1)
        for i, num in enumerate(nums):
            x = [d[1] for d in dp[:i] if d[0] < num]
            dp[i] = (num, max(x, default=0) + 1)
        return max([d[1] for d in dp])

