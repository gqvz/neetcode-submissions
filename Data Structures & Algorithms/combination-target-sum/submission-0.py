class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        m = min(nums)
        res = []
        nums = sorted(nums)
        def inner(ct, ar):
            if ct < m:
                return
            if ct in nums:
                res.append(sorted(ar + [ct]))
            for num in nums:
                inner(ct - num, ar + [num])
        inner(target, [])
        return [list(x) for x in dict.fromkeys(map(tuple, res))]