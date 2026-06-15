class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        wds = set(wordDict)
        m = {}
        def dfs(s1):
            if s1 in wds: 
                m[s1] = True
                return True
            if s1 in m:
                return m[s1]
            for i in range(1, len(s1)+1):
                if s1[:i] in wds and (s1[i:] in wds or dfs(s1[i:])):
                    m[s1] = True
                    return True
            m[s1] = False
            return False
        return dfs(s)