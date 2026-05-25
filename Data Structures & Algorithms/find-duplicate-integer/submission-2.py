class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        for n in nums:
            k = abs(n)
            if nums[k-1] < 0: return k
            nums[k-1] *= -1
        return -1