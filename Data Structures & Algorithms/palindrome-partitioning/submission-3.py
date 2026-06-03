class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        l  = [s[0]]
        def dfs(i):
            if i == len(s):
                if l[-1] == l[-1][::-1]:
                    res.append(l.copy())
                return
            if l[-1] == l[-1][::-1]:
                l.append(s[i])
                dfs(i+1)
                l.pop()
            l[-1] += (s[i])
            dfs(i+1)
            l[-1]=l[-1][:-1]
        dfs(1)

        return res
