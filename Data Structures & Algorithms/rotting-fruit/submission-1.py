class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        mi = len(grid[0])
        mj = len(grid)
        
        q = deque()
        for j in range(mj):
            for i in range(mi):
                if grid[j][i] == 2:
                    q.append((i, j))
                    grid[j][i] = 1
        time = 0
        while q:
            for i in range(len(q)):
                ri, rj = q.popleft()
                if 0 <= ri < mi and  0 <= rj < mj and grid[rj][ri] == 1:
                    grid[rj][ri] = 2
                    q.append((ri + 1, rj))
                    q.append((ri - 1, rj))
                    q.append((ri, rj - 1))
                    q.append((ri, rj + 1))

            time += 1
        for j in range(mj):
            for i in range(mi):
                if grid[j][i] == 1:
                    return -1
        return max(0, time - 2)
