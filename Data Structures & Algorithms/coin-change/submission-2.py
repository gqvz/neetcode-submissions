class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount == 0: return 0
        m = min(coins)
        if amount < m: return -1
        dp = {}
        for i in range(1, amount+1):
            for c in coins:
                # print(i, c, dp)
                if i == c:
                    dp[i] = 1
                    break
                elif i - c > 0:
                    if i - c in dp:
                        if i in dp:
                            dp[i] = min(dp[i], dp[i-c] + 1)
                        else:
                            dp[i] = dp[i-c] + 1
        # print(dp)
        return dp[amount] if amount in dp else -1
            
