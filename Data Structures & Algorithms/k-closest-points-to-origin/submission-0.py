class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        p = [(-x[0]**2 - x[1]**2, x) for x in points]
        heapq.heapify(p)
        while len(p) > k:
            heapq.heappop(p)
        return [x[1] for x in p]