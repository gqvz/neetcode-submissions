class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        visited = set()
        words = set(wordList)
        q = deque()
        q.append(beginWord)
        c = 0

        def distance(a: str, b: str) -> int:
            return len(a) - sum([1 for i in range(len(a)) if a[i] == b[i]])

        while q:
            for _ in range(len(q)):
                k = q.popleft()
                visited.add(k)
                for word in words - visited:
                    if distance(k, word) == 1:
                        q.append(word)
                if k == endWord:
                    return c + 1
            c += 1
        return 0
