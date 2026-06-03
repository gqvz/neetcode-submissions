class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        self.visited = set()
        c = 0
        for j in range(len(grid)):
            for i in range(len(grid[0])):
                if (i, j) not in self.visited and grid[j][i] == '1':
                    c += 1
                    self.bfs(i, j, grid)
        return c

    def bfs(self, i: int, j: int, grid: List[List[str]]) -> None:
        q = deque()
        q.append((i, j))
        mi = len(grid[0])
        mj = len(grid)
        while q:
            li, lj = q.popleft()
            if 0 <= li < mi and 0 <= lj < mj:
                if grid[lj][li] == '1':
                    self.visited.add((li, lj))
                    if (li + 1, lj) not in self.visited: q.append((li + 1, lj))
                    if (li - 1, lj) not in self.visited: q.append((li - 1, lj))
                    if (li, lj - 1) not in self.visited: q.append((li, lj - 1))
                    if (li, lj + 1) not in self.visited: q.append((li, lj + 1))
            
            