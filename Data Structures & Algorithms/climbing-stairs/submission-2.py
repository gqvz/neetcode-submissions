class Solution:
    def climbStairs(self, n: int) -> int:
        a = [1, 1] + [0] * (n-1)
        for i in range(2, n+1):
            a[i] = (a[i-1] + a[i-2])
        print(a)
        return a[n]

        