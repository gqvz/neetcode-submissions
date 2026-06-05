class Solution:
    def canJump(self, nums: List[int]) -> bool:
        r = nums[0]
        for i, num in enumerate(nums):
            if r < i: return False
            r = max(r, num+i)
        return True
