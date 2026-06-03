class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        area = 0
        for j in range(len(grid)):
            for i in range(len(grid[0])):
                if grid[j][i] == 1:
                    area = max(area, self.bfs(i, j, grid))
        return area

    def bfs(self, i: int, j: int, grid: List[List[int]]) -> int:
        q = deque()
        q.append((i, j))
        mi = len(grid[0])
        mj = len(grid)
        area = 0
        while q:
            li, lj = q.popleft()
            if 0 <= li < mi and 0 <= lj < mj and grid[lj][li] == 1:
                grid[lj][li] = 0
                area += 1
                q.append((li + 1, lj))
                q.append((li - 1, lj))
                q.append((li, lj - 1))
                q.append((li, lj + 1))
        return area
