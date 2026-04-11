class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t) or set(s) != set(t): return False

        i = 0
        for char in s:
            i += ord(char)
        for char in t:
            i -= ord(char)
        return i == 0 