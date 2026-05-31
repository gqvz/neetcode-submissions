class MedianFinder:

    def __init__(self):
        self.n = 0
        self.minh = []
        self.maxh = []

    def addNum(self, num: int) -> None:
        self.n += 1
        if self.n == 1:
            self.maxh.append(-num)
            # print("MAX ", sorted([-x for x in self.maxh]))
            # print("MIN ", sorted(self.minh))
            return
        if len(self.maxh) == len(self.minh):
            if num <= -self.maxh[0]:
                heapq.heappush(self.maxh, -num)
            else:
                heapq.heappush(self.minh, num)
        elif len(self.maxh) > len(self.minh):
            if num <= -self.maxh[0]:
                heapq.heappush(self.minh, -heapq.heapreplace(self.maxh, -num))
            else:
                heapq.heappush(self.minh, num)
        else:
            if num < self.minh[0]:
                heapq.heappush(self.maxh, -num)
            else:
                heapq.heappush(self.maxh, -heapq.heapreplace(self.minh, num))
        # print("MAX ", sorted([-x for x in self.maxh]))
        # print("MIN ", sorted(self.minh))

    def findMedian(self) -> float:
        if self.n % 2 == 0:
            return (-self.maxh[0] + self.minh[0]) / 2
        elif len(self.minh) > len(self.maxh):
            return self.minh[0]
        return -self.maxh[0]