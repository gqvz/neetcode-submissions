class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        if len(text1) > len(text2):
            text1, text2 = text2, text1
        m, n = len(text1), len(text2)
        dp = [[0]*m for _ in range(n)]
        print(m, n)

        for ni in range(n):
            for mi in range(m):
                # print(text2[ni], text1[mi], ni, mi, dp, dp[max(0, ni-1)][max(mi-1, 0)])
                if text1[mi] == text2[ni]:
                    dp[ni][mi] = dp[max(0, ni-1)][max(mi-1, 0)] + 1
                else: 
                    dp[ni][mi] = max(dp[max(0, ni-1)][mi], dp[ni][max(mi-1, 0)])
        return min(m, n, dp[-1][-1])