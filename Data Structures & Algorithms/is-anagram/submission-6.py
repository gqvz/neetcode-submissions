class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        l = [0] * 26
        for char in s:
            idx = ord(char) - ord('a')
            l[idx] += 1
        for char in t:
            idx = ord(char) - ord('a')
            l[idx] -= 1
        for i in l:
            if i != 0:
                return False
        return True