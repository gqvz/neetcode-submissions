class Solution:
    def countSubstrings(self, s: str) -> int:
        ls = 0
        for i in range(len(s)):
            k = 0
            while i + k < len(s) and i - k >= 0 and s[i-k] == s[i+k]:
                ls += 1
                k += 1
            k = 0
            if i+1 < len(s) and s[i] == s[i+1]:
                while i + k + 1 < len(s) and i - k >= 0 and s[i-k] == s[i+k+1]:
                    ls += 1
                    k += 1
        return ls