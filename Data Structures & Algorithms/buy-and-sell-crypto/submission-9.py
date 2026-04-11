class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        m = 0
        t = len(prices)
        k = [0]*t
        r = 0
        for i, n in enumerate(prices[::-1]):
            x = (m := max(m,n)) - prices[t - 1 - i]
            r = max(r, x)
        return r
    
