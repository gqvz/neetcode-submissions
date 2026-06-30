from functools import cache
class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        dirs = [[0,1], [0, -1], [1, 0], [-1, 0]]
        mj = len(matrix)
        mi = len(matrix[0])
        @cache
        def dfs(i, j):
            m = 0
            for d in dirs:
                ni, nj = i + d[0], j + d[1]
                if 0 <= ni < mi and 0 <= nj < mj and matrix[nj][ni] > matrix[j][i]:
                    m = max(m, dfs(ni, nj))
            return 1 + m
        rm = 0
        for j in range(mj):
            for i in range(mi):
                rm = max(rm, dfs(i, j))
        return rm 


                    