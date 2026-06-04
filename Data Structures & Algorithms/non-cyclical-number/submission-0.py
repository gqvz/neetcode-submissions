class Solution:
    def isHappy(self, n: int) -> bool:
        m = {n:True}
        while n != 1:
            n = sum([int(x)**2 for x in str(n)])
            if n in m:
                return False
            m[n] = True
        return True