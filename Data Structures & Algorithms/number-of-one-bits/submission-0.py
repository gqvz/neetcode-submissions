class Solution:
    def hammingWeight(self, n: int) -> int:
        i = 0
        while n:
            if n & 1 == 1:
                i += 1
            n >>= 1
        return i