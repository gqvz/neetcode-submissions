class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d: Dict[int, int] = defaultdict(int)
        for num in nums:
            d[num] += 1
        return [x for x, _ in sorted(d.items(), key=lambda i:-i[1])][0:k]