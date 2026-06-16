class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        visited = {}
        q = [(grid[0][0], 0, 0)]
        m = len(grid)
        ds = [(0, 1), (0, -1), (-1, 0), (1, 0)]
        while q:
            c, i, j = heapq.heappop(q)
            visited[(i, j)] = c
            if i == j == m - 1:
                break
            for d in ds:
                ni, nj = i + d[0], j + d[1]
                if 0 <= ni < m and 0 <= nj < m and (ni, nj) not in visited:
                    heapq.heappush(q, (grid[nj][ni], ni, nj))
            # print(q)
        return max(visited.values())

