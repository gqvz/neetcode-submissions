class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        m = 0
        t = len(prices)
        k = [0]*t
        for i, n in enumerate(prices[::-1]):
            k[i] = (m := max(m,n)) - prices[t - 1 - i]
        return max(k)
    
