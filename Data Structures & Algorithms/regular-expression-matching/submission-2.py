class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        def dfs(i, j):
            if j == len(p) and i == len(s): return True
            if i == len(s): return p[-1] == '*'
            if j == len(p): return False
            if j == len(p)-1:
                return (p[j] == '.' or p[j] == s[i]) and i == len(s)-1

            if p[j+1] == '*':
                if p[j] == '.':
                    return dfs(i+1, j) or dfs(i, j+2)
                else:
                    return ((p[j] == s[i]) and dfs(i+1, j)) or dfs(i, j+2)
            return (p[j] == '.' or p[j] == s[i]) and dfs(i+1, j+1)
        return dfs(0, 0)