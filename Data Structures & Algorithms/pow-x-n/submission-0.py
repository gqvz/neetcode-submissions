class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n < 0:
            return 1/self.myPow(x, -n)
        res = 1
        pows = [x]
        i = 0
        while n:
            pows.append(pows[-1]*pows[-1])
            if n & 1 == 1:
                res *= pows[i]
            n >>= 1
            i += 1
        return res
