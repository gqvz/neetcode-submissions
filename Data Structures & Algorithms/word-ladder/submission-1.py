class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        words = set(wordList)
        if endWord not in words: return 0
        q = deque([beginWord])
        visited = {beginWord}
        c = 1

        while q:
            for _ in range(len(q)):
                k = q.popleft()
                if k == endWord: return c
                for i in range(len(k)):
                    for ch in 'abcdefghijklmnopqrstuvwxyz':
                        nb = k[:i] + ch + k[i+1:]
                        if nb in words and nb not in visited:
                            visited.add(nb)
                            q.append(nb)
            c += 1
        return 0