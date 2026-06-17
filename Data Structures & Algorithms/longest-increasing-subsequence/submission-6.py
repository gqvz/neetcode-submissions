class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp = [()]*len(nums)
        dp[0] = (nums[0], 1)
        for i, num in enumerate(nums):
            x = [d[1] for d in dp[:i] if d[0] < num]
            if x:
                dp[i] = (num, max(x) + 1)
            else:
                dp[i] = (num, 1)
        return max([d[1] for d in dp])

