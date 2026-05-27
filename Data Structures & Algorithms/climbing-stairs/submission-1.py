class Solution:
    def climbStairs(self, n: int) -> int:
        a = [1, 1, 2]
        for _ in range(n):
            a.append(a[-1] + a[-2])
        return a[n]

        