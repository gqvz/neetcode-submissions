class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        m = min(nums)
        res = []
        nums.sort()
        def back(state, start, s):
            if s == target:
                res.append(state.copy())
                return
            for i in range(start, len(nums)):
                num = nums[i]
                if s + num > target:
                    continue
                state.append(num)
                back(state, i, s + num)
                state.pop()
        back([], 0, 0)
        return res
