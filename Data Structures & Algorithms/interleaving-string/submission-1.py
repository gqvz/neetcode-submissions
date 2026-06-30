from functools import cache
class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if len(s1) + len(s2) != len(s3): return False
        @cache
        def dfs(i1, i2):
            if i1 == len(s1): return s2[i2:] == s3[i1+i2:]
            if i2 == len(s2): return s1[i1:] == s3[i1+i2:]
            c = s3[i1+i2]
            if c == s1[i1] == s2[i2]:
                return dfs(i1+1, i2) or dfs(i1, i2+1)
            elif c == s1[i1]:
                return dfs(i1+1, i2)
            elif c == s2[i2]:
                return dfs(i1, i2+1)
            return False
        return dfs(0, 0)