class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        mi = len(grid[0])
        mj = len(grid)

        def bfs(i: int, j: int):
            visited = set()
            q = deque()
            q.append((0, i, j))
            while q:
                dist, ni, nj = q.popleft()
                if 0 <= ni < mi and 0 <= nj < mj and (ni, nj) not in visited and grid[nj][ni] != -1:
                    visited.add((ni, nj))
                    grid[nj][ni] = min(grid[nj][ni], dist)
                    q.append((dist + 1, ni + 1, nj))
                    q.append((dist + 1, ni - 1, nj))
                    q.append((dist + 1, ni, nj + 1))
                    q.append((dist + 1, ni, nj - 1))
        for j in range(len(grid)):
            for i in range(len(grid[0])):
                if grid[j][i] == 0:
                    bfs(i, j)