class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        se = n * (n + 1) // 2
        return se - sum(nums)