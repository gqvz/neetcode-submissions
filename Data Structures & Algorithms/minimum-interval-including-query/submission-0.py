class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        intervals.sort(key=lambda x: (x[1]-x[0], x[0]))
        res = [0]*len(queries)
        for c, q in enumerate(queries):
            for i in intervals:
                if i[0] <= q <= i[1]:
                    # print(q, i)
                    res[c] = i[1]-i[0]+1
                    break
            else:
                res[c] = -1
        return res            