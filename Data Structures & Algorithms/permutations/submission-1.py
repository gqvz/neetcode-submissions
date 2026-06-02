class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        def dfs(curr, left):
            if not left:
                res.append(curr.copy())
            for i in range(len(left)):
                n = left[i]
                curr.append(n)
                left.pop(i)
                dfs(curr, left)
                left.insert(i, n)
                curr.pop()
        dfs([], nums)
        return res
