from functools import lru_cache
class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        @lru_cache(maxsize=None)
        def dfs(s, idx):
            if idx == len(nums) - 1:
                if nums[idx] == abs(s):
                    return 2 if nums[idx] == 0 else 1
                return 0
            return dfs(s-nums[idx], idx+1) + dfs(s+nums[idx], idx+1)
        return dfs(target, 0)
