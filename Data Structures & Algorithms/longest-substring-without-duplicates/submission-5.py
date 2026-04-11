class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0
        m = 1
        d = {}
        l = 0
        r = 0
        while r < len(s):
            if s[r] not in d:
                d[s[r]] = r
                r += 1
                m = max(m, r - l)
            else:
                l = d[s[r]] + 1
                d = {k: v for k, v in d.items() if v >= l}
        return m