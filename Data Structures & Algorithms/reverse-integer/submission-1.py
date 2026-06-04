class Solution:
    def reverse(self, x: int) -> int:
        if x == 0: return 0
        r = (x//abs(x)) * int(str(abs(x))[::-1])
        if -(2**31) <= r <= 2**31 - 1: return r
        return 0