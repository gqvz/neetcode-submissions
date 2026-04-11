class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        k = []
        m = 0
        t = len(prices)
        for i, n in enumerate(prices[::-1]):
            k.append((m := max(m,n)) - prices[t - 1 - i])
        return max(k)
    
