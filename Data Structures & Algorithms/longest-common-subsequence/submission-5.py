class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        memo = {}
        def dfs(i, j):
            if i < 0 or j < 0:
                return 0
            if (i, j) in memo:
                return memo[i, j]
            if text1[i] == text2[j]:
                ret = memo[i, j] = dfs(i-1, j-1)+1
                return ret
            ret = memo[i, j] = max(dfs(i-1, j), dfs(i, j-1))
            return ret
        return dfs(len(text1)-1, len(text2)-1)
