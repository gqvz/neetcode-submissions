class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        m = r = 0
        for i, n in enumerate(prices[::-1]):
            m = max(m, n)
            r = max(r, m - prices[~i])
        return r
