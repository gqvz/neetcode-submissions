from functools import lru_cache
class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        @lru_cache(maxsize=None)
        def dfs(am, idx):
            if am == 0: return 1
            if am < 0 or idx >= len(coins): return 0
            return dfs(am-coins[idx], idx) + dfs(am, idx+1)

        return dfs(amount, 0)