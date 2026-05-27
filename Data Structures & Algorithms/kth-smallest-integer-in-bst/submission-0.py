# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        c = 0
        res = -1
        def dfs(root: Optional[TreeNode]):
            nonlocal c
            nonlocal res
            if not root or res != -1:
                return
            dfs(root.left)
            if c == k-1 and res == -1:
                res = root.val
                return
            c += 1
            dfs(root.right)
        dfs(root)
        return res