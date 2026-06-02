class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        h = defaultdict(bool)
        def dfs(state, depth):
            if depth == len(nums):
                if not h[tuple(state)]:
                    res.append(state.copy())
                    h[tuple(state)] = True
                return
            state.append(nums[depth])
            dfs(state, depth+1)
            state.pop()
            dfs(state, depth+1)
        dfs([], 0)
        return res
