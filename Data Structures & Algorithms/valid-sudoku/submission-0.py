class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for i in range(9):
            row = [board[i][x] for x in range(9) if board[i][x] != '.']
            if len(set(row)) != len(row):
                return False
            col = [board[x][i] for x in range(9) if board[x][i] != '.']
            if len(set(col)) != len(col):
                return False
        for i in range(3):
            for j in range(3):
                k = [board[y][x] for y in range(3 * i, 3 * i + 3) for x in range(3*j, 3*j + 3) if board[y][x] != '.']
                if len(set(k)) != len(k):
                    return False
        return True


