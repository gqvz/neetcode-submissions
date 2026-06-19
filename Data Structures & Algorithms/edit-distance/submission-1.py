class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        from functools import lru_cache
        @lru_cache(maxsize=None)
        def distance(a, b):
            if a == -1: return b
            if b == -1: return a

            return min(distance(a, b-1)+1, distance(a-1, b)+1, distance(a-1, b-1) + (1 if word1[a] != word2[b] else 0))
        return distance(len(word1) - 1, len(word2) - 1) + 1