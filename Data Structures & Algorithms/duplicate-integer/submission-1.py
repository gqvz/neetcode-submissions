class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        l = [0] * len(nums)
        for i, n in enumerate(nums):
            if n in l[:i]:
                return True
            l[i] = n
        return False;
        