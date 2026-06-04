class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        dp = [0]*len(cost)
        for i in range(2, len(cost)):
            dp[i] = min(dp[i-1] + cost[i-1], dp[i-2] + cost[i-2])
        return min(cost[-1] + dp[-1], cost[-2] + dp[-2])