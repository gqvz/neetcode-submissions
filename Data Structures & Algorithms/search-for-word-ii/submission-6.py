class TrieNode:
    def __init__(self):
        self.children = {}
        self.endOfWord = False

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        root = TrieNode()
        for word in words:
            cur = root
            for c in word:
                if c not in cur.children:
                    cur.children[c] = TrieNode()
                cur = cur.children[c]
            cur.endOfWord = True
        
        res = set()
        mj = len(board)
        mi = len(board[0])
        def dfs(state, i, j, node):
            if not (0 <= i < mi and 0 <= j < mj):
                return
            c = board[j][i]
            if c == '#':
                return
            state += c
            if c not in node.children:
                return
            nc = node.children[c]
            if nc.endOfWord:
                res.add(state)
            board[j][i] = '#'
            dfs(state, i-1, j, nc)
            dfs(state, i+1, j, nc)
            dfs(state, i, j-1, nc)
            dfs(state, i, j+1, nc)
            board[j][i] = c
        for j in range(mj):
            for i in range(mi):
                dfs("", i, j, root)
        return list(res)

