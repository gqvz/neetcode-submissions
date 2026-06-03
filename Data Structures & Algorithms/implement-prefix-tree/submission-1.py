class PrefixTree:
        
    def __init__(self):
        self.m = {}

    def insert(self, word: str) -> None:
        m = self.m
        if len(word) == 1:
            if word not in m:
                m[word] = (True, PrefixTree())
            else:
                p = m[word][1]
                m[word] = (True, p)
            return
        p = None
        if word[0] not in m:
            p = PrefixTree()
            m[word[0]] = (False, p)
        else:
            p = m[word[0]][1]
        p.insert(word[1:])

    def search(self, word: str) -> bool:
        if len(word) == 1:
            if word not in self.m: return False
            else: return self.m[word][0]
        if word[0] not in self.m:
            return False
        return self.m[word[0]][1].search(word[1:])

    def startsWith(self, prefix: str) -> bool:
        if len(prefix) == 1:
            return prefix in self.m
        if prefix[0] not in self.m:
            return False
        return self.m[prefix[0]][1].startsWith(prefix[1:])
 
        
        