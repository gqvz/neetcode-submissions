class Solution:
    def jump(self, nums: List[int]) -> int:
        if len(nums) < 2: return 0
        if nums[0] >= len(nums): return 1
        r = nums[0]
        c = 1
        cmr = r
        for i, num in enumerate(nums):
            if r < i: return False
            if num + i > r:
                r = num + i
            if i == cmr and i != len(nums) - 1:
                c += 1
                cmr = r
        return c
