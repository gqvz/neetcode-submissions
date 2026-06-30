from functools import lru_cache
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        @lru_cache(maxsize=None)
        def dfs(coin, idx):
            if idx >= len(prices):
                return 0
            if coin:
                return max(prices[idx] + dfs(False, idx+2), #sell 
                dfs(True, idx+1)) # dont sell
            else:
                return max(-prices[idx] + dfs(True, idx+1), # buy 
                dfs(False, idx+1)) # dont buy
        return dfs(False, 0)
