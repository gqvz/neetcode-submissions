from bisect import bisect_right

class KthLargest:
    def __init__(self, k: int, nums: List[int]):
        self.arr = sorted(nums)
        self.k = k

    def add(self, val: int) -> int:
        self.arr.insert(bisect_right(self.arr, val), val)
        return self.arr[-self.k]
