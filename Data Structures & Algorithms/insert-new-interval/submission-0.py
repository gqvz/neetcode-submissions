class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        intervals.append(newInterval)
        return self.merge(intervals)
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        res = []
        heap = []
        for interval in intervals:
            heapq.heappush(heap, (interval[0], 0))
            heapq.heappush(heap, (interval[1], 1))
        oc = 0
        while heap:
            v, e = heapq.heappop(heap)
            # print("GOT", v, e)
            if e == 0:
                # print("OPENING", oc)
                oc += 1
                if oc == 1:
                    res.append([v])
            elif e == 1:
                # print("CLOSING", oc)
                oc -= 1
                if oc == 0:
                    # print("APPEND")
                    res[-1].append(v)
        return res
 