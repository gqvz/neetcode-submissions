class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        m = l = r = 0
        d = {}
        while r < len(s):
            if s[r] not in d:
                d[s[r]] = r
                r += 1
                m = max(m, r - l)
            else:
                l = d[s[r]] + 1
                d = {k: v for k, v in d.items() if v >= l}
        return m