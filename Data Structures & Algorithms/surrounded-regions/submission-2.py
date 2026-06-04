class Solution:
    def solve(self, board: List[List[str]]) -> None:
        mi = len(board[0])
        mj = len(board)
        for i in range(mi):
            if board[0][i] == 'O':
                self.bfs(i, 0, board)
            if board[-1][i] == 'O':
                self.bfs(i, mj-1, board)
        for j in range(1, mj-1):
            if board[j][0] == 'O':
                self.bfs(0, j, board)
            if board[j][-1] == 'O':
                self.bfs(mi-1, j, board)
        for j in range(mj):
            for i in range(mi):
                if board[j][i] == 'O':
                    board[j][i] = 'X'
                elif board[j][i] == 'W':
                    board[j][i] = 'O'

    def bfs(self, i: int, j: int, grid: List[List[str]]):
        q = deque()
        q.append((i, j))
        mi = len(grid[0])
        mj = len(grid)
        while q:
            li, lj = q.popleft()
            if 0 <= li < mi and 0 <= lj < mj and grid[lj][li] == 'O':
                grid[lj][li] = "W"
                q.append((li + 1, lj))
                q.append((li - 1, lj))
                q.append((li, lj - 1))
                q.append((li, lj + 1))
 