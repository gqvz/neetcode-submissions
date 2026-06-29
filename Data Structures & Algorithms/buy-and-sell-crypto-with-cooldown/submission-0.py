from functools import lru_cache
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        @lru_cache(maxsize=None)
        def dfs(coin, idx, m):
            if idx >= len(prices):
                return m
            nm = 0
            if coin:
                nm = max(nm, dfs(False, idx+2, m+prices[idx])) # sell
                nm = max(nm, dfs(True, idx+1, m)) # dont sell
            else:
                nm = max(nm, dfs(True, idx+1, m-prices[idx])) # buy
                nm = max(nm, dfs(False, idx+1, m)) # dont buy

            return nm
        return dfs(False, 0, 0)