class Solution:
    def solve(self, board: List[List[str]]) -> None:
        mi = len(board[0])
        mj = len(board)
        for i in range(mi):
            jr = range(mj) if i == 0 or i == mi - 1 else [0, mj-1]
            for j in jr:
                if board[j][i] == 'O':
                    self.bfs(i, j, board)
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
 