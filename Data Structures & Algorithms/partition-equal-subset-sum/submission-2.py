class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        su = sum(nums)
        if su % 2 == 1: return False
        hs = su // 2
        memo = {}
        def dfs(cur, i):
            if cur == hs: return True
            if i == len(nums) - 1: return False
            if (cur, i) in memo:
                return memo[cur, i]
            if dfs(cur + nums[i], i+1) or dfs(cur, i+1):
                return True
            memo[cur,i] = False
            return False
        return dfs(0, 0)