class TrieNode:
    def __init__(self):
        self.children = {}
        self.endOfWord = False

class PrefixTree:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        cur = self.root
        for c in word:
            if c not in cur.children:
                cur.children[c] = TrieNode()
            cur = cur.children[c]
        cur.endOfWord = True

    def search(self, word: str) -> bool:
        cur = self.root
        for c in word:
            if c not in cur.children:
                return False
            cur = cur.children[c]
        return cur.endOfWord

    def startsWith(self, prefix: str) -> bool:
        cur = self.root
        for c in prefix:
            if c not in cur.children:
                return False
            cur = cur.children[c]
        return True

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        trie = PrefixTree()
        for word in words:
            trie.insert(word)
        
        res = set()
        mj = len(board)
        mi = len(board[0])
        def dfs(state, i, j):
            if not (0 <= i < mi and 0 <= j < mj):
                return
            if board[j][i] == '#':
                return
            state += board[j][i]
            if not trie.startsWith(state):
                return
            if trie.search(state):
                res.add(state)
            t = board[j][i]
            board[j][i] = '#'
            dfs(state, i-1, j)
            dfs(state, i+1, j)
            dfs(state, i, j-1)
            dfs(state, i, j+1)
            board[j][i] = t
        for j in range(mj):
            for i in range(mi):
                dfs("", i, j)
        return list(res)

