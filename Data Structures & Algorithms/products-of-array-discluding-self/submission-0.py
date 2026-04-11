class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        p = 1
        zeroc = 0
        zeroi = 0
        for i, num in enumerate(nums):
            if num is not 0:
                p *= num
            else: 
                zeroc += 1
                zeroi = i

        if zeroc > 1:
            return [0]*len(nums)
        elif zeroc == 1:
            ret = [0]*len(nums)
            ret[zeroi] = p
            return ret
        return [p // x for x in nums]
