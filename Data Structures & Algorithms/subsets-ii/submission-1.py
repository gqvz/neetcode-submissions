class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        state = []
        h = defaultdict(bool)
        def dfs(start):
            res.append(state.copy())
            for i in range(start, len(nums)):
                if i > start and nums[i] == nums[i-1]:
                    continue
                state.append(nums[i])
                dfs(i+1)
                state.pop()
        dfs(0)
        return res
