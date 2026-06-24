class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        m = {}
        def dfs(i):
            if i == len(s):
                return True
            if i in m: return m[i]
            for w in wordDict:
                if s[i:].startswith(w):
                    if dfs(i+len(w)):
                        return True
            m[i] = False
            return False
        return dfs(0)
                        