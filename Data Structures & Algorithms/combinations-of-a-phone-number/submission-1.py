class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        res = []
        if not digits:
            return res
        m = {
            '2':'abc',
            '3':'def',
            '4':'ghi',
            '5':'jkl',
            '6':'mno',
            '7':'pqrs',
            '8':'tuv',
            '9':'wxyz'
        }
        def dfs(s, i):
            if i == len(digits):
                res.append(s.copy())
                return
            for c in m[digits[i]]:
                s.append(c)
                dfs(s, i+1)
                s.pop()
        dfs([], 0)
        return [''.join(x) for x in res]