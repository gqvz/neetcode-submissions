class Solution:
    def longestPalindrome(self, s: str) -> str:
        ls = ""
        for i in range(len(s)):
            k = 0
            while i + k < len(s) and i - k >= 0 and s[i-k] == s[i+k]:
                if 2 * k + 1 > len(ls):
                    ls = s[i-k:i+k+1]
                k += 1
            k = 0
            if i+1 < len(s) and s[i] == s[i+1]:
                while i + k + 1 < len(s) and i - k >= 0 and s[i-k] == s[i+k+1]:
                    if 2 * k + 2 > len(ls):
                        ls = s[i-k:i+k+2]
                    k += 1
        return ls