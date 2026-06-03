class Trie:
    def __init__(self) -> None:
        self.eow = False
        self.m = defaultdict(Trie)

class WordDictionary:

    def __init__(self):
        self.trie = Trie()        

    def addWord(self, word: str) -> None:
        root = self.trie
        for c in word:
            root = root.m[c]
        root.eow = True

    def search(self, word: str) -> bool:
        def dfs(i: int, root: Trie) -> bool:
            if i == len(word):
                return root.eow
            if word[i] == '.':
                res = False
                for _, t in root.m.items():
                    res |= dfs(i+1, t)
                    if res: return True
                return False
            return dfs(i+1, root.m[word[i]])
        return dfs(0, self.trie)
        
