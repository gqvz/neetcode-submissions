class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        l = 0
        r = len(s1)
        k = sorted(s1)
        while r <=len(s2):
            if sorted(s2[l:r]) == k:
                return True
            r += 1
            l += 1
        return False