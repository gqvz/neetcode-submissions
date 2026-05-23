class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        lo, hi = 1, max(piles)
        mid = 0
        bm = hi
        while lo <= hi:
            mid = (hi + lo) >> 1
            hn = sum(map(lambda x: math.ceil(x / mid), piles))
            if hn <= h and mid < bm:
                bm = mid
            if hn > h: lo = mid + 1
            else: hi = mid - 1
        return bm
