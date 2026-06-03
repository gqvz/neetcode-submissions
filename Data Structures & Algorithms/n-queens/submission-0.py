class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        res=[]
        gonecols = []
        gonediasplus = []
        gonediasminu = []
        l = []
        def dfs(j):
            if j == n:
                res.append(l.copy())
                return
            for i in range(n):
                if i not in gonecols and i+j not in gonediasplus and j - i not in gonediasminu:
                    gonecols.append(i)
                    gonediasplus.append(i+j)
                    gonediasminu.append(j-i)
                    l.append("."*i+"Q"+"."*(n-i-1))
                    dfs(j+1)
                    gonecols.pop()
                    gonediasplus.pop()
                    gonediasminu.pop()
                    l.pop()
        dfs(0)
        return res


