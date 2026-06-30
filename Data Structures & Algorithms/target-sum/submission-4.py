from functools import lru_cache
class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        @lru_cache(maxsize=None)
        def dfs(s, idx):
            n = nums[idx]
            if idx == len(nums) - 1:
                if n == abs(s):
                    return 2 if n == 0 else 1
                return 0
            return dfs(s-n, idx+1) + dfs(s+n, idx+1)
        return dfs(target, 0)
