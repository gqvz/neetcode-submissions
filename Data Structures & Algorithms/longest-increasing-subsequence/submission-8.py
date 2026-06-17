class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp = [()]*len(nums)
        m = 0
        for i, num in enumerate(nums):
            dp[i] = (num, max([d[1] for d in dp[:i] if d[0] < num], default=0) + 1)
            m = max(dp[i][1], m)
        return m

