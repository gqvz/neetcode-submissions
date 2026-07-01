from functools import cache
class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        @cache
        def dfs(i, j):
            if j == len(t): return 1
            if i == len(s): return 0
            su = 0
            if s[i] == t[j]:
                su += dfs(i+1, j+1)
            su += dfs(i+1, j)
            return su
        return dfs(0, 0)

