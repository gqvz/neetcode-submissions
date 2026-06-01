class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        res = False
        mi = len(board[0])
        mj = len(board)
        if mi*mj < len(word): return False
        def dfs(i, j, c, cooked):
            nonlocal res
            if c == len(word) - 1 and board[j][i]==word[-1]:
                res = True
                return
            if board[j][i] != word[c]: return
            # left
            if i > 0 and (i-1, j) not in cooked:
                cooked.append((i-1, j))
                dfs(i-1, j, c+1, cooked)
                cooked.pop()
            # right
            if i < mi - 1 and (i +1, j) not in cooked:
                cooked.append((i+1, j))
                dfs(i+1, j, c+1, cooked)
                cooked.pop()
            # up
            if j > 0 and (i, j-1) not in cooked:
                cooked.append((i, j-1))
                dfs(i, j-1, c+1, cooked)
                cooked.pop()
            # down
            if j < mj - 1 and (i, j+1) not in cooked:
                cooked.append((i, j+1))
                dfs(i, j + 1, c + 1, cooked)
                cooked.pop()

        for j, row in enumerate(board):
            for i, c in enumerate(row):
                if c == word[0]:
                    dfs(i, j, 0, [])
                    if res:
                        return res
        return res