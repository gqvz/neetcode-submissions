class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if set(s) != set(t): return False

        i = 0
        for char in s:
            i += ord(char)
        for char in t:
            i -= ord(char)
        return i == 0 