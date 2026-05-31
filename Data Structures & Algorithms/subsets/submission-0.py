class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        for i in range(2**len(nums)):
            l = []
            n = 0
            while i:
                if i & 1 == 1:
                    l.append(nums[n])
                i >>= 1
                n += 1
            res.append(l)
        return res
