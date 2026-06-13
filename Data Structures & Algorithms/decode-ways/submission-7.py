class Solution:
    def numDecodings(self, s: str) -> int:
        dp = [0]*len(s)
        if s[0] == '0':
            return 0
        dp[0] = 1
        for i in range(1, len(s)):
            c = s[i]
            if c == '0':
                if s[i-1] < '1' or s[i-1] > '2': return 0
                dp[i] = (dp[i-2] if i-2 >= 0 else 1)
            else:
                if (i+1<len(s) and s[i + 1] == '0') or s[i-1] == '0':
                    dp[i] = dp[i-1]
                else:
                    if 0 < int(s[i-1] + c) <= 26:
                        dp[i] = dp[i-1] + (dp[i-2] if i-2 >= 0 else 1)
                    else:
                        dp[i] = dp[i-1]
            print(dp)
        return dp[-1]


            