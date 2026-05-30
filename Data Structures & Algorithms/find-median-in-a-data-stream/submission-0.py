from bisect import bisect_right
class MedianFinder:

    def __init__(self):
        self.a = []

    def addNum(self, num: int) -> None:
        self.a.insert(bisect_right(self.a, num), num)

    def findMedian(self) -> float:
        return self.a[len(self.a) // 2] if len(self.a) % 2 != 0 else (self.a[len(self.a) // 2] + self.a[len(self.a) // 2 -1]) / 2
        