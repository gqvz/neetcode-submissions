class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        def dfs(state, o, closed):
            if closed == n:
                res.append(state)
                return
            if o > closed:
                dfs(state + ")", o, closed+1)
            if o < n:
                dfs(state+"(", o +1, closed)

        dfs("", 0, 0)
        return sorted(res)
        