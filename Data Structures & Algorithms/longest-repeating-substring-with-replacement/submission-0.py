class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = r = 0
        m = defaultdict(int)
        ans = 0
        while r < len(s):
            m[s[r]] += 1
            if sum(m.values()) - max(m.values()) > k:
                l += 1
                m[s[l-1]] -= 1
            r += 1
            ans = r - l

        return ans