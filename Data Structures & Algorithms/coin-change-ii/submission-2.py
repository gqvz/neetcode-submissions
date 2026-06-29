class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        memo = {}
        def dfs(am, idx):
            if am == 0:
                memo[am, idx] = 1
                return 1
            if am < 0 or idx >= len(coins): return 0
            if (am, idx) in memo: return memo[am, idx]
            ret = dfs(am-coins[idx], idx) + dfs(am, idx+1)
            memo[am, idx] = ret
            return ret

        return dfs(amount, 0)