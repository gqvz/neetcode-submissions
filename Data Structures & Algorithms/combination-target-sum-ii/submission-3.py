class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        nums = candidates
        res = []
        nums.sort()
        def back(state, start, s):
            if s == target:
                res.append(state.copy())
                return
            i = start
            while i < len(nums):
                if i> start and nums[i] == nums[i-1]:
                    i +=1
                    continue
                num = nums[i]
                if s + num > target:
                    break
                state.append(num)
                back(state, i+1, s + num)
                state.pop()
                i += 1
        back([], 0, 0)
        return res