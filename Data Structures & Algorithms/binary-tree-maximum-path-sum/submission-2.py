# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        res = -1001
        def dfs(root: Optional[TreeNode]) -> int:
            nonlocal res
            if not root:
                return 0
            r = dfs(root.right)
            l = dfs(root.left)
            res = max(res, r + l + root.val, r + root.val, l+root.val, root.val)
            return max(r + root.val, l+root.val, root.val)
        d = dfs(root)
        res = max(res, d)
        return res
            