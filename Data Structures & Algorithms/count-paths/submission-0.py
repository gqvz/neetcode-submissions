class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        facs = {0:1}
        for i in range(1, m+n-1):
            facs[i] = i*facs[i-1]
        return facs[m+n-2]//(facs[n-1]*facs[m-1])
